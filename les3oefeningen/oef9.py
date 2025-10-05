def foo():
    for i in range(10,21):
        if i % 2 == 0:
            for j in range(i,-1, -1):
                print(f"{j}",end=" ")
            print()


if __name__ == '__main__':
    foo()
