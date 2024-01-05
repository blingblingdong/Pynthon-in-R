dictBook = {
    "001": ["書名一", 300],
    "002": ["書名二", 450],
    "003": ["書名三", 500]
}

# 使用字典的 key 逐一顯示 value 的內容
for key in dictBook:
    print(f"書號 {key}: 書名 - {dictBook[key][0]}, 單價 - {dictBook[key][1]}")

# 返回字典以供檢視
dictBook
