import csv
f = open('./temp.csv', 'w')
writer = csv.writer(f)
writer.writerow(['name', 'score', 'score1', 'rank'])
writer.writerow(['Joao', '12', '1', '23'])
writer.writerow(['Pedro', '13', '2', '114'])
writer.writerow(['Maria', '14', '2', '10'])
writer.writerow(['Francisco', '15', '3', '56'])
f.close()

class Student:

    def __init__(self, name, score, rank):
        self.name = name
        self.score = score
        self.rank = rank


student_list = []

with open('temp.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None)  # Skip the header.
    # Unpack the row directly in the head of the for loop.
    for name, score1, score2, rank in reader:
        # Convert the numbers to floats.
        score1 = float(score1)
        score2 = float(score2)
        rank = float(rank)
        # Now create the Student instance and append it to the list.
        student_list.append(Student(name, (score1, score2), rank))