import csv
f = open('./18.csv', 'w')
writer = csv.writer(f)
writer.writerow(['a', 'b', 'c', 'd'])
writer.writerow(['d', 'e', 'g', 'h'])
writer.writerow(['i', 'j', 'k', 'l'])
writer.writerow(['m', 'n', 'o', 'p'])
writer.writerow(['q', 'r', 's', 't'])
f.close()
