import csv
with open("house.csv", "r") as file:
#just read = 'r''
#write (modify) = 'w'
#get file and input in the variable arquivo
    file_csv = csv.reader(file, delimiter = ",")
#treatment the file with csv package
    for i, row in enumerate(file_csv):
#traversing the lines
#for i, row in enumerate(file_csv): - we can get the line and the index
#for row in file_csv: - just get the row
        if i == 0:
            print("head:" + str(row))
        else:
            print("value:" + str(row))