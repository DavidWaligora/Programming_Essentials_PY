if __name__ == '__main__':
    color = str(input("What is your favorite color? "))
    print(str(color), "consists of ", str(len(color)), "letters")

    for i in range(len(color)):
        print(color[i], ord(color[i]))

    print()

    bla = True
    for i in range(len(color)):
        if bla:
            print(f"#{color[i]}#")
            bla = not bla
        elif not bla:
            print(f"**{color[i]}**")
            bla = not bla



