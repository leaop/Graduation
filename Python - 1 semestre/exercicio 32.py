print('If you want know the multiplication table of any number, I can show you')
number=int(input('try a number: '))
class Table:
    def table(number):
        multi_table = []
        cont = 1
        while cont < 11:
            multi_table.append(number * cont)
            cont += 1
        return multi_table
X = Table.table(number)
print(f"the multiplication table is:{X}")