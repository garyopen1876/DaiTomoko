from PIL import Image, ImageTk
import tkinter as tk
import settings as sett


main_window = tk.Tk()

# 視窗標題
main_window.title('DaiTomko')
# 視窗大小
main_window.geometry('800x1000')
# 背景顏色
main_window.configure(bg='#FF95CA')
# icon
main_window.iconbitmap(sett.icon)
# 封面圖片
main_img = Image.open(sett.main_picture)
main_imgTk = ImageTk.PhotoImage(main_img)
img_label = tk.Label(main_window, image=main_imgTk)
img_label.grid(row=0, column=0, sticky=sett.align_mode)


def to_aiueo_window():
    main_window.destroy()
    from aiueo import aiueo_window


button_aiueo = tk.Button(main_window, text='50音', padx=70, pady=70, bg='#ACD6FF', command=to_aiueo_window)
button_vocabulary = tk.Button(main_window, text='日文詞彙', padx=70, pady=70, bg='#ACD6FF')

button_aiueo.grid(row=1, column=0, sticky=sett.align_mode)
button_vocabulary.grid(row=2, column=0, sticky=sett.align_mode)


main_window.mainloop()

