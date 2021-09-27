
from PIL import Image, ImageTk
import tkinter as tk

import settings
import settings as sett


aiueo_window = tk.Tk()

# 視窗標題
aiueo_window.title('DaiTomko')
# 視窗大小
aiueo_window.geometry('800x1000')
# 背景顏色
aiueo_window.configure(bg='#FF95CA')
# icon
aiueo_window.iconbitmap(sett.icon)

# あ
button_a = tk.Button(aiueo_window, text='あ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                     bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_i = tk.Button(aiueo_window, text='い', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                     bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_u = tk.Button(aiueo_window, text='う', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                     bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_e = tk.Button(aiueo_window, text='え', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                     bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_o = tk.Button(aiueo_window, text='お', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                     bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# か
button_ka = tk.Button(aiueo_window, text='か', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ki = tk.Button(aiueo_window, text='き', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ku = tk.Button(aiueo_window, text='く', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ke = tk.Button(aiueo_window, text='け', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ko = tk.Button(aiueo_window, text='こ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# さ
button_sa = tk.Button(aiueo_window, text='さ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_si = tk.Button(aiueo_window, text='し', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_su = tk.Button(aiueo_window, text='す', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_se = tk.Button(aiueo_window, text='せ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_so = tk.Button(aiueo_window, text='そ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# た
button_ta = tk.Button(aiueo_window, text='た', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_chi = tk.Button(aiueo_window, text='ち', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                       bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_tsu = tk.Button(aiueo_window, text='つ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                       bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_te = tk.Button(aiueo_window, text='て', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_to = tk.Button(aiueo_window, text='と', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# な
button_na = tk.Button(aiueo_window, text='な', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ni = tk.Button(aiueo_window, text='に', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_nu = tk.Button(aiueo_window, text='ぬ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ne = tk.Button(aiueo_window, text='ね', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_no = tk.Button(aiueo_window, text='の', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# は
button_ha = tk.Button(aiueo_window, text='は', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_hi = tk.Button(aiueo_window, text='ひ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_fu = tk.Button(aiueo_window, text='ふ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_he = tk.Button(aiueo_window, text='へ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ho = tk.Button(aiueo_window, text='ほ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# ま
button_ma = tk.Button(aiueo_window, text='ま', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_mi = tk.Button(aiueo_window, text='み', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_mu = tk.Button(aiueo_window, text='む', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_me = tk.Button(aiueo_window, text='め', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_mo = tk.Button(aiueo_window, text='も', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# や
button_ya = tk.Button(aiueo_window, text='や', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_y_no = tk.Button(aiueo_window, text='', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                        bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_yu = tk.Button(aiueo_window, text='ゆ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ye = tk.Button(aiueo_window, text='', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_yo = tk.Button(aiueo_window, text='よ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# ら
button_ra = tk.Button(aiueo_window, text='ら', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ri = tk.Button(aiueo_window, text='り', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ru = tk.Button(aiueo_window, text='る', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_re = tk.Button(aiueo_window, text='れ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_ro = tk.Button(aiueo_window, text='ろ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# わ
button_wa = tk.Button(aiueo_window, text='わ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_wi = tk.Button(aiueo_window, text='ゐ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_w_no = tk.Button(aiueo_window, text='', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                        bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_we = tk.Button(aiueo_window, text='ゑ', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
button_wo = tk.Button(aiueo_window, text='を', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                      bg=sett.aiueo_button_color, font=sett.aiueo_button_font)
# ん
button_n = tk.Button(aiueo_window, text='ん', padx=sett.aiueo_button_padx, pady=settings.aiueo_button_pady,
                     bg=sett.aiueo_button_color, font=sett.aiueo_button_font)


# あ
button_a.grid(row=0, column=0, sticky=sett.align_mode)
button_i.grid(row=1, column=0, sticky=sett.align_mode)
button_u.grid(row=2, column=0, sticky=sett.align_mode)
button_e.grid(row=3, column=0, sticky=sett.align_mode)
button_o.grid(row=4, column=0, sticky=sett.align_mode)
# か
button_ka.grid(row=0, column=1, sticky=sett.align_mode)
button_ki.grid(row=1, column=1, sticky=sett.align_mode)
button_ku.grid(row=2, column=1, sticky=sett.align_mode)
button_ke.grid(row=3, column=1, sticky=sett.align_mode)
button_ko.grid(row=4, column=1, sticky=sett.align_mode)
# さ
button_sa.grid(row=0, column=2, sticky=sett.align_mode)
button_si.grid(row=1, column=2, sticky=sett.align_mode)
button_su.grid(row=2, column=2, sticky=sett.align_mode)
button_se.grid(row=3, column=2, sticky=sett.align_mode)
button_so.grid(row=4, column=2, sticky=sett.align_mode)
# た
button_ta.grid(row=0, column=3, sticky=sett.align_mode)
button_chi.grid(row=1, column=3, sticky=sett.align_mode)
button_tsu.grid(row=2, column=3, sticky=sett.align_mode)
button_te.grid(row=3, column=3, sticky=sett.align_mode)
button_to.grid(row=4, column=3, sticky=sett.align_mode)
# な
button_na.grid(row=0, column=4, sticky=sett.align_mode)
button_ni.grid(row=1, column=4, sticky=sett.align_mode)
button_nu.grid(row=2, column=4, sticky=sett.align_mode)
button_ne.grid(row=3, column=4, sticky=sett.align_mode)
button_no.grid(row=4, column=4, sticky=sett.align_mode)
# は
button_ha.grid(row=0, column=5, sticky=sett.align_mode)
button_hi.grid(row=1, column=5, sticky=sett.align_mode)
button_fu.grid(row=2, column=5, sticky=sett.align_mode)
button_he.grid(row=3, column=5, sticky=sett.align_mode)
button_ho.grid(row=4, column=5, sticky=sett.align_mode)
# ま
button_ma.grid(row=0, column=6, sticky=sett.align_mode)
button_mi.grid(row=1, column=6, sticky=sett.align_mode)
button_mu.grid(row=2, column=6, sticky=sett.align_mode)
button_me.grid(row=3, column=6, sticky=sett.align_mode)
button_mo.grid(row=4, column=6, sticky=sett.align_mode)
# や
button_ya.grid(row=0, column=7, sticky=sett.align_mode)
button_y_no.grid(row=1, column=7, sticky=sett.align_mode)
button_yu.grid(row=2, column=7, sticky=sett.align_mode)
button_ye.grid(row=3, column=7, sticky=sett.align_mode)
button_yo.grid(row=4, column=7, sticky=sett.align_mode)
# ら
button_ra.grid(row=0, column=8, sticky=sett.align_mode)
button_ri.grid(row=1, column=8, sticky=sett.align_mode)
button_ru.grid(row=2, column=8, sticky=sett.align_mode)
button_re.grid(row=3, column=8, sticky=sett.align_mode)
button_ro.grid(row=4, column=8, sticky=sett.align_mode)
# わ
button_wa.grid(row=0, column=9, sticky=sett.align_mode)
button_wi.grid(row=1, column=9, sticky=sett.align_mode)
button_w_no.grid(row=2, column=9, sticky=sett.align_mode)
button_we.grid(row=3, column=9, sticky=sett.align_mode)
button_wo.grid(row=4, column=9, sticky=sett.align_mode)
# ん
button_n.grid(row=0, column=10, rowspan=5, sticky=sett.align_mode)

aiueo_window.mainloop()
