#!/usr/bin/env Rscript
if (!require(optparse)) { install.packages("optparse") }
if (!require(readr)) { install.packages("readr") }

opt = parse_args(OptionParser(option_list = list(
  make_option(c("-d", "--dir"), type = "character", default = NULL,
              help = "input files dir", metavar = "character"),
  make_option(c("-s", "--selector"), type = "character", default = NULL,
              help = "selected column", metavar = "character"),
  make_option(c("-o", "--out"), type = "character", default = "out.txt",
              help = "output file name [default= %default]", metavar = "character")
)));

if (is.null(opt$dir)) {
  print_help(opt_parser)
  stop("Input csv files dir is requred", call. = FALSE)
}

if (is.null(opt$selector)) {
  print_help(opt_parser)
  stop("Column selector is required", call. = FALSE)
}

if (is.null(opt$out)) {
  print_help(opt_parser)
  stop("Output file is required", call. = FALSE)
}

files_from_dir = list.files(path = opt$dir, pattern = "*_output.csv", all.files = FALSE,
           full.names = FALSE, recursive = FALSE,
           ignore.case = FALSE, include.dirs = FALSE, no.. = FALSE)

result = data.frame(1:120)
colnames(result) <- c("chunk")

for (file_name in files_from_dir) {
  content = readr::read_csv(file_name)

  selected_column = content[[opt$selector]]

  result[[file_name]] <- selected_column
}

readr::write_csv(result, opt$out, append = TRUE, col_names = TRUE)



