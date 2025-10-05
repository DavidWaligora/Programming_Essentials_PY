# Write a program that allows a user to convert the results of a vote
#into percentages.
#The user enters the number of Yes votes, the number of No votes
#and the number of blank votes.
#The program shows the percentage of each type of vote.
#Exercise 3
#Write a program that reads a 3-digit number and prints the
#following information.

class Votes:
    def __init__(self, yes_amount, no_amount, blanc_amount):
        self.yes_amount = yes_amount
        self.no_amount = no_amount
        self.blanc_amount = blanc_amount

    def print_percentages(self):
        total_votes = self.yes_amount + self.no_amount + self.blanc_amount
        if total_votes == 0:
            print("No votes were cast.")
            return
        print("YES: ", str(self.yes_amount /total_votes * 100) + "%")
        print("NO: ", str(self.no_amount /total_votes * 100)+ "%")
        print("BLANC: " + str(self.blanc_amount / total_votes + 100)+ "%")

def get_votes():
    yes = int(input("How many people voted YES: "))
    no = int(input("How many people voted NO: "))
    blanc = int(input("How many people voted BLANC: "))
    return Votes(yes, no, blanc)

def main():
    votes:Votes = get_votes()
    votes.print_percentages()

if __name__ == "__main__":
    main()