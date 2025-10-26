import json

if __name__ == '__main__':
    with open("Files Chapter 10/ex2_courses.json") as file:
        jsonfile = json.load(file)
        courses = jsonfile["courses"]
        for course in courses:
            print(course["name"])
            groups = course["groups"]
            print(end="\t")
            for i in groups:
                print(i["name"], end="\t")

            print()