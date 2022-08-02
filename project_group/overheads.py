from pathlib import Path
import csv
file_path = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"

def ov() :
    overheads = []

    if file_path.exists():
        with file_path.open(mode = "r",encoding = 'ascii', errors = 'ignore', newline='') as open:
            all = csv.reader(open)
            next(all)
            for items in all:
                overheads.append({items[0] : float(items[1])})

    # print(overheads)
    allov = []

    for lists in overheads:
        for category, ov in lists.items():
            allov.append(ov)
            highest = [max(allov)]
            if ov in highest:
                print(category, ov)

ov()