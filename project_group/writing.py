from pathlib import Path
import api

file_path= Path.cwd()/"project_group"/"csv_reports"/"summary_report.txt"
file_path.touch()

with file_path.open(mode = "w") as file:
    file.writelines(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}')