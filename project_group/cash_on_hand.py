from pathlib import Path
from read_files import csvread

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


    for items in allCOH:
        for days, number in items.items():
            for one, two in deficit:
                if number == one:
                    print(two)
    else:
        print(f"[CASH SURPLUS] CASH ON HAND EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

cash_on_hand()