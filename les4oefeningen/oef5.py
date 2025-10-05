if __name__ == "__main__":
    text = input("Enter text: ")
    triples = 0
    for i in range(int(len(text))):
        if i < (len(text) - 2):
            if text[i] == text[i+1] and text[i] == text[i+2]:
               triples += 1

    print(triples)


