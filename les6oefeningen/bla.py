def print_name(name):
    print(f'Welcome, {name}')
    for i in range(len(name)):
        print("-", end="")

    aa=0
    while aa < len(name):
        print(name[0:aa])
        aa+=1





if __name__ == '__main__':
    name = input("name")
    print_name(name)

    print()

