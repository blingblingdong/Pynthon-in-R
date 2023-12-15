while True:
    try:
        # 輸入第一個正整數
        num1 = int(input("請輸入第一個正整數: "))

        # 輸入第二個正整數
        num2 = int(input("請輸入第二個正整數: "))

        # 計算餘數
        result = num1 % num2

        # 輸出結果
        print(f"{num1} 除以 {num2} 的餘數是 {result}")

        # 如果沒有發生錯誤，跳出迴圈
        break

    except ValueError:
        print("錯誤：請輸入有效的數字。")

    except ZeroDivisionError:
        print("錯誤：除數不能為零。請重新輸入。")

