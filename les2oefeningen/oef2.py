import datetime

if __name__ == "__main__":
    year_birth = int(input("Enter year birth: "))
    age = datetime.date.today().year - year_birth
    print(
        "Your age = " + str(age) + "\n" +
        "You're " + ("an" if age > 18 else "not an") + " adult"
    )