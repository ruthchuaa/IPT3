# #Profit & Loss csv : The program will compute the
# difference in the net profit between each day. If
# the net profit is not consecutively higher each
# day, the program will highlight the day where net
# profit is lower than the previous day and the value
# difference

from pathlib import Path
import csv
file_path = Path.cwd()/"project_group"/"csv_reports"/"Profits and Loss.csv"

netprofit = []
if file_path.exists():
   with file_path.open(mode = "r",encoding = 'ascii', errors = 'ignore', newline='') as open:
    profits = csv.reader(open)
    next(profits)

   
    for lines in profits:
        netprofit.append(int(lines[4]))

print(netprofit)

for index, value in enumerate(netprofit):
    if value > netprofit[0]:
        diff = netprofit[index] - netprofit[index-1]
        print(diff)
        


        