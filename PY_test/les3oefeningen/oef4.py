import random
def enter_higher_number():
    number = random.randint(1, 20)
    amount = 0
    choice = 0
    while choice != number:
        choice = int(input("Enter a positive number: "))
        if choice < number:
            print("Higher!")
        elif choice > number:
            print("Lower!")
        choice +=1

    print(f"You have guessed the number! {number} in {amount} tries.")



if __name__ == '__main__':
    enter_higher_number()
