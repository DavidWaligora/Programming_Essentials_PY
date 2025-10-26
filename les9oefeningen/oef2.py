def findamount(file):
    unique_lines = set()
    for line in file:
        line = line.strip()  # remove whitespace and newlines
        if line:
            unique_lines.add(line)
    return len(unique_lines)

def printalfabetical(file):
    unique_lines = set()
    for line in file:
        line = line.strip()  # remove whitespace and newlines
        if line:
            unique_lines.add(line)
    alfabetic = list(unique_lines)
    alfabetic.sort()
    for i in alfabetic:
        print(i)



if __name__ == '__main__':
    with open("Files Chapter 9/first_names1ITF.txt") as fileone:
        amountone = findamount(fileone)


    with open("Files Chapter 9/first_names2ITF.txt") as filetwo:
        amounttwo = findamount(filetwo)

    print(amountone)
    print(amounttwo)

    with open("Files Chapter 9/first_names1ITF.txt") as fileone:
        bla = printalfabetical(fileone)

    with open("Files Chapter 9/first_names2ITF.txt") as filetwo:
        bla = printalfabetical(filetwo)

