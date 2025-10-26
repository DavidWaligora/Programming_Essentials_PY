import json

if __name__ == '__main__':
    with open("Files Chapter 10/ex2_courses.json") as file:
        jsonfile = json.load(file)
        courses = jsonfile["courses"]
        for course in courses:
            print(course["name"])
            groups = course["groups"]
            print(end="\t")
            amount = 0
            for i in groups:
                print(i["name"], end="\t")
                amount += i["students"]
            print()
            print(f"\tTotal students in {course["name"]} = {amount}")
            print()