# 設某國之信用卡號第0碼必定為1
# 設某國之信用卡號第4碼必定為8
# 設某國之信用卡號第8碼必定為8
# 設某國之信用卡號只有8碼


n = input("credit card number")

i1 = 0

if len(n) != 8:
  i1 = 1

p = 0
while i1 == 1 and p < 8:
    if p == 0 and n[p] != "1":
      i1 = 1
    elif p == 4 and n[p] != "8":
      i1 = 1
    elif p == 8 and n[p] != "8":
      i1 = 1
    p = p +1
    
if i1 == 1:
  print("錯誤")
else:
  print(n)
  

