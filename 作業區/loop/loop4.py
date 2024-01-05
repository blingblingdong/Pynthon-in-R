total = 0
while True:
    input_str = input("Enter a number (or 'done' to finish): ")
    if input_str.lower() == 'done':
        break
    try:
        number = float(input_str)
        total += number
    except ValueError:
        print("Please enter a valid number.")

print(f"The sum of all entered numbers is: {total}")
