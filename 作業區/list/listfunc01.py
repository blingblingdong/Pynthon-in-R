# 建立一個串列 listScore 來存放五位同學的成績
listScore = [85, 92, 78, 90, 88]

# 計算最高分、最低分、成績加總及平均成績
highest_score = max(listScore)
lowest_score = min(listScore)
total_score = sum(listScore)
average_score = total_score / len(listScore)

# 打印同學的成績、最高分、最低分、成績加總與平均成績
scores_info = {
    "同學的成績": listScore,
    "最高分": highest_score,
    "最低分": lowest_score,
    "成績加總": total_score,
    "平均成績": average_score
}

scores_info
