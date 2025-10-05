#With this program you can calculate the product of a number of numbers. The program continues
#to ask the user for whole numbers until they enter a 0 (zero).class PersonData

#Extend your exercise and print also how many numbers were entered.

if __name__ == "__main__":
    nummer = None
    result = int(1)
    numbers_entered = int()
    while nummer != 0:
        nummer = int(input("Enter number, stop by entering a zero: "))
        if nummer != 0:
            result *= nummer
            numbers_entered += 1

    print(f"The product of the {numbers_entered} numbers is {result}")