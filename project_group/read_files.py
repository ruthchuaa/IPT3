from pathlib import Path
import csv
file_path = Path.cwd()/"project_group"/"csv_reports"

cashonhand = []
def csvread(path, csvfile, list):
    newpath = path/csvfile
    with newpath.open(mode = "r",encoding = "UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) 
        for line in reader:
            list.append(line)

        


csvread(file_path, 'Cash on Hand.csv', cashonhand)
print(cashonhand)




