def calculate_years(principal, rate, target):
    years = 0
    while principal < target:
        principal += principal * rate
        years += 1
    return years

# 自訂本金、利率和目標金額
principal = 10000  # 例如：本金 $10,000
rate = 0.05       # 例如：年利率 5%
target = 20000    # 例如：目標金額 $20,000

years_needed = calculate_years(principal, rate, target)
print(f"需要 {years_needed} 年才能從 ${principal} 達到目標金額 ${target}。")
