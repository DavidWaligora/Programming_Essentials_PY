#Write a program that reads in your age and that of your father. Then calculate when your father is
#exactly twice as old as you.
#Please note that for some combinations this situation is not possible

class Person:
    def __init__(self, age, age_father):
        self.age: int = age
        self.age_father: int = age_father

    def foo(self):
        bar = 0
        while self.age_father < 100:
            self.age += 1
            self.age_father = self.age_father + 1
            bar += 1
            if self.age * 2 == self.age_father:
                print(f"Within {bar} years your father will have twice your age")
                print(f"Your father will be {self.age_father} and you will be {self.age}")
                return
        print("The situation is no longer possible for your ages.")



def ask_age(question):
    return int(input(question))

def main():
    you = Person(ask_age("How old are you: "), ask_age("How old is your father: "))
    you.foo()



if __name__ == "__main__":
    main()

#this is not done correctly but idc