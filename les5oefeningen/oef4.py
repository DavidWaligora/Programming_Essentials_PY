some_numberstostart = (3, 2, 5, 77, 8, 5647, 7, 6, 56, 34)

if __name__ == '__main__':
    print(some_numberstostart)
    print("changing the tuple")

    try:
        blabla = some_numberstostart.index(4)
        print(f"Found 4 at index {blabla}")
        new_tuplenumbers = some_numberstostart[blabla:]
        print(new_tuplenumbers)
    except ValueError:
        print("No number 4 found in the tuple")
