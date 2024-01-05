number = 57361

# 萬位
wan = number // 10000
# 千位
qian = (number % 10000) // 1000
# 百位
bai = (number % 1000) // 100
# 十位
shi = (number % 100) // 10
# 個位
ge = number % 10

print("萬位:", wan)
print("千位:", qian)
print("百位:", bai)
print("十位:", shi)
print("個位:", ge)
