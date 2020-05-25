#!/usr/bin/env Rscript
if (!require(optparse)) { install.packages("optparse") }
if (!require(readr)) { install.packages("readr") }

opt = parse_args(OptionParser(option_list = list(
  make_option(c("-f", "--file"), type = "character", default = NULL,
              help = "input file name", metavar = "character"),
  make_option(c("-s", "--selector"), type = "character", default = NULL,
              help = "selected field", metavar = "character"),
  make_option(c("-o", "--out"), type = "character", default = "out.txt",
              help = "output file name [default= %default]", metavar = "character")
)));

if (is.null(opt$file)) {
  print_help(opt_parser)
  stop("Input csv file is requred", call. = FALSE)
}

if (is.null(opt$selector)) {
  print_help(opt_parser)
  stop("Column selector is required", call. = FALSE)
}

if (is.null(opt$out)) {
  print_help(opt_parser)
  stop("Output file is required", call. = FALSE)
}

file_to_divide <- readr::read_csv(opt$file)

results <- data.frame(matrix(ncol = 14, nrow = 0))

for (chunk in 1:120) {
  num_users <- chunk * 25

  chunk_subset <- subset(file_to_divide, grpThreads == num_users)

  selector <- chunk_subset[[opt$selector]]

  num_requests = nrow(chunk_subset)
  max_val = max(selector)
  min_val = min(selector)
  avg_val = mean(selector)
  median_val = median(selector)
  percentiles = quantile(selector, c(.60, .80, .90, .98))
  std_dev_val = sd(selector)

  chunk_duration_in_seconds = 6 # JMeter scenario was bumping users by 25 every 6 seconds
  throughput_val = num_requests / chunk_duration_in_seconds
  bandwidth_in_bytes = sum(chunk_subset$bytes)

  df <- data.frame(
    chunk,
    num_users,
    num_requests,
    throughput_val,
    bandwidth_in_bytes,
    max_val,
    min_val,
    avg_val,
    median_val,
    std_dev_val,
    percentiles[1],
    percentiles[2],
    percentiles[3],
    percentiles[4])

  colnames(df) <- c(
    "chunk",
    "num_users",
    "num_requests",
    "throughput",
    "bandwidth_in_bytes",
    "max",
    "min",
    "avg",
    "median",
    "std_dev",
    "60th percentile",
    "80th percentile",
    "90th percentile",
    "98th percentile"
  )

  results <- rbind(results, df)
}


readr::write_csv(results, opt$out, append = TRUE, col_names = TRUE)











