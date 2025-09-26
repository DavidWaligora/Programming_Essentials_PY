class Difference:
    def __init__(self, smallest, largest):
        self.smallest = smallest
        self.largest = largest

    def print_difference(self):
        print(f"The difference between the largest number 44 and the largest {self.largest} and smallest {self.smallest} is: {self.largest - self.smallest}")


def main():
    foo = Difference(1, 1)
    bar = 1
    while bar != 0:
        bar = int(input("Enter a number: "))
        if bar != 0:
            if foo.smallest > bar:
                foo.smallest = bar
            if foo.largest < bar:
                foo.largest = bar

    foo.print_difference()


if __name__ == "__main__":
    main()
