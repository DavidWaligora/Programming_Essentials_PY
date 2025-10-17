'For this exercise you use the file first_names.txt.'

def print_if_z(line):
    if (check_z(line)):
        print(line)
        return True
    return False

def check_z(line):
    for i in line:
        if i.lower() == 'z':
            return  True
    return False

if __name__ == "__main__":
    with open('Files Chapter 7/first_names.txt') as file:
        amount = 0
        amount_z = 0
        line = file.readline()
        while line:
            if line !='\n':
                amount += 1
                if print_if_z(line):
                    amount_z += 1
            line = file.readline().strip()
        print(f'There are {amount} first names in the file.')
        print(f'{amount_z} of which contain a letter z')


