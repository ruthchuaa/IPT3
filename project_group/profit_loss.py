from pathlib import Path
import csv
file_path = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"

netprofit = []
allprofits = []

if file_path.exists():
   with file_path.open(mode = "r",encoding = 'ascii', errors = 'ignore', newline='') as open:
    profits = csv.reader(open)
    next(profits)
    
    for lines in profits:
        netprofit.append(int(lines[4]))
        allprofits.append({lines[0]: int(lines[4])})
    
deficit = []

for index, value in enumerate(netprofit):
    if value > netprofit[0]:
        diff = netprofit[index] - netprofit[index-1]
        if diff < 0 :
            deficit.append(value)


for items in allprofits:
    for days, number in items.items() :
        if number in deficit :
             print(days)
        