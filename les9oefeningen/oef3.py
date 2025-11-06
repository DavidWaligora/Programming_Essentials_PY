def getset():
    classrooms = {}
    with open('Files Chapter 9/local_booking.txt') as file:
        for i in file:
            if i:
                line = i.rstrip()
                record = line.split(";")
                if record[3] not in classrooms:
                    classrooms[record[3]] = record[3]

    return classrooms

if __name__ == '__main__':
    resultset = getset()
    print("Classrooms")
    for i in resultset:
        print(i)

