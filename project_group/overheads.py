from os import read
from pathlib import Path
import csv
import api
import read_files
#
def overheads():
    file_path = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"

    overhead = []
    alldata = []

    readfile = read_files.csvread('Overheads.csv', alldata)
        
    for items in alldata:
        overhead.append({items[0] : float(items[1])})

    # print(overheads)
    allov = []

#
    for lists in overhead:
        for category, ov in lists.items():
            allov.append(ov)
            highest = [max(allov)]
            if ov in highest:
                return (f"[HIGHEST OVERHEADS] {category.upper()}: SGD{api.convert(ov):.2f}")



                