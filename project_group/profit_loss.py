from pathlib import Path
from read_files import csvread
import api
#
def profitloss():
<<<<<<< HEAD
    try :
        netprofit = []
        allprofits = []
        alldata = []

        readfiles = csvread('Profits and loss.csv', alldata)
=======
    netprofit = []
    allprofits = []
    alldata = []
##
    readfiles = csvread('Profits and loss.csv', alldata)
>>>>>>> 62855a96c4f9aa2fe2a0af85ceac84d491e7d9cb

        for lines in alldata:
            netprofit.append(int(lines[4]))
            allprofits.append({lines[0]: int(lines[4])})
            
        deficit = []

        for index, value in enumerate(netprofit):
            if value > netprofit[0]:
                diff = netprofit[index] - netprofit[index-1]
                if diff < 0 :
                    deficit.append([value, diff])

<<<<<<< HEAD
        list = []
        for items in allprofits:
            for days, number in items.items():
                for one, two in deficit:
                    if number == one:
                        amt = abs(two)
                        re = (f'[PROFIT DEFICIT] DAY : {days}, AMOUNT : SGD{amt}') #api.convert(amt):.2f
                        list.append(re)

        if list == []:
            return(f'[PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY')
        else :
            return(list)
    except Exception as e:
        return('Error')
=======
    list = []
    for items in allprofits:
        for days, number in items.items():
            for one, two in deficit:
                if number == one:
                    amt = abs(two)
                    re = (f'[PROFIT DEFICIT] DAY : {days}, AMOUNT : SGD{api.convert(amt):.2f}')
                    list.append(re)
#
    if list == []:
        return(f'[PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY')
    else :
        return(list)
>>>>>>> 62855a96c4f9aa2fe2a0af85ceac84d491e7d9cb










                        


