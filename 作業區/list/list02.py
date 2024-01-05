# 建立兩個串列分別用來存放四位同學的姓名和成績

# 存放姓名的串列
name = ["同學A", "同學B", "同學C", "同學D"]

# 存放成績的串列
score = [90, 85, 88, 92]

# 打印出兩個串列確認內容
name, score


# 將每位同學的姓名和成績互相對應並顯示出來
for i in range(len(name)):
    print(f"{name[i]} 的成績是 {score[i]}")
