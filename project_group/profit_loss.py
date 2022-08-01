
from pathlib import Path
import csv

from read_files import csvread

netprofit = []
allprofits = []
alldata = []

readfiles = csvread('Profits and loss.csv', alldata)

for lines in alldata:
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
        