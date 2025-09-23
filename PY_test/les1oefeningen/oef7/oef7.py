#Write a program to generate the next output. The number 15 is fixed. The other numbers should be
#calculated by using operators += -= *= etc. So use only 1 variable


if __name__ == "__main__":
    number = int(input("Enter starting number: "))
    print(number)

    number *= 10
    print(number)

    number += 5
    print(number)

    number -= 7
    print(number)

    number += 1
    print(number)

    number *= 100
    print(number)

    number -= 7450
    print(number)

