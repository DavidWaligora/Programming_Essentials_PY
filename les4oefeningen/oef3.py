def main():
    word = input("Enter a word: ")
    length = len(word)
    middle = int(length / 2)
    print(word[middle -1: middle + 2])


if __name__ == "__main__":
    main()
