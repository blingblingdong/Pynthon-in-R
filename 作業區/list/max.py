# 初始化一個空串列來存儲整數
user_numbers = []

# 提示用戶輸入五個整數
for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    user_numbers.append(number)

# 從串列中找出最大數
max_number = max(user_numbers)

print(f"The largest number you entered is: {max_number}")
