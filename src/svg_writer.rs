use crate::LayoutBox;

pub fn svg_with_header(b: &LayoutBox) -> xmlwriter::XmlWriter {
    let mut svg = xmlwriter::XmlWriter::new(xmlwriter::Options::default());
    svg.start_element("svg");
    svg.write_attribute("xmlns", "http://www.w3.org/2000/svg");
    svg.write_attribute("xmlns:xlink", "http://www.w3.org/1999/xlink");
    svg.write_attribute_fmt(
        "viewBox",
        format_args!("{} {} {} {}", b.x, b.y, b.width, b.height),
    );
    svg
}

pub fn write_box_to_svg(b: &LayoutBox, svg: &mut xmlwriter::XmlWriter) {
    svg.start_element("rect");
    svg.write_attribute("x", &b.x);
    svg.write_attribute("y", &b.y);
    svg.write_attribute("width", &b.width);
    svg.write_attribute("height", &b.height);
    svg.write_attribute("fill", "none");
    svg.write_attribute("stroke", "green");
    svg.end_element();
}

use std::path::PathBuf;
pub fn svg_output(output_path: &PathBuf, svg: xmlwriter::XmlWriter) -> Result<(), std::io::Error> {
    std::fs::write(output_path, svg.end_document())
}

use ttf_parser as ttf;

pub fn write_glyph_to_svg(
    glyph_id: ttf::GlyphId,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    struct Builder<'a>(&'a mut String);

    impl ttf::OutlineBuilder for Builder<'_> {
        fn move_to(&mut self, x: f32, y: f32) {
            use std::fmt::Write;
            write!(self.0, "M {} {} ", x, y).unwrap()
        }

        fn line_to(&mut self, x: f32, y: f32) {
            use std::fmt::Write;
            write!(self.0, "L {} {} ", x, y).unwrap()
        }

        fn quad_to(&mut self, x1: f32, y1: f32, x: f32, y: f32) {
            use std::fmt::Write;
            write!(self.0, "Q {} {} {} {} ", x1, y1, x, y).unwrap()
        }

        fn curve_to(&mut self, x1: f32, y1: f32, x2: f32, y2: f32, x: f32, y: f32) {
            use std::fmt::Write;
            write!(self.0, "C {} {} {} {} {} {} ", x1, y1, x2, y2, x, y).unwrap()
        }

        fn close(&mut self) {
            self.0.push_str("Z ")
        }
    }

    let scale = bbox.height / face.height() as f64;

    let mut path_buf = String::with_capacity(256);
    // path_buf.clear();
    let mut builder = Builder(&mut path_buf);
    let _ = match face.outline_glyph(glyph_id, &mut builder) {
        Some(v) => v,
        None => return,
    };
    if !path_buf.is_empty() {
        path_buf.pop(); // remove trailing space
    }

    let x = bbox.x;
    let y = bbox.y + bbox.height + face.descender() as f64 * scale;
    let transform = format!("matrix({} 0 0 {} {} {})", scale, -scale, x, y);

    svg.start_element("path");
    svg.write_attribute("d", &path_buf);
    svg.write_attribute("transform", &transform);
    svg.end_element();
}

