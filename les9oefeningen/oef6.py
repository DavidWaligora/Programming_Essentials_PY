

if __name__ == '__main__':
    listofusers = {}
    with open('Files Chapter 9/tasks.csv') as file:
        header = file.readline()
        line = file.readline().rstrip()

        while line:
            records = line.split(";")
            for i in records[1:6]:
                if i not in listofusers:
                    listofusers[i] = 1
                else:
                    listofusers[i] += 1

            line = file.readline().rstrip()


        print("task distribution:")
        for value in listofusers:
            print(value, listofusers[value])






