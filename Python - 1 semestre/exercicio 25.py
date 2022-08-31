import csv
data_list = [["ID", "Name", "Area"],
             [123887, "Linus Snow", "Linux"],
             [290454, "Tim Lee", "CSS/JAVA"],
             [303745, "Guido Rossum", "Python"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)
    