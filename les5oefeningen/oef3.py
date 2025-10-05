original_list = ['cat', 'rabbit', 'mouse', 'rat', 'squirrel']

def slide_list_one_left(lst):
    if not lst:
        return lst  # handle empty list safely
    return lst[1:] + [lst[0]]


if __name__ == '__main__':
    print('original list: ', original_list)
    original_list = slide_list_one_left(original_list)
    print('after sliding: ', original_list)
