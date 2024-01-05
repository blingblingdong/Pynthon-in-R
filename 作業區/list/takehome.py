# 讓使用者輸入數字並加入串列中
numbers = []
while True:
    input_str = input("Enter a number (or 'done' to finish): ")
    if input_str.lower() == 'done':
        break
    try:
        number = float(input_str)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# 檢查數字數量是否足夠
if len(numbers) <= 2:
    print("Data insufficient. Please enter more than two numbers.")
else:
    # 去除兩個最低分
    numbers.remove(min(numbers))
    numbers.remove(min(numbers))
    # 計算總和
    total = sum(numbers)
    print(f"The sum of the numbers, excluding the two lowest, is: {total}")
