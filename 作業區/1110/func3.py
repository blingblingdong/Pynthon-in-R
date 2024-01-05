def HelloByName():
  
  n = input("輸入名字")
  g = bool(input("輸入性別"))
  
  if g == True :
    print(f"Hello大家好，我是{n}先生")
  else :
    print(f"Hello大家好，我是{n}女生")
    

HelloByName()
