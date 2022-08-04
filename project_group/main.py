from pathlib import Path
import api
import overheads
import cash_on_hand
import profit_loss

# create 'summary_report' text file in IPT3 file
file_path= Path.cwd()/"project_group"/"csv_reports"/"summary_report.txt"
file_path.touch()

# check if 'summary_report.txt' is created
print(file_path.exists())


with file_path.open(mode = "w") as file:
    # write the real time currency conversion rate using data from 'api.py' file into 'summary_report.txt'
    file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.all}")

    # write data from 'overheads.py' file into 'summary_report.txt'
    file.writelines(f"\n{overheads.overheads()}")
    
    # write the following string into 'summary_report.txt' if there is no data found in the 'cash_on_hand.py' file
    if cash_on_hand.cash_on_hand() == [] :
        file.writelines(f'\n[CASH SURPLUS] CASH ON HAND ON EACH DAY IS HIGHER THAN PREVIOUS DAY')
    else :
        # write data from 'cash_on_hand.py' file into 'summary_report.txt'
        for num, val in enumerate(cash_on_hand.cash_on_hand()):
            file.writelines(f"\n{cash_on_hand.cash_on_hand()[num]}")

    # write the following string into 'summary_report.txt' if there is no data found in the 'profit_loss.py' file 
    if profit_loss.profitloss() == [] :
        file.writelines(f'[PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY')
    else :
        # write data from 'profit_loss.py' file into 'summary_report.txt'
        for num, val in enumerate(profit_loss.profitloss()):
            file.writelines(f"\n{profit_loss.profitloss()[num]}")
