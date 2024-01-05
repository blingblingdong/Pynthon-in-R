def HelloByName(c):
  
  n = len(c)
  
  if n == 0 :
    return
  print("-"*(n+2))
  print("!"+c+"!")
  print("-"*(n+2))
    
c = input("輸入要印的東西：")
HelloByName(c)
