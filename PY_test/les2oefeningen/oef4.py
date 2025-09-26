if __name__ == "__main__":
    day = input("Enter a day: ").lower()  # convert input to lowercase to match cases
    match day:
        case "monday":
            print("1")
        case "tuesday":
            print("2")
        case "wednesday":
            print("3")
        case "thursday":
            print("4")
        case "friday":
            print("5")
        case "saturday":
            print("6")
        case "sunday":
            print("7")
        case _:  # default case if input doesn't match any day
            print("Invalid day")

