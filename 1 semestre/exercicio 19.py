import csv
with open('./exercicio18.csv', 'w') as csvfile:
    csv.writer(csvfile, delimiter=',').writerow(['Joao', '21', '1,70', 'solteiro'])
    csv.writer(csvfile, delimiter=',').writerow(['Pedro', '22', '1,79', 'solteiro'])
    csv.writer(csvfile, delimiter=',').writerow(['Henrique', '23', '1,81', 'solteiro'])
    csv.writer(csvfile, delimiter=',').writerow(['Zé', '24', '1,84', 'solteiro'])
    csv.writer(csvfile, delimiter=',').writerow(['Maria', '25', '1,67', 'solteiro'])

    

