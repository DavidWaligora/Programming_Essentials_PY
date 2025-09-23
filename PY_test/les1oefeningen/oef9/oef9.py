#Write a program that helps you calculate the number of degrees Fahrenheit (Tf)
#when you enter the temperature in degrees Celsius (Tc). Use this conversion
#formula between Tc and Tf :

if __name__ == "__main__":
    celsius = float(input("Enter celsius: "))
    fahrenheit = float(celsius * (9/5)) + 32
    print(celsius)
    print(fahrenheit)