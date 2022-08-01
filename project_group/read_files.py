from pathlib import Path
import csv


cashonhand = []
def csvread(csvfile, list):
    
    allfilepath = Path.cwd()/"project_group"/"csv_reports"
    newpath = allfilepath/csvfile
    with newpath.open(mode = "r",encoding = "UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) 
        for line in reader:
            list.append(line)

        


csvread('Cash on Hand.csv', cashonhand)
print(cashonhand)




