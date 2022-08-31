import csv

with open('18.csv') as f:

    DictReader_obj = csv.DictReader(f)

    for item in DictReader_obj:

        print(dict(item))