pub fn write_glyph_metrics_to_svg(
    id: ttf::GlyphId,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    write_glyph_embox_to_svg(id, face, bbox, svg);
    write_glyph_horizontal_metric("baseline", 0., id, face, bbox, svg);
    write_glyph_horizontal_metric(
        "cap height",
        face.capital_height().unwrap().into(),
        id,
        face,
        bbox,
        svg,
    );
    write_glyph_horizontal_metric(
        "x height",
        face.x_height().unwrap().into(),
        id,
        face,
        bbox,
        svg,
    );
    write_glyph_horizontal_metric("ascender", face.ascender() as f64, id, face, bbox, svg);
    write_glyph_horizontal_metric("descender", face.descender() as f64, id, face, bbox, svg);
    write_glyph_vertical_metric(
        "",
        face.glyph_hor_side_bearing(id).unwrap() as f64,
        id,
        face,
        bbox,
        svg,
    );
    write_glyph_vertical_metric(
        "",
        face.glyph_hor_advance(id).unwrap() as f64
            - face.glyph_hor_side_bearing(id).unwrap() as f64,
        id,
        face,
        bbox,
        svg,
    );
    write_glyph_horizontal_segment_metric(
        "left bearing",
        -50.,
        0.,
        face.glyph_hor_side_bearing(id).unwrap() as f64,
        id,
        face,
        bbox,
        svg,
    );
    write_glyph_horizontal_segment_metric(
        "right bearing",
        -50.,
        face.glyph_hor_advance(id).unwrap() as f64
            - face.glyph_hor_side_bearing(id).unwrap() as f64,
        face.glyph_hor_advance(id).unwrap() as f64,
        id,
        face,
        bbox,
        svg,
    );
    write_glyph_horizontal_segment_metric(
        "advance width",
        -100.,
        0.,
        face.glyph_hor_advance(id).unwrap() as f64,
        id,
        face,
        bbox,
        svg,
    );
}

pub fn write_glyph_embox_to_svg(
    glyph_id: ttf::GlyphId,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    let scale = bbox.height / face.height() as f64;
    let bbox_w = face.glyph_hor_advance(glyph_id).unwrap() as f64 * scale;
    svg.start_element("rect");
    svg.write_attribute("x", &bbox.x);
    svg.write_attribute("y", &bbox.y);
    svg.write_attribute("width", &bbox_w);
    svg.write_attribute("height", &bbox.height);
    svg.write_attribute("fill", "none");
    svg.write_attribute("stroke", "green");
    svg.end_element();
}

pub fn write_glyph_char_info(c: &str, bbox: &LayoutBox, svg: &mut xmlwriter::XmlWriter) {
    svg.start_element("text");
    svg.write_attribute("x", &(bbox.x + 2.0));
    svg.write_attribute("y", &(bbox.y + bbox.height - 4.0));
    svg.write_attribute("font-size", "36");
    svg.write_attribute("fill", "gray");
    svg.write_text_fmt(format_args!("{}", &c));
    svg.end_element();
}

pub fn write_line_in_glyph_coordinate(
    x1: f64,
    y1: f64,
    x2: f64,
    y2: f64,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    let scale = bbox.height / face.height() as f64;
    let x = bbox.x;
    let y = bbox.y + bbox.height + face.descender() as f64 * scale;

    svg.start_element("path");
    svg.write_attribute("fill", "none");
    svg.write_attribute("stroke", "black");
    svg.write_attribute("stroke-width", "1");

    let mut path = String::with_capacity(256);
    use std::fmt::Write;
    write!(
        &mut path,
        "M {} {} L {} {} ",
        x + x1 * scale,
        y - y1 * scale,
        x + x2 * scale,
        y - y2 * scale,
    )
    .unwrap();
    path.pop();
    svg.write_attribute("d", &path);
    svg.end_element();
}

pub fn write_glyph_horizontal_metric(
    annotation: &str,
    metric_value: f64,
    glyph_id: ttf::GlyphId,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    write_line_in_glyph_coordinate(
        0.0,
        metric_value,
        face.glyph_hor_advance(glyph_id).unwrap() as f64,
        metric_value,
        face,
        bbox,
        svg,
    );

    let scale = bbox.height / face.height() as f64;
    let x = bbox.x;
    let y = bbox.y + bbox.height + face.descender() as f64 * scale;
    svg.start_element("text");
    svg.write_attribute("x", &(x - 50.0));
    svg.write_attribute("y", &(y - metric_value * scale + 5.));
    svg.write_attribute("font-size", "12");
    svg.write_attribute("fill", "gray");
    svg.write_text_fmt(format_args!("{}", annotation));
    svg.end_element();
}

