#![allow(dead_code)]

pub mod svg_writer;

use ttf::GlyphId;
use ttf_parser as ttf;

pub struct LayoutBox {
    pub x: f64,
    pub y: f64,
    pub width: f64,
    pub height: f64,
}

pub struct Point {
    pub x: f64,
    pub y: f64,
}

#[derive(Debug, Clone, Copy)]
// #[derive(PartialEq, Eq, Hash)]
pub struct KerningPair {
    pub left: GlyphId,
    pub right: GlyphId,
    pub value: f64,
}

impl PartialEq for KerningPair {
    fn eq(&self, other: &Self) -> bool {
        self.left == other.left
        &&
        self.right == other.right
    }
}
impl Eq for KerningPair {}

impl std::hash::Hash for KerningPair {
    fn hash<H: std::hash::Hasher>(&self, state: &mut H) {
        self.left.hash(state);
        self.right.hash(state);
    }
}

pub enum Stripe {
    Left(GlyphId, Point, f64),
    Right(GlyphId, Point, f64),
}

pub struct Instance {
    pub stripes: Vec<Stripe>,
}

fn print_opentype_layout(name: &str, table: &ttf_parser::opentype_layout::LayoutTable) {
    println!("OpenType {}:", name);
    println!("  Scripts:");
    for script in table.scripts {
        println!("    {}", script.tag);

        if script.languages.is_empty() {
            println!("      No languages");
            continue;
        }

        println!("      Languages:");
        for lang in script.languages {
            println!("        {}", lang.tag);
        }
    }

    let mut features: Vec<_> = table.features.into_iter().map(|f| f.tag).collect();
    features.dedup();
    println!("  Features:");
    for feature in features {
        println!("    {}", feature);
    }
}


pub fn get_kerning_pairs(face: &ttf::Face) -> Option<Vec<KerningPair>> {
    use ttf_parser::gpos::*;
    use ttf_parser::opentype_layout::*;
    if let Some(gpos) = face.tables().gpos {
        if let Some(features) = gpos.features.into_iter().find_map(|s| 
            if format!("{}", s.tag) == "kern" {
                Some(s)
            } else { None }
        ) {
            let t = gpos.lookups.get(features.lookup_indices.get(0).unwrap()).unwrap();
            if let Some(PositioningSubtable::Pair(pairs)) = t.subtables.get(0) {
                if let PairAdjustment::Format1 {coverage, sets} = pairs {
                    let mut count = 0;
                    if let Coverage::Format2 { records } = coverage {
                        println!("records len {}", records.len());
                        let mut ret :Vec<KerningPair> = Vec::new();
                        for r in records.into_iter() {
                            let pair_set = sets.get(r.value).unwrap();
                            for temp in 0..10000 {
                                let id = GlyphId(temp);
                                if let Some(result) = pair_set.get(id) {
                                    ret.push(
                                        KerningPair {
                                            left: r.start,
                                            right: r.start,
                                            value: (result.0.x_advance + result.1.x_advance) as f64
                                        }
                                    );
                                    count += 1;
                                }
                            }
                        }
                        return Some(ret);
                    }
                    println!("in total {}", count);
                } else {
                    println!("format 2 PairAdjustment not supported yet");
                }
            } else {
                println!("no kern feature in GPOS table");
            }
        } else {
            println!("no kern feature in GPOS table");
        }
    } else {
        println!("no GPOS table");
    }
    match face.tables().kern {
        Some(kern) => kern.subtables.into_iter().find_map(|s| match s.format {
            ttf::kern::Format::Format0(kern_table) => Some(
                kern_table
                    .pairs
                    .into_iter()
                    .map(|p| KerningPair {
                        left: p.left(),
                        right: p.right(),
                        value: p.value as f64,
                    })
                    .collect::<Vec<KerningPair>>(),
            ),
            _ => {
                println!("not format 0");
                None
            },
        }),
        None => {
                println!("no kern table");
                None
        }
    }
}

pub fn get_kern_pair_with_default(
    kerning_pairs: &[KerningPair],
    left: GlyphId,
    right: GlyphId,
) -> KerningPair {
    kerning_pairs
        .iter()
        .find(|p| p.left == left && p.right == right)
        .or({
            Some(&KerningPair {
                left,
                right,
                value: 0.,
            })
        })
        .copied()
        .unwrap()
}
