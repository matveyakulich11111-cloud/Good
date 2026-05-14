from random import randint
def print_name(name):
    print(f'Hello {name}')
    
names = ['Vasa', 'Petya', 'Kolya', 'Tola', 'Ola']


def make_marx(num_el, num_row):
    matrix = []
    for row in range(num_row):
        row = []
        for el in range(num_el):
            row.append(randint(1,10))
        matrix.append(row)
    return matrix

