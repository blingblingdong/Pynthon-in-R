n = input("phone")

i1 = 0

if len(n) != 13:
  i1 = 1

p = 0
while i1 == 1 and p < 13:
    if p == 0 and n[p] != "(":
      i1 = 1
    elif p == 4 and n[p] != ")":
      i1 = 1
    elif p == 8 and n[p] != "-":
      i1 = 1
    p = p +1
    
if i1 == 1:
  print("錯誤")
else:
  print(n)
  