pub fn write_glyph_vertical_metric(
    annotation: &str,
    metric_value: f64,
    _glyph_id: ttf::GlyphId,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    write_line_in_glyph_coordinate(
        metric_value,
        face.descender() as f64,
        metric_value,
        face.ascender() as f64,
        face,
        bbox,
        svg,
    );

    let scale = bbox.height / face.height() as f64;
    let x = bbox.x;
    let y = bbox.y + bbox.height + face.descender() as f64 * scale;
    svg.start_element("text");
    svg.write_attribute("x", &(x - 50.0));
    svg.write_attribute("y", &(y - metric_value * scale + 5.));
    svg.write_attribute("font-size", "12");
    svg.write_attribute("fill", "gray");
    svg.write_text_fmt(format_args!("{}", annotation));
    svg.end_element();
}

#[allow(clippy::too_many_arguments)]
pub fn write_glyph_horizontal_segment_metric(
    annotation: &str,
    y_offset: f64, // y_offset as in the Glyph origin coordinate
    start: f64,
    end: f64, // start and end all in glyph origin coordinate
    _glyph_id: ttf::GlyphId,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    let scale = bbox.height / face.height() as f64;
    let x = bbox.x;
    let y = bbox.y + bbox.height + (face.descender() as f64 - y_offset) * scale;

    svg.start_element("path");
    svg.write_attribute("fill", "none");
    svg.write_attribute("stroke", "blue");
    svg.write_attribute("stroke-width", "1");
    svg.write_attribute("marker-end", "url(#head)");
    svg.write_attribute("marker-start", "url(#head)");

    let mut path = String::with_capacity(256);
    use std::fmt::Write;
    write!(
        &mut path,
        "M {} {} L {} {} ",
        x + start * scale,
        y,
        x + end * scale,
        y,
    )
    .unwrap();
    path.pop();
    svg.write_attribute("d", &path);
    svg.end_element();

    svg.start_element("text");
    svg.write_attribute("x", &(x + (start + (end - start) / 2.) * scale - 12.));
    svg.write_attribute("y", &(y + 5.0));
    svg.write_attribute("font-size", "5");
    svg.write_attribute("fill", "blue");
    svg.write_text_fmt(format_args!("{}", annotation));
    svg.end_element();
}

#[allow(clippy::too_many_arguments)]
pub fn write_glyph_strip(
    y_offset: f64, // y_offset as in the Glyph origin coordinate
    start: f64,
    end: f64, // start and end all in glyph origin coordinate
    color: &str,
    _glyph_id: ttf::GlyphId,
    face: &ttf::Face,
    bbox: &LayoutBox,
    svg: &mut xmlwriter::XmlWriter,
) {
    let scale = bbox.height / face.height() as f64;
    let x = bbox.x;
    let y = bbox.y + bbox.height + (face.descender() as f64 - y_offset) * scale;

    svg.start_element("path");
    svg.write_attribute("stroke", color);
    svg.write_attribute("stroke-opacity", "0.5");
    svg.write_attribute("stroke-width", "5");
    svg.write_attribute("marker-end", "url(#head)");
    svg.write_attribute("marker-start", "url(#head)");

    let mut path = String::with_capacity(256);
    use std::fmt::Write;
    write!(
        &mut path,
        "M {} {} L {} {} ",
        x + start * scale,
        y,
        x + end * scale,
        y,
    )
    .unwrap();
    path.pop();
    svg.write_attribute("d", &path);
    svg.end_element();

    svg.start_element("text");
    svg.write_attribute("x", &(x + (start + (end - start) / 2.) * scale - 2.));
    svg.write_attribute("y", &(y + 10.0));
    svg.write_attribute("font-size", "5");
    svg.write_attribute("fill", color);
    svg.write_text_fmt(format_args!("{}", &(end - start)));
    svg.end_element();
}
