if __name__ == "__main__":
    number = int(input("Enter a number: "))
    for foo in range(number, -1, -1):
        if foo != 0:
            print(str(foo) + " ... ", end=" ")
        else:
            print(foo)


