import csv
with open('innovators.csv', 'r', encoding='UTF8', newline='') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        print(row)
    