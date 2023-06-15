use ttf_parser as ttf;

use kern_demo::svg_writer::*;
use kern_demo::LayoutBox;

use clap::Parser;

#[derive(Parser)]
#[command(name = "Glyph Psy")]
#[command(author = "Jialin Lu. <luxxxlucy@gmail.com>")]
#[command(version = "0.1")]
#[command(about = "Export a glyph from a font file as SVG", long_about = None)]
struct Args {
    #[arg(long)]
    font_source_path: std::path::PathBuf,
    #[arg(long)]
    output_path: std::path::PathBuf,
    #[arg(long)]
    glyph: char,
}

fn main() {
    let args = Args::parse();

    println!("font source ttf path: {:?}", args.font_source_path);
    println!("output svg path: {:?}", args.output_path);
    println!("glyph: {:?}", args.glyph);

    if let Err(e) = process(args) {
        eprintln!("Error: {}.", e);
        std::process::exit(1);
    }
}

#[allow(clippy::too_many_arguments)]
fn draw_single_glyph(
    x_margin: f64,
    y_margin: f64,
    height: f64,
    face: &ttf::Face,
    id: ttf::GlyphId,
    output_path: &std::path::PathBuf,
) -> Result<(), Box<dyn std::error::Error>> {
    let scale = height / face.height() as f64;
    let glyph_width = face.glyph_hor_advance(id).unwrap() as f64 * scale;

    let canvas_box = LayoutBox {
        x: 0.,
        y: 0.,
        width: 2. * x_margin + glyph_width,
        height: 2. * y_margin + height,
    };
    // main canvas
    let mut svg = svg_with_header(&canvas_box);
    // misc information: write the char at the corner
    write_glyph_char_info(face.glyph_name(id).unwrap(), &canvas_box, &mut svg);

    let main_box = LayoutBox {
        x: x_margin,
        y: y_margin,
        width: glyph_width,
        height,
    };

    write_glyph_to_svg(id, face, &main_box, &mut svg);
    write_glyph_metrics_to_svg(id, face, &main_box, &mut svg);

    // output
    svg_output(output_path, svg)?;
    Ok(())
}

fn process(args: Args) -> Result<(), Box<dyn std::error::Error>> {
    let font_data = std::fs::read(&args.font_source_path)?;
    #[allow(unused_mut)]
    let mut face = ttf::Face::parse(&font_data, 0)?;
    let c = args.glyph;
    let id = face.glyph_index(c).ok_or(format!(
        "this glyph {} not found in this font {:?}",
        c, args.font_source_path
    ))?;

    draw_single_glyph(
        100., // x_margin
        100., // y_margin
        300., // height
        &face,
        id,
        &args.output_path,
    )?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use crate::process;
    use crate::Args;

    use file_diff::diff;

    #[test]
    fn singel_glyph_show() {
        let font_path = "./asset/Helvetica.ttc";
        let output_path = "glyph_psy_Helvetica_A_test.svg";
        let ground_truth_output_path = "./asset/result/Helvetica A.svg";
        let test_arg = Args {
            font_source_path: font_path.into(),
            output_path: output_path.into(),
            glyph: 'A',
        };
        assert!(process(test_arg).is_ok());
        assert!(std::path::Path::new(output_path).exists());
        assert!(diff(output_path, ground_truth_output_path));
        assert!(std::fs::remove_file(output_path).is_ok());
    }
}
