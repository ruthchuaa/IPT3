from pathlib import Path
from read_files import csvread
import api
#
def profitloss():
    '''
    - Returns whether Profit is consecutively higher each day
    - If Profit has deficit, function will highlight the day where profit is lower than the previous day and the difference
    '''
    try :
        # Create an empty list for all line from Profits and Loss.csv
        # and another one for all values with the day
        # and anotherone for only values from the different days
        
        alldata = []
        netprofit = []
        allprofits = []
        
        #Read Profits and loss file and append line to alldata list
        readfiles = csvread('Profits and loss.csv', alldata)

        #From alldata list, append only the values to netprofit list
        # and append all values with the respective days to allprofits list 
        for lines in alldata:
            netprofit.append(int(lines[4]))
            allprofits.append({lines[0]: int(lines[4])})
            
        #Create an empty list for the values of days with deficit and the cash on hand on that day
        deficit = []

        for index, value in enumerate(netprofit):
            if value > netprofit[0]:
                #Find the difference between the values 
                diff = netprofit[index] - netprofit[index-1]
                # If difference between values is negative, append values and difference to deficit list
                if diff < 0 :
                    deficit.append([value, diff])

        #Create an empty list for days with cash deficit and amount of cash deficit
        list = []
        for items in allprofits:
            for days, number in items.items():
                for one, two in deficit:
                    if number == one:
                        amt = abs(two)
                        # if values appear in deficit, append cash deficit day and converted amount from USD to SGD to list
                        re = (f'[PROFIT DEFICIT] DAY : {days}, AMOUNT : SGD{amt}') #api.convert(amt):.2f
                        list.append(re)

        if list == []:
            return(f'[PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY')
        else :
            return(list)
    except Exception as e:
        return('Error')










                        


