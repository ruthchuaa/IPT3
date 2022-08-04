from pathlib import Path
from read_files import csvread
import api
#
def cash_on_hand():
    netCOH = []
    allCOH = []
    alldata = []

    readfiles = csvread('Cash on Hand.csv', alldata)

    for lines in alldata:
        netCOH.append(int(lines[1]))
        allCOH.append({lines[0]: int(lines[1])})
        
    deficit = []

    for index, value in enumerate(netCOH):
        if value > netCOH[0]:
            diff = netCOH[index] - netCOH[index-1]
            if diff < 0 :
                deficit.append([value, diff])
        
    list =[]

    for items in allCOH:
        for days, number in items.items():
            for one, two in deficit:
                if number == one:
                    amt = abs(two)
                    re = (f'[CASH DEFICIT] DAY : {days}, AMOUNT : SGD{api.convert(amt):.2f}')
                    list.append(re)
                    
    return(list)




    
