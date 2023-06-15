# specify the target path
target_path="~/Library/Fonts/"

# iterate over each file in target_path with .a, .b, .c extensions
[ -d "result/solve-loop" ] || mkdir "result/solve-loop"

fontfilenames=`ls ~/Library/Fonts/*.{otf,ttf,TTF}`
for file in $fontfilenames
do
    echo "$file"
    # check if file exists
    if [ -f "$file" ]
    then
        # get the file name without the extension
        file_name=$(basename "$file" .${file##*.})
        echo "$file_name"


        [ -d "result/solve-loop/$file_name" ] || mkdir "result/solve-loop/$file_name"

        # run program on the file and pipe the result into a text file with the same name
        # cargo run --release --bin kern_sol -- --k 50 --font-source-path "$file" --output-path "result/solve-loop/$file_name" --specify-pairs "$(./en_top.py)" --append-kern-table > "result/solve-loop/$file_name/result.txt"
        cargo run --release --bin kern_sol -- --k 50 --font-source-path "$file" --output-path "result/solve-loop/$file_name" --specify-pairs "$(./en_top.py)" > "result/solve-loop/$file_name/result.txt"
    fi
done
