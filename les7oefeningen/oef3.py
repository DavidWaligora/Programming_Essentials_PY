if __name__ == "__main__":
    with open("Files Chapter 7/first_names.txt") as file:
        firstnames_list = list()
        line = file.readline().strip()
        while line:
            if line != '\n':
                firstnames_list.append(line)
            line = file.readline().strip()


        per = 10
        now = 0

        lengthoflist = len(firstnames_list)

        while now <= lengthoflist:
            end = now + per
            bla = firstnames_list[now:end]
            for i in bla:
                print(i.ljust(10), end="")
            print()
            print("---")
            now = now + per