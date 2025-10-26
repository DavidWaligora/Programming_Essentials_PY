import json

if __name__ == '__main__':
    with open("files/file1.json") as file:
        jsonfile = json.load(file)
        count = 1
        for i in jsonfile["common"]:
            print(f"Plant number {count}")
            print(f"\tname: {i["common"]}")
            print(f"\tlight: {i["light"]}")
            print(f"\tprice: {i["price"]}")
            count+=1

