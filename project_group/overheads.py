from pathlib import Path
import csv

<<<<<<< HEAD
def overheads():
    file_path = Path.cwd()/"project_group"/"csv_reports"/"Overheads.csv"

    overheads = []

    if file_path.exists():
        with file_path.open(mode = "r",encoding = 'ascii', errors = 'ignore', newline='') as open:
            all = csv.reader(open)
            next(all)
        
            for items in all:
                overheads.append({items[0] : float(items[1])})

    # print(overheads)
    allov = []


=======
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

>>>>>>> 472064dbfa444c5c060e581ddeab2fdc15481200
    for lists in overheads:
        for category, ov in lists.items():
            allov.append(ov)
            highest = [max(allov)]
            if ov in highest:
<<<<<<< HEAD
                print(f"[HIGHEST OVERHEADS] {category.upper(), ov}")

overheads()

                
=======
                print(category, ov)

ov()
>>>>>>> 472064dbfa444c5c060e581ddeab2fdc15481200
