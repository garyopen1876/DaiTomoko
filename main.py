from PIL import Image, ImageTk
import tkinter as tk
import settings as sett
import random
import csv

root = tk.Tk()

# 視窗標題
root.title('日文詞彙打字機')
# 視窗大小
root.geometry('500x300')
# 背景顏色
root.configure(bg='#FF95CA')
# icon
root.iconbitmap(sett.icon)
# 封面圖片
#  main_img = Image.open(sett.main_picture)
# main_imgTk = ImageTk.PhotoImage(main_img)
#  = tk.Label(main_window, image=main_imgTk)
# img_label.grid(row=0, column=0, sticky=sett.align_mode)

# 題目變數
questionString = ""
answerString = ""


# 隨機出題
def question_random():
    check = random.random()

    with open('日文詞彙.csv', encoding='utf-8-sig') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        # 以迴圈輸出每一列
        for row in rows:
            print(row)


# 答案比對
def vocabulary_check():
    if landString.get():
        print("做得好")
    else:
        print("爛死")


# 顯示題目
labelLand = tk.Label(root, text="Country")
labelLand.grid(column=0, row=0)

# 輸入
landString = tk.StringVar()
entryLand = tk.Entry(root, width=20, textvariable=landString)
entryLand.grid(row=1, column=0, padx=10)

# 按鈕
button_submit = tk.Button(root, text='提交', padx=20, pady=20, bg='#ACD6FF', command=question_random)
button_submit.grid(row=2, column=0, sticky=sett.align_mode)

root.mainloop()

