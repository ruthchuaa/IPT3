from pathlib import Path
import api
import overheads
import cash_on_hand
import profit_loss

file_path= Path.cwd()/"project_group"/"csv_reports"/"summary_report.txt"
file_path.touch()
print(file_path.exists())

# list= [f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}"]
with file_path.open(mode = "w") as file:
    file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}")
    file.writelines(f"\n{overheads.overheads()}")
    file.writelines(f"\n{cash_on_hand.cash_on_hand()}")
    file.writelines(f"\n{profit_loss.profitloss()}")