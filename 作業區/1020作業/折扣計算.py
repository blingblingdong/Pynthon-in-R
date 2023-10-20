aa = int(input("請輸入價格："))

if aa > 500:
  bb = aa*0.5
elif aa > 400:
  bb = aa*0.6
elif aa>300:
  bb = aa*0.7
elif aa>200:
  bb = aa * 0.8
elif aa>100:
  bb = aa * 0.9
else :
  bb = aa

if aa > 100:
  print(f"打完折的價格是{bb}")
else :
  print(f"沒有折扣喔，你的價格是原價")
