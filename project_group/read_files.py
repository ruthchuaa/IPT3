from pathlib import Path
import csv

# Create a function to read .csv files
def csvread(csvfile, list):
    """
    - 2 required parameters: file name.csv, empty list 
    - Reads data from .csv files from the "csv_reports" folder
    """
    
    allfilepath = Path.cwd()/"project_group"/"csv_reports"
    newpath = allfilepath/csvfile

    #
    with newpath.open(mode = "r",encoding = 'ascii', errors = 'ignore', newline='') as file:
        reader = csv.reader(file)

        # Skips reading the first line of the .csv files since the first line is the headers for the data
        next(reader) 

        # Read data from .csv files by appending them into a list
        for line in reader:
            list.append(line)