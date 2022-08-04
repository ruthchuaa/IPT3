from pathlib import Path
from read_files import csvread
import api

def cash_on_hand():
    '''
    - Returns whether Cash on hand is consecutively higher each day
    - If cash on hand has deficit, function will highlight the day where cash on hand is lower than the previous day and the difference
    '''
    try:
        # Create an empty list for all line from Cash on Hand.csv
        # and another one for all values with the day
        # and anotherone for only values from the different days
        alldata = []
        allCOH = []
        netCOH = []

        #Read files and append lines to alldata list
        readfiles = csvread('Cash on Hand.csv', alldata)
        
        #From alldata list, append only the values to netCOH list
        # and append all values with the respective days to allCOH list 
        for lines in alldata:
            netCOH.append(int(lines[1]))
            allCOH.append({lines[0]: int(lines[1])})
        
        #Create an empty list for the values of days with deficit and the cash on hand on that day 
        deficit = []
        
        
        for index, value in enumerate(netCOH):
            if value > netCOH[0]:
                #Find the difference between the values 
                diff = netCOH[index] - netCOH[index-1]

                # If difference between values is negative, append values and difference to deficit list
                if diff < 0 :
                    deficit.append([value, diff])

        #Create an empty list for days with cash deficit and amount of cash deficit
        list =[]

        
        for items in allCOH:
            for days, number in items.items():
                for one, two in deficit:
                    # if values appear in deficit, append cash deficit day and amount to list
                    if number == one:
                        amt = abs(two)
                        re = (f'[CASH DEFICIT] DAY : {days}, AMOUNT : SGD{api.convert(amt):.2f}')
                        list.append(re)
                     
        return(list)
    except Exception as e:
        return ('Error')




    
