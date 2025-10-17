

if __name__ == '__main__':
    givemesome = list()
    num = float()
    while num != -1:
        num = float(input("score: "))
        if num != -1:
            givemesome.append(num)

    amount = len(givemesome)
    print(amount)
    givemesome.sort()
    print("The scores (ordered): "+ str(givemesome))
    print("the average score is: " +  str(sum(givemesome)/amount))
