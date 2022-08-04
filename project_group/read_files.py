from pathlib import Path
import csv


def csvread(csvfile, list):
    
    allfilepath = Path.cwd()/"project_group"/"csv_reports"
    newpath = allfilepath/csvfile
    with newpath.open(mode = "r",encoding = 'ascii', errors = 'ignore', newline='') as file:
        reader = csv.reader(file)
        next(reader) 
        for line in reader:
            list.append(line)