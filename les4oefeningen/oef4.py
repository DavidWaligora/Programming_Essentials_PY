
def check_if_palindrome(word):
    length = len(word)
    for i in range(length):
        if word[i] != word[length-i-1]:
            return False

    return True
if __name__ == "__main__":
    word = input("Enter a word: ")
    foo = check_if_palindrome(word)
    if foo:
        print("Palindrome")
    else:
        print("Not Palindrome")
