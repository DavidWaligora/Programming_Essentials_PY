
if __name__ == '__main__':
    students = list()
    input_result = str()

    while input_result != 'stop':
        result = list()

        input_result = input("Enter your name: ")
        if input_result != 'stop':
            result.append(input_result)

            input_result = input("Enter your age: ")
            if input_result != 'stop':
                result.append(float(input_result))

        if input_result != 'stop':
            students.append(result)

    print("The students are: " + str(students))
    print("Overview")
    for std in students:
        print(std[0],'\t', std[1])

    the_max = students[0]  # assume the first student is the oldest
    for std in students:
        if std[1] > the_max[1]:  # compare ages
            the_max = std
    print("The maximum score is: " + the_max[0], str(the_max[1]))
    # Average age
    total_age = 0
    for std in students:
        total_age += std[1]
    average_age = total_age / len(students)
    print("The average age is: " + str(average_age))
