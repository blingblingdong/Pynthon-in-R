aa= int(input("輸入成績："))

if aa >= 90:
  print(f"研習成績優，成就非凡")
elif aa >= 80:
  print(f"研習成績甲，表現良好")
elif aa >= 70:
  print(f"研習成績乙，差強人意")
elif aa >= 60:
  print(f"研習成績丙，仍須努力")
elif aa >= 0:
  print(f"研習成績丁，待加強")
else :
  print(f"輸入錯誤，分數必須在0~100之間")
