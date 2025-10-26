import json

if __name__ == '__main__':
    with open("files/file1.json") as file:
        filedata = json.load(file)
        for i in filedata["common"]:
            data = str(i).lstrip()
            data = data.replace("'", "")
            data = data.replace(":","")
            data = data.replace("{", "")
            data = data.replace("}", "")
            data = data.replace(",", "\n")
            print(data)