#Electricity companies charge their customers a fixed annual amount of € 83.6 (connection, meter
#rental, maintenance, ...).
#At night you pay 0,035 € / kilowatt per hour. During the day you pay 0,068 €/ kilowatt per hour.
#On top of that, the customer also has to pay 21% VAT.
#Create a program that calculates how much you have to pay. First the customer has to enter his data
#(power consumption is always a whole number).
#Then the customer gets an overview of his account.

class ElectricityBill:
    FIXED_COST = 83.6
    DAY_RATE = 0.068
    NIGHT_RATE = 0.035
    VAT = 0.21

    def __init__(self, day_kwh: int, night_kwh: int):
        self.day_kwh = day_kwh
        self.night_kwh = night_kwh

    def calculate_day_cost(self):
        return self.day_kwh * self.DAY_RATE

    def calculate_night_cost(self):
        return self.night_kwh * self.NIGHT_RATE

    def calculate_subtotal(self):
        return self.FIXED_COST + self.calculate_day_cost() + self.calculate_night_cost()

    def calculate_total(self):
        return self.calculate_subtotal() * (1 + self.VAT)

    def print_invoice(self):
        day_cost = self.calculate_day_cost()
        night_cost = self.calculate_night_cost()
        subtotal = self.calculate_subtotal()
        total = self.calculate_total()

        print("\n--- Electricity Bill ---")
        print(f"Fixed annual cost: €{self.FIXED_COST}")
        print(f"Day consumption: €{day_cost}")
        print(f"Night consumption: €{night_cost}")
        print(f"Subtotal (excl. VAT): €{subtotal}")
        print(f"Total (incl. 21% VAT): €{total}")


def main():
    day_kwh = int(input("Enter daytime consumption (kWh): "))
    night_kwh = int(input("Enter nighttime consumption (kWh): "))

    bill = ElectricityBill(day_kwh, night_kwh)
    bill.print_invoice()


if __name__ == "__main__":
    main()
