from pathlib import Path
import api
<<<<<<< HEAD
import overheads
import profit_loss
=======
>>>>>>> 472064dbfa444c5c060e581ddeab2fdc15481200

file_path= Path.cwd()/"project_group"/"csv_reports"/"summary_report.txt"
file_path.touch()

with file_path.open(mode = "w") as file:
<<<<<<< HEAD
    file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}")
    file.writelines(f"\n{overheads.lists}")



=======
    file.writelines(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}')
>>>>>>> 472064dbfa444c5c060e581ddeab2fdc15481200
