def get_amount_uppers(blabla):
    i = 0
    amount = 0
    length = len(blabla)
    while i < length:
        if blabla[i].isupper():
            amount += 1
        i += 1

    return amount


if __name__ == '__main__':
    for i in [1, 2, 300]:
        print(i)

    result = get_amount_uppers(input("Enter a wordOr: "))
    print(result)

assert get_amount_uppers("HHH") == 3, "fuck off"
assert get_amount_uppers("HHd") == 2, "Fuck off"
assert get_amount_uppers("HHH") == 2, "Fuck off"
for i in [1,2,300]:
    print(i)
