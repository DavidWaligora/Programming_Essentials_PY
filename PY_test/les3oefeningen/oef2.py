

def main():
    numbers_entered = int(input("Enter a number: "))
    zeros = 0
    sixes = 0
    for i in str(numbers_entered):
        if i == "0":
            zeros += 1
        if i == "6":
            sixes += 1

    print(f"The number consists of {zeros} zeros and {sixes} sixes")


if __name__ == "__main__":
    main()
