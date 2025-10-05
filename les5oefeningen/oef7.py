
if __name__ == '__main__':
    one = [2,4,5,9]
    amount: int = len(one) * 2
    result = list()
    for x in range(amount):
        result.append(0)

    result[-1] = one[-1]
    print(result)
