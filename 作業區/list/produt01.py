# 建立三個串列分別用來存放產品編號、品名和單價的資料
product_ids = ["P001", "P002", "P003", "P004"]
product_names = ["產品A", "產品B", "產品C", "產品D"]
product_prices = [100, 200, 300, 400]

# 由於無法在這個環境中使用 input() 函數，我們將模擬使用者輸入
# 假設使用者想要查詢第二項產品的資訊
user_input = 2  # 使用者輸入的索引，實際情況下應由 input() 函數獲得

# 確保使用者輸入的索引是有效的
if 1 <= user_input <= len(product_ids):
    # 由於串列索引從0開始，所以我們從使用者輸入的數字中減去1
    index = user_input - 1
    # 獲取對應的產品資訊
    product_id = product_ids[index]
    product_name = product_names[index]
    product_price = product_prices[index]
    product_info = (product_id, product_name, product_price)
else:
    product_info = "輸入的項目編號無效。"

product_info
