def feet_to_meters(feet):
    return feet * 0.3048

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    print("\nUnit Conversion")
    print("1: Feet to Meters")
    print("2: Celsius to Fahrenheit")
    print("Type 'exit' to end the program.")

    choice = input("Enter your choice: ")
    if choice.lower() == 'exit':
        break

    if choice == '1':
        feet = float(input("Enter length in feet: "))
        print(f"{feet} feet is {feet_to_meters(feet)} meters.")
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit.")
    else:
        print("Invalid choice. Please try again.")
