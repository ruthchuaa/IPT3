from pathlib import Path
from read_files import csvread

def test():
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
                deficit.append([value, diff])


    for items in allprofits:
        for days, number in items.items():
            for one, two in deficit:
                if number == one:
                    print(two)

