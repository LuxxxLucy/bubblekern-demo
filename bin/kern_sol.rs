use clap::Parser;
use kern_demo::svg_writer::{
    svg_output, svg_with_header, write_glyph_embox_to_svg, write_glyph_strip, write_glyph_to_svg,
};
use kern_demo::*;
use ttf::GlyphId;
use ttf_parser as ttf;

#[allow(non_snake_case)]
#[derive(Parser)]
#[command(name = "kern demo")]
#[command(author = "Jialin Lu. <luxxxlucy@gmail.com>")]
#[command(version = "0.1")]
#[command(
    about = "solve kerning with discrete bubble strip.",
    long_about = " It will extract all pairs from the kern table and try to solve it with a specified K (number of strip/bubble) that at least <number> pairs are satisfied. If <number> is not satisfied, we then will ask Z3 to maximize. The paris can also be specified in the form of `A,T;A,W` separated bt semicolon"
)]
struct Args {
    #[arg(long)]
    K: usize,
    #[arg(long)]
    number: Option<i64>,
    #[arg(long)]
    font_source_path: std::path::PathBuf,
    #[arg(long)]
    output_path: std::path::PathBuf,
    #[arg(long)]
    specify_pairs: Option<String>,
    #[arg(long)]
    append_kern_table: bool,
}

fn main() {
    let args = Args::parse();

    println!("font source ttf path: {:?}", args.font_source_path);
    if let Err(e) = process(args) {
        eprintln!("Error: {}.", e);
        std::process::exit(1);
    }
}

#[allow(clippy::too_many_arguments)]
fn draw_kerning_pair_with_strip(
    x_margin: f64,
    y_margin: f64,
    height: f64,
    face: &ttf::Face,
    left_id: ttf::GlyphId,
    right_id: ttf::GlyphId,
    kern: f64,
    problem_instance: &Instance,
    output_path: &std::path::PathBuf,
) {
    let scale = height / face.height() as f64;

    let left_width = face.glyph_hor_advance(left_id).unwrap() as f64 * scale;
    let right_width = face.glyph_hor_advance(right_id).unwrap() as f64 * scale;
    let kern_distance = kern * scale;

    let canvas_box = LayoutBox {
        x: 0.,
        y: 0.,
        width: 2. * x_margin + left_width + right_width + kern_distance,
        height: 2. * y_margin + height,
    };
    let mut svg = svg_with_header(&canvas_box);

    let left_box = LayoutBox {
        x: x_margin,
        y: y_margin,
        width: left_width,
        height,
    };
    write_glyph_to_svg(left_id, face, &left_box, &mut svg);
    write_glyph_embox_to_svg(left_id, face, &left_box, &mut svg);
    let right_box = LayoutBox {
        x: x_margin + left_width + kern_distance,
        y: y_margin,
        width: left_width,
        height,
    };
    write_glyph_to_svg(right_id, face, &right_box, &mut svg);
    write_glyph_embox_to_svg(right_id, face, &right_box, &mut svg);

    for stripe in problem_instance.stripes.iter() {
        match stripe {
            Stripe::Left(id, point, value) => {
                if *id == left_id {
                    write_glyph_strip(
                        point.y,
                        point.x,
                        point.x + value,
                        "red",
                        *id,
                        face,
                        &left_box,
                        &mut svg,
                    );
                }
            }
            Stripe::Right(id, point, value) => {
                if *id == right_id {
                    write_glyph_strip(
                        point.y,
                        point.x - value,
                        point.x,
                        "blue",
                        *id,
                        face,
                        &right_box,
                        &mut svg,
                    );
                }
            }
        }
    }
    svg_output(output_path, svg).unwrap();
}

