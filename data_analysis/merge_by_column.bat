set merge_dir="."
set merge_column="median"
set output_file="median_merged.csv"

Rscript .\merge_files_by_column.R -d %merge_dir% -s %merge_column% -o %output_file%