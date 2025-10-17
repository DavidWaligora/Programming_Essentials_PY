from dataclasses import replace

some_numberstostart = [334,78,765,657,43,5423,43,31,0,0,14,0,6,5645,5,0]

def zero_with_largest_odd(sometimes):
    onlyOdd = list()
    for sometime in sometimes:
        if sometime % 2 != 0:
            onlyOdd.append(sometime)


    if len(onlyOdd) == 0:
        return sometimes
    else:
        largest_odd = max(onlyOdd)
        # modify the list in-place using indexes
        for idx in range(len(sometimes)):
            if sometimes[idx] == 0:
                sometimes[idx] = largest_odd

        return sometimes



if __name__ == '__main__':
    print(some_numberstostart)
    numbers = zero_with_largest_odd(some_numberstostart)
    print(numbers)
