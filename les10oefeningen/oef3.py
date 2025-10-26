import json


def get_club_members():
    club_members_list = []
    name = input("Name of the club member: ")

    while name.lower() != "end":
        shortsize = input("Short size (S/M/L/XL): ")
        tshirtsize = input("T-shirt size (S/M/L/XL): ")
        newbackpack = input("New backpack? (Y/N): ")
        clubmember = {
            "name": name,
            "short size": shortsize.upper(),
            "t-shirt size": tshirtsize.upper(),
            "new backpack": newbackpack.strip().upper() == "Y"
        }

        if clubmember in club_members_list:
            print("That member already exists.")
        else:
            club_members_list.append(clubmember)

        name = input("Name of the club member: ")

    return club_members_list


def get_club_order(members_orders):
    # Initialize counters
    order_summary = {
        "short sizes": {"S": 0, "M": 0, "L": 0, "XL": 0},
        "t-shirt sizes": {"S": 0, "M": 0, "L": 0, "XL": 0},
        "backpacks": {"New": 0, "Old": 0}
    }

    for member in members_orders:
        short_size = member["short size"]
        if short_size in order_summary["short sizes"]:
            order_summary["short sizes"][short_size] += 1
        else:
            order_summary["short sizes"][short_size] = 1

        tshirt_size = member["t-shirt size"]
        if tshirt_size in order_summary["t-shirt sizes"]:
            order_summary["t-shirt sizes"][tshirt_size] += 1
        else:
            order_summary["t-shirt sizes"][tshirt_size] = 1

        if member["new backpack"]:
            order_summary["backpacks"]["New"] += 1
        else:
            order_summary["backpacks"]["Old"] += 1

    return order_summary


if __name__ == '__main__':
    club_members = get_club_members()
    print("\nClub Members:")
    for m in club_members:
        print(m)

    club_order = get_club_order(club_members)
    print("\nOrder Summary:")
    print(club_order)
    with open("files/file2.json", "w") as file:
        json.dump(club_order, file, indent=4)