#[allow(non_snake_case)]
fn solve_problem_instance(
    kerning_pairs: &[KerningPair],
    K: usize,
    number: Option<i64>,
    face: &ttf::Face,
) -> Result<(Instance, Vec<(GlyphId, GlyphId, bool)>), Box<dyn std::error::Error>> {
    use std::collections::HashSet;
    let left_ids: Vec<GlyphId> = kerning_pairs
        .iter()
        .map(|p| p.left)
        .collect::<HashSet<_>>()
        .into_iter()
        .collect();
    let right_ids: Vec<GlyphId> = kerning_pairs
        .iter()
        .map(|p| p.right)
        .collect::<HashSet<_>>()
        .into_iter()
        .collect();

    println!("In total {} kerning pairs", kerning_pairs.len());
    println!("In total {} Left side glyphs", left_ids.len());
    println!("In total {} Right side glyphs", right_ids.len());

    use z3::ast::Ast;
    use z3::ast::Bool;
    use z3::*;

    let cfg = z3::Config::new();
    let ctx = Context::new(&cfg);

    use std::collections::BTreeMap;
    let mut left_side = BTreeMap::new();
    for id in left_ids.iter() {
        let mut stripe_for_it = Vec::new();
        for i in 0..K {
            let s = ast::Int::new_const(&ctx, format!("{}_{}_{}", "left", id.0, i));
            stripe_for_it.push(s);
        }
        left_side.insert(id, stripe_for_it);
    }
    let mut right_side = BTreeMap::new();
    for id in right_ids.iter() {
        let mut stripe_for_it = Vec::new();
        for i in 0..K {
            let s = ast::Int::new_const(&ctx, format!("{}_{}_{}", "left", id.0, i));
            stripe_for_it.push(s);
        }
        right_side.insert(id, stripe_for_it);
    }
    let mut bo_list = BTreeMap::new();
    for p in kerning_pairs.iter() {
        bo_list.insert(
            (p.left, p.right),
            Bool::new_const(&ctx, format!("b{},{}", p.left.0, p.right.0)),
        );
    }

    let mut formulas = Vec::<Bool<'_>>::new();
    for p in kerning_pairs.iter() {
        let mut inequations = Vec::<Bool<'_>>::new();
        let mut equations = Vec::<Bool<'_>>::new();
        for i in 0..K {
            let left_strip = &left_side[&p.left][i];
            let right_strip = &right_side[&p.right][i];
            let left_x = face.glyph_hor_advance(p.left).unwrap() as f64 / 2.;
            let right_x = face.glyph_hor_advance(p.right).unwrap() as f64 / 2.;
            let distance =
                face.glyph_hor_advance(p.left).unwrap() as f64 + p.value + right_x - left_x;
            inequations
                .push(ast::Int::from_i64(&ctx, distance as i64).ge(&(left_strip + right_strip)));
            equations
                .push(ast::Int::from_i64(&ctx, distance as i64)._eq(&(left_strip + right_strip)));
        }

        let bo = &bo_list[&(p.left, p.right)];
        formulas.push(bo.ite(
            &ast::Bool::and(
                &ctx,
                &[
                    &ast::Bool::or(&ctx, &(equations.iter().collect::<Vec<&_>>())),
                    &ast::Bool::and(&ctx, &(inequations.iter().collect::<Vec<&_>>())),
                ],
            ),
            &ast::Bool::from_bool(&ctx, true),
        ));
    }

    let query = ast::Bool::and(&ctx, &(formulas.iter().collect::<Vec<&_>>()));

    let sat_number = ast::Int::add(
        &ctx,
        &bo_list
            .values()
            .map(|v| v.ite(&ast::Int::from_u64(&ctx, 1), &ast::Int::from_u64(&ctx, 0)))
            .collect::<Vec<_>>()
            .iter()
            .collect::<Vec<&_>>(),
    );

    let model = match number {
        Some(num) => {
            let solver = z3::Solver::new(&ctx);
            solver.assert(&query);
            solver.assert(
                &ast::Int::from_i64(&ctx, num).le(&sat_number)
            );
            match solver.check() {
                z3::SatResult::Unknown => {
                    return Err("solve fail unknown reason".into());
                }
                z3::SatResult::Unsat => {
                    return Err("solve fail not satisfiable".into());
                }
                z3::SatResult::Sat => {
                    solver.get_model().unwrap()
                }
            }
        },
        None => {
            let solver = Optimize::new(&ctx);
            solver.assert(&query);
            solver.maximize(&sat_number);
            match solver.check(&[]) {
                z3::SatResult::Unknown => {
                    return Err("solve fail unknown reason".into());
                }
                z3::SatResult::Unsat => {
                    return Err("solve fail not satisfiable".into());
                }
                z3::SatResult::Sat => {
                    solver.get_model().unwrap()
                }
            }
        }
    };

    let mut stripes = Vec::new();
    for &id in left_side.keys() {
        if let Some(inferred_stripes) = left_side.get(id) {
            for (i, var) in inferred_stripes.iter().enumerate() {
                let val: i64 = model.eval(var, true).unwrap().as_i64().unwrap();

                let y = face.height() as f64 / (K as f64 + 1.) * (i as f64 + 1.)
                    + face.descender() as f64;
                let x = face.glyph_hor_advance(*id).unwrap() as f64 / 2.;
                let strip = Stripe::Left(*id, Point { x, y }, val as f64);
                stripes.push(strip);
            }
        }
    }
    for &id in right_side.keys() {
        if let Some(inferred_stripes) = right_side.get(id) {
            for (i, var) in inferred_stripes.iter().enumerate() {
                let val: i64 = model.eval(var, true).unwrap().as_i64().unwrap();
                let y = face.height() as f64 / (K as f64 + 1.) * (i as f64 + 1.)
                    + face.descender() as f64;
                let x = face.glyph_hor_advance(*id).unwrap() as f64 / 2.;
                let strip = Stripe::Right(*id, Point { x, y }, val as f64);
                stripes.push(strip);
            }
        }
    }

    let pairs_sol_results: Vec<(GlyphId, GlyphId, bool)> = bo_list
        .iter()
        .map(|(key, bo)| (key.0, key.1, model.eval(bo, true).unwrap().as_bool().unwrap())).collect();


    Ok((Instance { stripes }, pairs_sol_results))
}

