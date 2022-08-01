from pathlib import Path
import csv
file_path = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"

netCOH = []
allCOH = []

if file_path.exists():
   with file_path.open(mode = "r",encoding = 'ascii', errors = 'ignore', newline='') as open:
    cash = csv.reader(open)
    next(cash)
    
    for lines in cash:
        netCOH.append(int(lines[1]))
        allCOH.append({lines[0]: int(lines[1])})
    
deficit = []

for index, value in enumerate(netCOH):
    if value > netCOH[0]:
        diff = netCOH[index] - netCOH[index-1]
        if diff < 0 :
            deficit.append(value)



print(allCOH)
print(deficit)


for items in allCOH:
    for days, number in items.items() :
        if number in deficit :
             print(days)
        

        else:
            print("No cash deficit found")
        



        