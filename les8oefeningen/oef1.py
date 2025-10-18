def orderlist(listofstudents):
    result = listofstudents
    result.sort(key=lambda item: item[2])
    return result





if __name__ == "__main__":

    with open('oefdata/classrooms.txt') as file:
        list_of_students = []
        line = file.readline().rstrip()
        while line:
            record = line.split(';')
            list_of_students.append(record)
            line = file.readline().rstrip()

        ordered_list = orderlist(list_of_students)
        indicator = ordered_list[0][2]
        amount = 0
        print(indicator)
        for i in ordered_list:
            if i[2] == indicator:
                print(i[0],i[1])
                amount +=1
            else:
                print(f"Number of students in classroom = {indicator} {amount -1}")
                indicator=i[2]
                print(indicator)
                print(i[0], i[1])
                amount = 1
        print(f"Number of students in classroom = {indicator} {amount - 1}")
