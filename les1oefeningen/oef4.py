#Write a program to read 2 names and then change places in memory and print them again.

if __name__ == "__main__":
    first = str(input("Enter first name: "))
    last = str(input("Enter last name: "))
    print("before changing: "+first, last)
    change = first
    first = last
    last = change
    print("after changing: "+first, last)
