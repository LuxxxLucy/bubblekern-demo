use ttf_parser as ttf;

use kern_demo::svg_writer::*;

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

fn process(args: Args) -> Result<(), Box<dyn std::error::Error>> {
    let font_data = std::fs::read(&args.font_source_path)?;
    #[allow(unused_mut)]
    let mut face = ttf::Face::parse(&font_data, 0)?;
    let c = args.glyph;
    let id = face.glyph_index(c).unwrap();

    let canvas_box = LayoutBox {
        x: 0.,
        y: 0.,
        width: 500.,
        height: 500.,
    };
    let mut svg = svg_with_header(&canvas_box);

    // main canvas
    write_box_to_svg(&canvas_box, &mut svg);
    // misc information: write the char at the corner
    write_glyph_char_info(c, &canvas_box, &mut svg);

    let main_box = LayoutBox {
        x: 100.,
        y: 50.,
        width: 400.,
        height: 400.,
    };
    write_glyph_to_svg(id, &face, &main_box, &mut svg);
    write_glyph_embox_to_svg(id, &face, &main_box, &mut svg);

    write_glyph_horizontal_metric("baseline", 0., id, &face, &main_box, &mut svg);
    write_glyph_horizontal_metric(
        "cap height",
        face.capital_height().unwrap().into(),
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_horizontal_metric(
        "x height",
        face.x_height().unwrap().into(),
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_horizontal_metric(
        "ascender",
        face.ascender() as f64,
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_horizontal_metric(
        "descender",
        face.descender() as f64,
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_vertical_metric(
        "",
        face.glyph_hor_side_bearing(id).unwrap() as f64,
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_vertical_metric(
        "",
        face.glyph_hor_advance(id).unwrap() as f64
            - face.glyph_hor_side_bearing(id).unwrap() as f64,
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_horizontal_segment_metric(
        "left bearing",
        -50.,
        0.,
        face.glyph_hor_side_bearing(id).unwrap() as f64,
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_horizontal_segment_metric(
        "right bearing",
        -50.,
        face.glyph_hor_advance(id).unwrap() as f64
            - face.glyph_hor_side_bearing(id).unwrap() as f64,
        face.glyph_hor_advance(id).unwrap() as f64,
        id,
        &face,
        &main_box,
        &mut svg,
    );
    write_glyph_horizontal_segment_metric(
        "advance width",
        -100.,
        0.,
        face.glyph_hor_advance(id).unwrap() as f64,
        id,
        &face,
        &main_box,
        &mut svg,
    );

    // output
    svg_output(&args.output_path, svg)?;
    Ok(())
}
