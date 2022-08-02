from pathlib import Path
import api
import profit_loss

file_path= Path.cwd()/"project_group"/"csv_reports"/"summary_report.txt"
file_path.touch()
print(file_path.exists())

# list= [f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}"]
with file_path.open(mode="a") as file:

    file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}")



