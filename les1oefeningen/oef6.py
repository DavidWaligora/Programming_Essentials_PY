#Write a program that allows you to repeat a word on the screen. You let the user choose a text and
#the number of times the text will be repeated.

if __name__ == "__main__":
    number = int(input("Enter number: "))
    text = str(input("Enter text: "))
    print(str(number), "times your text:")
    for i in range(number):
        print(i+1, text)