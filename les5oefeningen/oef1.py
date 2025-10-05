original_list = ['cat', 'rabbit', 'mouse', 'rat', 'squirrel']

def print_and_reverse(somelist: list):
    print(somelist)
    somelist.reverse()
    print(somelist)


if __name__ == '__main__':
    print_and_reverse(original_list)
