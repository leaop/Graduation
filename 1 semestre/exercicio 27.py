import csv

meu_dict = {
    "jan": "1:3",
    "fev": "2:27",
    "mar": "3:4",
    "abr": "4:4",
    "mai": "5:3",
    "jun": "6:4"
}

with open("mess.csv", 'w', encoding='UTF8', newline='') as new:
    writer = csv.writer(new)
    for key, value in meu_dict.items():
        writer.writerow([key, value])