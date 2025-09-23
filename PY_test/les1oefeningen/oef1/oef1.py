class PersonalData:
    def __init__(self, surname, lastname, street, number, zipcode, city):
        self.surname = surname
        self.lastname = lastname
        self.street = street
        self.number = number
        self.zipcode = zipcode
        self.city = city

    def print_address_label(self):
        print(f"{str(self.surname)} {str(self.lastname)}")
        print(f"{str(self.street)} {str(self.number)}")
        print(f"{str(self.zipcode)} {str(self.city)}")


def get_personal_data():
    surname = int(input("Enter surname: "))
    lastname = str(input("Enter lastname: "))
    street = str(input("Enter street: "))
    number = int(input("Enter house number: "))
    zipcode = str(input("Enter zipcode: "))
    city = str(input("Enter city: "))

    return PersonalData(surname, lastname, street, number, zipcode, city)


if __name__ == "__main__":
    personal_data = get_personal_data()
    personal_data.print_address_label()
