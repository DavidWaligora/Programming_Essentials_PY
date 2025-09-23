#Write a program that allows a user to know what time his alarm will go off when he indicates what
#time it is (only the hour is entered) and how long he wants to wait.

if __name__ == "__main__":
    current_hour = int(input("Enter current hour: "))
    wait_hours = int(input("How long do you want to wait: "))

    alarm_hour = (current_hour + wait_hours) % 24

    print("The alarm will go off at " + str(alarm_hour) + "h.")