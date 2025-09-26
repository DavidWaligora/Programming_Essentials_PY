#Write a program to convert an amount in Euro into Dollar. You first have to read the current exchange rate
def euro_to_dollar_excache():
    rate = float(input("Enter the current excha,ge dollar rate (€->$): "))
    euro_amount = float(input("Enter the amount in euro: "))
    print(str(euro_amount), "€", "=", float(euro_amount * rate),"$")

if __name__ == "__main__":
    euro_to_dollar_excache()