
def bool_containsinlist(blabla, blablalist):
    for j in blablalist:
        if j[0] == blabla[0]:
            return True
    return False

if __name__ == "__main__":

    with open('oefdata/courses.csv')as file:
        userlist = []

        line = file.readline().rstrip()
        while line:
            userlist.append(line.split(';'))
            line = file.readline().rstrip()

        userlist.remove(userlist[0])

        resultlist = []
        for i in userlist:
            if not bool_containsinlist(i, resultlist):
                resultlist.append(i)

        for bla in resultlist:
            print(bla)

