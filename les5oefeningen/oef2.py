import random

original_list = [random.randint(1, 100) for _ in range(10)]
even_numbers = list()
odd_numbers = list()
if __name__ == '__main__':
    print(original_list, end='')
    print(" becomes ", end='')

    for i in original_list:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    list_toprint = list(even_numbers)  + list(odd_numbers)
    print(list_toprint)
