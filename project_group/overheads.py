
from pathlib import Path
import api
import read_files

def overheads():
    '''
    - Returns the highest Overhead category and its value in SGD
    '''
    try:
        # Create empty list to append all lines from Overheads.csv 
        # and another empty list for all values with the different categories
        overhead = []
        alldata = []


        file_path = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"
        # Read file from Overheads.csv and append it to alldata list
        readfile = read_files.csvread('Overheads.csv', alldata)
        
        #from alldata, append {Category : Value} to a dictionary for each category
        # so that we can call Categories of values easily later 
        for items in alldata:
            overhead.append({items[0] : float(items[1])})

        # Create empty list for only Values
        allov = []

        #Append Values from the dictionaries in overhead to allov empty list
        for lists in overhead:
            
            #find the highest value 
            for category, ov in lists.items():
                allov.append(ov)
                highest = [max(allov)]
                # Return highest value along with their Category 
                # and convert highest value from USD to SGD using convert function from api file
                if ov in highest:
                    return (f"[HIGHEST OVERHEADS] {category.upper()}: SGD{api.convert(ov):.2f}")
    except Exception as e:
        return('Error')



                