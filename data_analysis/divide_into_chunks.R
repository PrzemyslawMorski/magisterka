#!/usr/bin/env Rscript
library("optparse")
library("readr")
 
option_list = list(
  make_option(c("-f", "--file"), type="character", default=NULL, 
              help="input file name", metavar="character"),
  make_option(c("-s", "--selector"), type="character", default=NULL, 
              help="selected field", metavar="character"),
	make_option(c("-o", "--out"), type="character", default="out.txt", 
              help="output file name [default= %default]", metavar="character")
); 
 
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

print(opt$file)
print(opt$out)
print(opt$selector)

function_field_selector <- function(arg1) {
  arg1.loc(opt$selector)
}


file <- file.choose()
file_to_divide <- readr::read_csv(file)

results <- data.frame(matrix(ncol = 10, nrow = 0))

for (chunk in 1:120) {
  num_users <- chunk * 25
  
  chunk_subset <- subset(file_to_divide, grpThreads == num_users)
  
  selector <- function_field_selector(chunk_subset)
  
  max_val = max(selector)
  min_val = min(selector)
  avg_val = mean(selector)
  median_val = median(selector)
  percentiles = quantile(selector, c(.60, .80, .90, .98))
  std_dev_val = sd(selector)
  
  df <- data.frame(
    chunk, 
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


readr::write_csv(results, output_file_name, append=TRUE, col_names = TRUE)











