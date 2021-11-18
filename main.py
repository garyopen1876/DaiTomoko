from PIL import Image, ImageTk
import pymysql
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
root.configure(bg=sett.back_ground_color)
# icon
root.iconbitmap(sett.icon)
# 封面圖片
#  main_img = Image.open(sett.main_picture)
# main_imgTk = ImageTk.PhotoImage(main_img)
#  = tk.Label(main_window, image=main_imgTk)
# img_label.grid(row=0, column=0, sticky=sett.align_mode)

# 全域變數
vocabulary_array = []
question_number = 0


# 題庫會入
def vocabulary_in():
    with open('日文詞彙.csv', encoding='utf-8-sig') as csvfile:
        # 讀取 CSV 檔案內容
        data = csv.reader(csvfile)
        for line in data:
            vocabulary_array.append(line)


# 隨機出題
def question_show():
    global question_number
    question_number = random.randint(0, len(vocabulary_array)-1)
    label_question = tk.Label(root, text=vocabulary_array[question_number][0], bg=sett.back_ground_color)
    label_question.grid(row=0, column=0, columnspan=2)
    label_mean = tk.Label(root, text=vocabulary_array[question_number][1], bg=sett.back_ground_color)
    label_mean.grid(row=1, column=0, columnspan=2)


# 答案顯示
def answer_show():
    global question_number
    # 新視窗相關
    new_window = tk.Toplevel(root)
    new_window.title('答案顯示')
    new_window.geometry('300x100')
    new_window.iconbitmap(sett.icon)
    new_window.configure(bg='#FF95CA')
    # 顯示
    label_wrong = tk.Label(new_window, text=vocabulary_array[question_number][2], bg=sett.back_ground_color)
    label_wrong.pack()


# 答案比對
def vocabulary_check():
    global question_number
    if landString.get() == vocabulary_array[question_number][1]:
        # 回答正確 換題
        question_show()
    else:
        # 新視窗相關
        new_window = tk.Toplevel(root)
        new_window.title('你好爛')
        new_window.geometry('300x100')
        new_window.iconbitmap(sett.icon)
        new_window.configure(bg=sett.back_ground_color)
        # 顯示
        label_wrong = tk.Label(new_window, text="錯了 你好爛喔", bg=sett.back_ground_color)
        label_wrong.pack()


# 資料庫新增
def database_new(vocabulary):
    # 建立Connection物件
    conn = pymysql.connect(**sett.db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        # 新增資料SQL語法
        command = "INSERT INTO vocabulary(Numbe, Word, Hiragana, Chinese)VALUES(%s, %s, %s, %s)"

        cursor.execute(command, (1, vocabulary['word'], vocabulary['hiragana'], vocabulary['chinese']))
    # 儲存變更
    conn.commit()


# 新增詞彙
def vocabulary_new():
    # 新視窗相關
    new_window = tk.Toplevel(root)
    new_window.title('新增詞彙')
    new_window.geometry('300x100')
    new_window.iconbitmap(sett.icon)
    new_window.configure(bg=sett.back_ground_color)

    # 顯示
    show_word = tk.Label(new_window, text="單字:", bg=sett.back_ground_color)
    land_word = tk.StringVar()
    entry_word = tk.Entry(new_window, width=20, textvariable=land_word)
    show_hiragana = tk.Label(new_window, text="平假名:", bg=sett.back_ground_color)
    land_hiragana = tk.StringVar()
    entry_hiragana = tk.Entry(new_window, width=20, textvariable=land_hiragana)
    show_chinese = tk.Label(new_window, text="中文:", bg=sett.back_ground_color)
    land_chinese = tk.StringVar()
    entry_chinese = tk.Entry(new_window, width=20, textvariable=land_chinese)

    vocabulary_detail = {
        'word': entry_word,
        'hiragana': entry_hiragana,
        'chinese': entry_chinese
    }

    # 排版
    show_word.grid(row=0, column=0, padx=10)
    entry_word.grid(row=0, column=1, padx=10)
    show_hiragana.grid(row=1, column=0, padx=10)
    entry_hiragana.grid(row=1, column=1, padx=10)
    show_chinese.grid(row=2, column=0, padx=10)
    entry_chinese.grid(row=2, column=1, padx=10)

    vocabulary_new_submit = tk.Button(new_window, text='確認', padx=20, pady=20, bg='#ACD6FF',
                                      command=lambda: database_new(vocabulary_detail))
    vocabulary_new_submit.grid(row=3, column=0, sticky=sett.align_mode)
    vocabulary_new_cancel = tk.Button(new_window, text='取消', padx=20, pady=20, bg='#ACD6FF', command=answer_show)
    vocabulary_new_cancel.grid(row=3, column=1, sticky=sett.align_mode)


# 執行會入
vocabulary_in()
# 顯示題目
question_show()

# 輸入
landString = tk.StringVar()
entryLand = tk.Entry(root, width=20, textvariable=landString)
entryLand.grid(row=2, column=0, padx=10, columnspan=2)

# 按鈕
button_submit = tk.Button(root, text='確認', padx=20, pady=20, bg='#ACD6FF', command=vocabulary_check)
button_submit.grid(row=3, column=0, sticky=sett.align_mode)
button_answer = tk.Button(root, text='答案', padx=20, pady=20, bg='#ACD6FF', command=answer_show)
button_answer.grid(row=3, column=1, sticky=sett.align_mode)
button_change = tk.Button(root, text='換題', padx=90, pady=10, bg='#ACD6FF', command=question_show)
button_change.grid(row=4, column=0, columnspan=2)
button_new = tk.Button(root, text='新增詞彙', padx=78, pady=10, bg='#B9B9FF', command=vocabulary_new)
button_new.grid(row=6, column=0, columnspan=2)

root.mainloop()

