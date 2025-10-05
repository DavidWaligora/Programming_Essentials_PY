def print_menu():
    print("menu:\n"+
          "*****\n" +
          "U Uppercase\n" +
          "L Lowercase\n" +
          "A Alternative\n"
          )

if __name__ == "__main__":
    name = input("Enter your name: ")
    print_menu()
    choice = input("Make a choice (U,A,L): ").lower()

    while choice != "":
        if choice == "u":
            print(name.upper())
        if choice == "l":
            print(name.lower())
        if choice == "a":
            print("notimplemented")

