# Kern: experiments

see https://luxxxlucy.github.io/projects/2023_kern/kerning.html

## Definition

We start with a Shape

A glyph is a shape together with some other information.

A kerning table is a key-value store of left-right-glyph pair mapping to a numerical value.

A kerning instance is a kerning table together with the involving glyphs.

## Run

Some scripts are saved in the `scripts/` folder.

We use `Helvetica` in the `asset` folder for the test.

inspect a glyph from a font source and export annotated version as SVG
```
cargo run --bin glyph_psy -- --font-source-path ./font_of_interest.otf --output-path ./test.svg --glyph A

```
Result lookes like [A in Helvetica](./asset//result/Helvetica%20A.svg)


Inspect and export pairs (kerned v.s. not kerend)


```
cargo run --bin kern_psy -- --font-source-path ./asset/Helvetica.ttc --left A --right T --use-kern --output-path "Helvetica AT kerned.svg"
or
cargo run --bin kern_psy -- --font-source-path ./asset/Helvetica.ttc --left A --right T --output-path "Helvetica AT not kerned.svg"
```

Result lookes like [T A kerned in Helvetica](./asset//result/Helvetica%20AT%20kerned.svg)
[T A not kerned in Helvetica](./asset//result/Helvetica%20AT%20not%20kerned.svg)


Run with all pairs (pairs from the kern table)
```
cargo run --bin kern_sol -- --font-source-path ./asset/Helvetica.ttc --output-path test-sol
```

Note that if we do not specify the number of satisfiable pairs, then we are asking the Z3 solver to maximize the number, which is costy.

Or run with specified pairs (note that by this way we will generate kerning=0 pairs for pairs that are not presented in the kern table, as 0 is the deafault value)
```
cargo run --bin kern_sol -- --k 5 --font-source-path ./asset/Helvetica.ttc --output-path result/solve-helvetica-4-pair-AL-VT --specify-pairs "A,T;A,V;L,T;L,V" --number 4
```

You can specify the number
```
cargo run --release --bin kern_sol -- --k 5 --font-source-path ./asset/Helvetica.ttc --output-path result/all-helvetica-pairs --number 105
```

This should be computed quicker.


Top 200 pairs (from andre fuchs https://github.com/andre-fuchs/kerning-pairs)
```
 clear; cargo run --release --bin kern_sol -- --k 50 --font-source-path ./asset/Helvetica.ttc --output-path result/solve-helvetica-en-top-200 --specify-pairs "$(./en_top.py)"
```

All pairs (A to Z and a to z) in the latin alphabet (2704 pairs in total)
```
 clear; cargo run --release --bin kern_sol -- --k 50 --font-source-path ./asset/Helvetica.ttc --output-path result/solve-helvetica-en-top-200 --specify-pairs "$(./pair_gen.py)"
```