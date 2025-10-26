def printnumbers(sete):
    for i in sete:
        if i.isdigit():
            print(i)

def printletters(jee):
    for i in jee:
        if i.isalpha():
            print(i)




if __name__ == '__main__':
    set = set(input("give input letters and numbers: "))
    print("the numbers: " + "\n" )
    printnumbers(set)
    print("the letters: " + "\n")
    printletters(set)
