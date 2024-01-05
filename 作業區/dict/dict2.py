# 初始字典 dictBook
dictBook = {"a001": ["book1", 199]}

# 顯示初始字典
initial_dict = dictBook.copy()

# 新增元素到字典
dictBook["a002"] = ["book2", 299]

# 顯示新增後的字典
after_adding = dictBook.copy()

# 刪除元素
del dictBook["a001"]

# 顯示刪除後的字典
after_removing = dictBook.copy()

# 檢查 "a001" 是否存在於 dictBook 中
a001_exists = "a001" in dictBook

initial_dict, after_adding, after_removing, a001_exists
