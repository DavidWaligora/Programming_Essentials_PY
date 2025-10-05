#Write a program that reads a 3-digit number and prints the
#following information.
#Do not use string functions to find the separate digits.
from traceback import print_last


class three_digit_numbers:
    def __init__(self, number):
        if not (100 <= number <= 999):
            raise ValueError("Number must be a 3-digit integer")
        self.number = number

    def print_all_shit(self):
        print("half = " + str(self.number/2))
        print("Double = " + str(self.number*2))
        print("Third power = " + str(self.number**3))
        print("Tenfold = " + str(self.number * 10))
        print("The digits are: ")
        for digit in str(self.number):
            print(digit)



if __name__ == "__main__":
    three_digit_numbers(int(input("Enter a 3-digit number: "))).print_all_shit()