#[allow(non_snake_case)]
fn process(args: Args) -> Result<(), Box<dyn std::error::Error>> {
    let font_data = std::fs::read(&args.font_source_path)?;
    #[allow(unused_mut)]
    let mut face = ttf::Face::parse(&font_data, 0)?;

    let all_kerning_pairs = match get_kerning_pairs(&face) {
        Some(pairs) => pairs,
        _ => 
        {
            println!("error: get kerning pair from table failed");
            return Err("error: get kerning pair from table failed".into())
        }
    };

    fn parse_pairs(s: &str) -> Result<Vec<(char, char)>, &'static str> {
        let mut pairs = Vec::new();
        let mut idx = 0;
        while idx < s.len() {
            if s.chars().nth(idx) == Some(';') {
                idx += 1;
                continue;
            }
            let string = &s[idx..idx+3];
            let left: char = string.chars().nth(0).unwrap();
            let right: char = string.chars().nth(2).unwrap();
            pairs.push((left, right));
            idx += 3;
        }

        Ok(pairs)
    }

    let kerning_pairs: Vec<KerningPair> = if let Some(specify_pairs) = args.specify_pairs {
        let pairs = parse_pairs(&specify_pairs)?
            .iter()
            .map(|p| {
                get_kern_pair_with_default(
                    &all_kerning_pairs,
                    face.glyph_index(p.0).unwrap(),
                    face.glyph_index(p.1).unwrap(),
                )
            })
            .collect();
        if args.append_kern_table
        {
            use std::collections::HashSet;
            [pairs, all_kerning_pairs].concat()
            .into_iter()
            .collect::<HashSet<KerningPair>>()
            .into_iter()
            .collect::<Vec<KerningPair>>()
        }
        else
        {
            pairs
        }
    } else {
        all_kerning_pairs
    };

    let (instance, pairs_sol_result) = solve_problem_instance(&kerning_pairs, args.K, args.number,  &face)?;

    let solved_pairs = pairs_sol_result.iter().filter(|(_,_,b)| *b).collect::<Vec<_>>();
    println!("number of solved pairs is {}", solved_pairs.len());
    println!("solved pairs are\n{:?}", solved_pairs.iter().map(|(l,r,_)| 
            format!("{},{}" , &face.glyph_name(*l).unwrap(), &face.glyph_name(*r).unwrap())
        ).collect::<Vec<_>>()
    );

    let unsolved_pairs = pairs_sol_result.iter().filter(|(_,_,b)| !*b).collect::<Vec<_>>();
    println!("number of not solved pairs is {}", unsolved_pairs.len());
    println!("not solved pairs are\n{:?}", unsolved_pairs.iter().map(|(l,r,_)| 
            format!("{},{}" , &face.glyph_name(*l).unwrap(), &face.glyph_name(*r).unwrap())
        ).collect::<Vec<_>>()
    );


    if std::fs::metadata(&args.output_path).is_err() {
        std::fs::create_dir_all(&args.output_path)?;
    }
    for p in kerning_pairs.iter() {
        let left_name = face.glyph_name(p.left).unwrap();
        let right_name = face.glyph_name(p.right).unwrap();
        draw_kerning_pair_with_strip(
            100.,
            100.,
            300.,
            &face,
            p.left,
            p.right,
            p.value,
            &instance,
            &std::path::PathBuf::from(format!(
                "{}/{}_{}_{}.svg",
                &args.output_path.display(),
                args.K,
                left_name,
                right_name
            )),
        );
    }

    println!("Exit normally.");
    Ok(())
}

#[allow(non_snake_case)]
#[cfg(test)]
mod tests {
    use crate::process;
    use crate::Args;

    #[test]
    fn test_ATLV_all() {
        let font_path = "./asset/Helvetica.ttc";
        let output_path = "./test_result/solve-helvetica-4-pair-AL-VT-test";
        let test_arg = Args {
            K: 5,
            number: Some(4),
            font_source_path: font_path.into(),
            output_path: output_path.into(),
            specify_pairs: Some(String::from("A,T;A,V;L,T;L,V")),
            append_kern_table: false
        };
        assert!(process(test_arg).is_ok());
        assert!(std::path::Path::new(output_path).exists());
        assert!(std::fs::remove_dir_all(output_path).is_ok());
    }
}
