

if __name__ == '__main__':
    text = input("Enter some text: ").replace(" ", "")
    ronfz = list()
    for word in text:
        ronfz.append(word)

    print(ronfz)
    for word in ronfz:
        print(word, end=" ")

    print()

    for i in ronfz:
        print(i + "\t", end="")
