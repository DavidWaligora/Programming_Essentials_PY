import csv


def bool_containsinlist(blabla, blablalist):
    for j in blablalist:
        if j[4] == blabla[4] and j[5] == blabla[5]:
            return True
    return False

if __name__ == "__main__":

    with open('oefdata/courses.csv')as file:
        userlist = []

        line = file.readline().rstrip()
        while line:
            userlist.append(line.split(';'))
            line = file.readline().rstrip()

        header = userlist[0]
        userlist.remove(userlist[0])

        resultlist = []
        for i in userlist:
            if not bool_containsinlist(i, resultlist):
                resultlist.append(i)

        for bla in resultlist:
            print(bla)

        resultlist.insert(0, header)
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for i in resultlist:
                writer.writerow([i[3], i[4], i[5]])
