set file_name="C:\Users\pmorski\Desktop\Wyniki testow\podman fibb 30\summary.csv"

Rscript .\divide_into_chunks.R -s "elapsed" -o ".\elapsed_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "Latency" -o ".\latency_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "ErrorCount" -o ".\error_count_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "Connect" -o ".\connect_output.csv" -f %file_name%
Rscript .\divide_into_chunks.R -s "IdleTime" -o ".\idle_time_output.csv" -f %file_name%