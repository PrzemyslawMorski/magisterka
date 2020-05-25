set root_dir="."
set file_name=%root_dir%"\summary.csv"

Rscript .\divide_into_chunks.R -s "elapsed" -o %root_dir%"\elapsed_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "Latency" -o %root_dir%"\latency_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "ErrorCount" -o %root_dir%"\error_count_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "Connect" -o %root_dir%"\connect_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "IdleTime" -o %root_dir%"\idle_time_output.csv" -f %file_name%