if __name__ == "__main__":
    file = open("Files Chapter 7/first_names.txt")
    print(file.read())
    file.close()
    file = open("Files Chapter 7/first_names.txt")
    reversed_list = list()
    line = file.readline().strip()
    while line:
        if line != '\n':
            reversed_list.append(line)
        line = file.readline().strip()
    file.close()

    print ('------------------')
    reversed_list.reverse()
    for i in reversed_list:
        print(i)

