use clap::Parser;
use kern_demo::svg_writer::{svg_output, svg_with_header, write_glyph_to_svg, write_glyph_metrics_to_svg, write_glyph_embox_to_svg};
use kern_demo::*;
use ttf_parser as ttf;

#[derive(Parser)]
#[command(name = "kern psy")]
#[command(author = "Jialin Lu. <luxxxlucy@gmail.com>")]
#[command(version = "0.1")]
#[command(about = "visualize a kern pair", long_about = None)]
struct Args {
    #[arg(long)]
    font_source_path: std::path::PathBuf,
    #[arg(long)]
    output_path: std::path::PathBuf,
    #[arg(long)]
    left: char,
    #[arg(long)]
    right: char,
    #[arg(long)]
    use_kern: bool,
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
fn draw_kerning_pair(
    x_margin: f64,
    y_margin: f64,
    height: f64,
    face: &ttf::Face,
    left_id: ttf::GlyphId,
    right_id: ttf::GlyphId,
    kern: Option<f64>, // we do not kern if None
    output_path: &std::path::PathBuf,
) -> Result<(), Box<dyn std::error::Error>> {
    let scale = height / face.height() as f64;

    let left_width = face.glyph_hor_advance(left_id).unwrap() as f64 * scale;
    let right_width = face.glyph_hor_advance(right_id).unwrap() as f64 * scale;
    let kern_distance = if let Some(kern_distance) = kern {
        kern_distance * scale
    } else {
        0.
    };

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
    // write_glyph_embox_to_svg(left_id, face, &left_box, &mut svg);
    // write_glyph_metrics_to_svg(left_id, face, &left_box, &mut svg);
    let right_box = LayoutBox {
        x: x_margin + left_width + kern_distance,
        y: y_margin,
        width: left_width,
        height,
    };
    write_glyph_to_svg(right_id, face, &right_box, &mut svg);
    // write_glyph_embox_to_svg(right_id, face, &right_box, &mut svg);
    // write_glyph_metrics_to_svg(right_id, face, &right_box, &mut svg);

    // output
    svg_output(output_path, svg)?;
    Ok(())
}

fn process(args: Args) -> Result<(), Box<dyn std::error::Error>> {
    let font_data = std::fs::read(&args.font_source_path)?;
    #[allow(unused_mut)]
    let mut face = ttf::Face::parse(&font_data, 0)?;

    let kerning_pairs = get_kerning_pairs(&face).unwrap();

    let target_left_glyph = face.glyph_index(args.left).unwrap();
    let target_right_glyph = face.glyph_index(args.right).unwrap();
    println!(
        "The kerning pair of interest is {}({:?}), {}({:?})",
        args.left, target_left_glyph, args.right, target_right_glyph
    );

    println!("In total {} kerning pairs", kerning_pairs.len());

    let p = kerning_pairs
        .iter()
        .find(|p| p.left == target_left_glyph && p.right == target_right_glyph)
        .ok_or(format!(
            "this pair({}, {}) not found in this font",
            args.left, args.right
        ))?;
    println!(" the pair is {:?}", p);
    draw_kerning_pair(
        100.,
        100.,
        300.,
        &face,
        p.left,
        p.right,
        if args.use_kern { Some(p.value) } else { None },
        &args.output_path,
    )?;
    Ok(())
}

#[allow(non_snake_case)]
#[cfg(test)]
mod tests {
    use crate::process;
    use crate::Args;

    use file_diff::diff;

    #[test]
    fn test_A_T_kerned() {
        let font_path = "./asset/Helvetica.ttc";
        let output_path = "glyph_psy_Helvetica_A_T_kerned.svg";
        let ground_truth_output_path = "./asset/result/Helvetica AT kerned.svg";
        let test_arg = Args {
            font_source_path: font_path.into(),
            output_path: output_path.into(),
            left: 'A',
            right: 'T',
            use_kern: true,
        };
        assert!(process(test_arg).is_ok());
        assert!(std::path::Path::new(output_path).exists());
        assert!(diff(output_path, ground_truth_output_path));
        assert!(std::fs::remove_file(output_path).is_ok());
    }

    #[test]
    fn test_A_T_not_kerned() {
        let font_path = "./asset/Helvetica.ttc";
        let output_path = "glyph_psy_Helvetica_A_T_not_kerned.svg";
        let ground_truth_output_path = "./asset/result/Helvetica AT not kerned.svg";
        let test_arg = Args {
            font_source_path: font_path.into(),
            output_path: output_path.into(),
            left: 'A',
            right: 'T',
            use_kern: false,
        };
        assert!(process(test_arg).is_ok());
        assert!(std::path::Path::new(output_path).exists());
        assert!(diff(output_path, ground_truth_output_path));
        assert!(std::fs::remove_file(output_path).is_ok());
    }

    #[test]
    fn pair_not_find() {
        let font_path = "./asset/Helvetica.ttc";
        let output_path = "glyph_psy_Helvetica_A_T_kerned.svg";
        let test_arg = Args {
            font_source_path: font_path.into(),
            output_path: output_path.into(),
            left: 'T',
            right: 'T',
            use_kern: true,
        };
        assert!(process(test_arg).is_err());
        assert!(!std::path::Path::new(output_path).exists());
    }
}
