import tkinter as tk
import settings as sett


vocabulary_window = tk.Tk()

# 視窗標題
vocabulary_window.title('日文詞彙')
# 視窗大小
vocabulary_window.geometry('800x1000')
# 背景顏色
vocabulary_window.configure(bg='#FF95CA')
# icon
vocabulary_window.iconbitmap(sett.icon)


def to_main_window():
    vocabulary_window.destroy()
    from main import main_window


button_back = tk.Button(vocabulary_window, text='返回', padx=70, pady=70, bg='#ACD6FF', command=to_main_window)
button_back.grid(row=0, column=0, sticky=sett.align_mode)
