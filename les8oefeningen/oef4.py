from textwrap import indent


def get_all():
    data = []
    with open('oefdata/sponsors.txt') as file:
        for line in file:
            line = line.strip()
            if line:
                records = line.split("*")
                data.append(records)
    return data

def findin(a,b):
    for i in a:
        if i[0] == int(b[0]):
            return True
    return False

if __name__ == '__main__':
    a = get_all()
    grouped_users = []

    for i in a:
        bol = findin(grouped_users, i)
        if not bol:
            grouped_users.append([int(i[0]),i[1],i[2],int(i[3])])
        else:
            for j in grouped_users:
                if int(i[0]) == j[0]:
                    j[3] += int(i[3])



    print("Overview gifts")
    print("number","sponsor",sep="     ")
    grouped_users.sort()
    for i in grouped_users:
        print(i[0],i[1],i[2],i[3])



