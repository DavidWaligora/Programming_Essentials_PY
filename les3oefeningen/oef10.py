smaller_than_12 = 20
between_12_18 = 50
older_than_18 = 95

class Member:
    def __init__(self, name, age, amount_years):
        self.name = name
        self.age = age
        self.amount_years = amount_years

    def member_fee_calculator(self):
        amount: float = 0

        if self.age <= 12:
            amount = smaller_than_12

        if 12 < self.age <= 18:
            amount = between_12_18
        if self.age > 18:
            amount = older_than_18


        if self.amount_years >= 5:
            amount = amount - (amount /100) *10

        return amount

    def foo(self):
        print("Information for member 1")
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("Member for how many years: " + str(self.amount_years))
        print(f"Member fee for {self.name} = {str(self.member_fee_calculator())}")

def main():
    member = Member("Alice", 25, 3)
    member.foo()



if __name__ == "__main__":
    main()
