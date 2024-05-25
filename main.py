from tkinter import *
from tkinter.ttk import Frame
from pathlib import Path

from settings import *


def rgbtohex(r, g, b):
    """
    Возвращает строку формата RGB.

    :param r: red
    :param g: green
    :param b: blue
    :return: rgb format string - #******
    """
    return f'#{r:02x}{g:02x}{b:02x}'


# ======================== Кнопка начала ========================
def on_start(event=None):
    Button_start['image'] = b_start_dark


def off_start(event=None):
    Button_start['image'] = b_start


def change_color_start(event=None):
    Button_start['image'] = b_start_light
# ===============================================================


# ======================== Кнопка вперед ========================
def on_forward(event=None):
    forward_button['image'] = arrow_forward_dark_img
    forward_button['foreground'] = fg_w


def off_forward(event=None):
    forward_button['image'] = arrow_forward_img
    forward_button['foreground'] = fg_w


def change_color_forward(event=None):
    forward_button['image'] = arrow_forward_light_img
    forward_button['foreground'] = fg_b
# ===============================================================


# ======================== Кнопка назад =========================
def on_back(event=None):
    back_button['image'] = arrow_back_dark_img


def off_back(event=None):
    back_button['image'] = arrow_back_img


def change_color_back(event=None):
    back_button['image'] = arrow_back_light_img
# ===============================================================


# ========================= Кнопки дат ==========================
def date_btn_on(event, button):
    button["image"] = date_btn_img_dark
    button["foreground"] = fg_w


def date_btn_off(event, button):
    button["image"] = date_btn_img
    button["foreground"] = fg_w


def date_btn_clicked(event, button):
    button["image"] = date_btn_img_light
    button["foreground"] = fg_b
# ===============================================================


# ======================== Кнопки + и - =========================
def minus_btn_on(event):
    minus_button['image'] = minus_dark_img


def minus_btn_off(event):
    minus_button['image'] = minus_img


def minus_btn_clicked(event):
    minus_button['image'] = minus_light_img


def plus_btn_on(event):
    plus_button['image'] = plus_dark_img


def plus_btn_off(event):
    plus_button['image'] = plus_img


def plus_btn_clicked(event):
    plus_button['image'] = plus_light_img
# ===============================================================


def clearing_w_start():
    """
    Удаление всех виджетов из окна.

    :return: None
    """
    for widget in W.winfo_children():
        widget.place_forget()


def back_win():
    """
    Функция для открытия предыдущего окна в зависимости от window_number.

    :return: None
    """
    global window_number
    # if window_number == 2:
    #     clearing_w_start()
    #     window1()
    if window_number == 5:
        clearing_w_start()
        window2()


def next_win():
    """
    Функция для открытия следующего окна в зависимости от window_number.

    :return: None
    """
    try:
        function = globals().get(f"window{window_number+1}")
        function()
    except Exception as e:
        pass


def window1(event=None):
    """
    Размещает элементы интерфейса n-нного окна.

    :param e: None
    :return: None
    """
    global window_number
    window_number = 1
    bg_start.place(x=0, y=0)
    Button_start.place(x=130, y=600, width=243, height=54)


def additional_elements(event=None):
    """
    Одинаковые элементы окон - стрелки, фон и тп.

    :param e: None
    :return: None
    """
    background_label.place(x=0, y=0)

    arrows_block.place(x=24, y=height - 24 - 88)
    back_button.place(x=24 + 48, y=height - 24 - 24 - 48)
    forward_button.place(x=24 + 48 + 100 + 20, y=height - 24 - 24 - 48)


def window2(event=None):
    global window_number
    window_number = 2
    additional_elements()

    logo_label.place(x=24, y=44)
    date_label.place(x=24, y=124)

    date_button1.place(x=24, y=124 + 36 + 24)
    date_button2.place(x=24 + 104 + 24, y=124 + 36 + 24)
    date_button3.place(x=24 + 104 + 24 + 104 + 24, y=124 + 36 + 24)
    date_button4.place(x=24, y=124 + 36 + 24 + 48 + 24)
    date_button5.place(x=24 + 104 + 24, y=124 + 36 + 24 + 48 + 24)


def window3(event=None):
    global window_number
    window_number = 3

    time_label.place(x=24, y=124 + 36 + 24 + 48 + 24 + 32 + 48)  # 336

    time_button1.place(x=24,
                       y=336 + 36 + 24)
    time_button2.place(x=24 + 104 + 24,
                       y=336 + 36 + 24)
    time_button3.place(x=24 + 104 + 24 + 104 + 24,
                       y=336 + 36 + 24)
    time_button4.place(x=24,
                       y=336 + 36 + 24 + 48 + 24)
    time_button5.place(x=24 + 104 + 24,
                       y=336 + 36 + 24 + 48 + 24)
    time_button6.place(x=24 + 104 + 24 + 104 + 24,
                       y=336 + 36 + 24 + 48 + 24)
    time_button7.place(x=24,
                       y=336 + 36 + 24 + 48 + 24 + 48 + 24)
    time_button8.place(x=24 + 104 + 24,
                       y=336 + 36 + 24 + 48 + 24 + 48 + 24)
    time_button9.place(x=24 + 104 + 24 + 104 + 24,
                       y=336 + 36 + 24 + 48 + 24 + 48 + 24)
    time_button10.place(x=24,
                        y=336 + 36 + 24 + 48 + 24 + 48 + 24 + 48 + 24)
    time_button11.place(x=24 + 104 + 24,
                        y=336 + 36 + 24 + 48 + 24 + 48 + 24 + 48 + 24)
    time_button12.place(x=24 + 104 + 24 + 104 + 24,
                        y=336 + 36 + 24 + 48 + 24 + 48 + 24 + 48 + 24)


def window4(event=None):
    global window_number
    window_number = 4

    people_label.place(x=24, y=612 + 32 + 48)
    counter_block.place(x=24, y=612 + 32 + 48 + 24 + 38)

    minus_button.place(x=24 + 4, y=612 + 32 + 48 + 24 + 38 + 4)
    plus_button.place(x=24 + 214 - 28 - 4, y=612 + 32 + 48 + 24 + 38 + 4)


def window5(event=None):
    global window_number
    window_number = 5
    clearing_w_start()
    additional_elements()

    ...


if __name__ == "__main__":
    # ===================== Логика и параметры ===================
    window_number = 1  # Номер окна

    # Кнопки для дат:
    activated_date_button = False  # Либо номер кнопки 1-5, либо никакая - False

    # Доп цвета:
    label_green_color = rgbtohex(r=109, g=191, b=102)  # светло-зеленый
    bg_peach_color = rgbtohex(r=252, g=240, b=227)  # персиковый

    # ====================== Стартовое окно ======================
    W = Tk()
    W.geometry(f"{width}x{height}")
    W.title("Ресторан \"Хмели-сунели\"")
    W.resizable(False, False)
    W.iconbitmap(Path(window_logo))

    image_start = PhotoImage(file=Path(bg_with_logo))  # Стартовый фон

    # Изображения для разных фаз кнопки
    b_start = PhotoImage(file=Path(button_start))
    b_start_dark = PhotoImage(file=Path(button_start_dark))
    b_start_light = PhotoImage(file=Path(button_start_light))

    bg_start = Label(W, image=image_start, borderwidth=0)  # Фон через лейбл

    Button_start = Button(W, image=b_start, borderwidth=0,
                          text="ЗАБРОНИРОВАТЬ СТОЛ", compound="center",
                          fg=fg_w, font=global_font, activebackground=bg_peach_color,
                          command=window2)
    Button_start.bind('<Enter>', on_start)
    Button_start.bind('<Leave>', off_start)
    Button_start.bind('<Button-1>', change_color_start)

    # ====================== Второе окно ======================
    solid_background = PhotoImage(file=Path(solid_bg))
    background_label = Label(W, image=solid_background, borderwidth=0)

    # Логотипус:
    logo = PhotoImage(file=Path(logo_2))
    logo_label = Label(W, image=logo, borderwidth=0)


    # Стрелочки:
    arrows_block_image = PhotoImage(file=Path(arrows_block_bg))
    arrows_block = Label(W, image=arrows_block_image, borderwidth=0)

    arrow_back_img = PhotoImage(file=Path(arrow_back))
    arrow_back_dark_img = PhotoImage(file=Path(arrow_back_dark))
    arrow_back_light_img = PhotoImage(file=Path(arrow_back_light))

    back_button = Button(W, image=arrow_back_img, borderwidth=0,
                         compound="center", command=back_win, bg=bg_w, activebackground=bg_w)
    back_button.bind('<Enter>', on_back)
    back_button.bind('<Leave>', off_back)
    back_button.bind('<Button-1>', change_color_back)

    arrow_forward_img = PhotoImage(file=Path(arrow_forward))
    arrow_forward_dark_img = PhotoImage(file=Path(arrow_forward_dark))
    arrow_forward_light_img = PhotoImage(file=Path(arrow_forward_light))

    forward_button = Button(W, image=arrow_forward_img, borderwidth=0,
                            text="ДАЛЕЕ", font=global_font, foreground=fg_w,
                            compound="center", command=next_win, bg=bg_w, activebackground=bg_w)
    forward_button.bind('<Enter>', on_forward)
    forward_button.bind('<Leave>', off_forward)
    forward_button.bind('<Button-1>', change_color_forward)

    # Даты:
    date_label = Label(W, borderwidth=0, font=label_font, text="Выберите дату",
                       fg=label_green_color, bg=bg_peach_color)

    date_btn_img = PhotoImage(file=Path(date_button))
    date_btn_img_light = PhotoImage(file=Path(date_button_light))
    date_btn_img_dark = PhotoImage(file=Path(date_button_dark))
    date_btn_img_on = PhotoImage(file=Path(date_button_on))

    date_button1 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="29 мая", font=global_font, foreground=fg_w)
    date_button2 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="31 мая", font=global_font, foreground=fg_w)
    date_button3 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="1 июня", font=global_font, foreground=fg_w)
    date_button4 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="7 июня", font=global_font, foreground=fg_w)
    date_button5 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="10 июня", font=global_font, foreground=fg_w)

    date_button1.bind('<Enter>', lambda event: date_btn_on(event, date_button1))
    date_button1.bind('<Leave>', lambda event: date_btn_off(event, date_button1))
    date_button1.bind('<Button-1>', lambda event: date_btn_clicked(event, date_button1))
    date_button2.bind('<Enter>', lambda event: date_btn_on(event, date_button2))
    date_button2.bind('<Leave>', lambda event: date_btn_off(event, date_button2))
    date_button2.bind('<Button-1>', lambda event: date_btn_clicked(event, date_button2))
    date_button3.bind('<Enter>', lambda event: date_btn_on(event, date_button3))
    date_button3.bind('<Leave>', lambda event: date_btn_off(event, date_button3))
    date_button3.bind('<Button-1>', lambda event: date_btn_clicked(event, date_button3))
    date_button4.bind('<Enter>', lambda event: date_btn_on(event, date_button4))
    date_button4.bind('<Leave>', lambda event: date_btn_off(event, date_button4))
    date_button4.bind('<Button-1>', lambda event: date_btn_clicked(event, date_button4))
    date_button5.bind('<Enter>', lambda event: date_btn_on(event, date_button5))
    date_button5.bind('<Leave>', lambda event: date_btn_off(event, date_button5))
    date_button5.bind('<Button-1>', lambda event: date_btn_clicked(event, date_button5))

    # Время:
    time_label = Label(W, borderwidth=0, font=label_font, text="Выберите время",
                       fg=label_green_color, bg=bg_peach_color)

    time_button1 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="16:00", font=global_font, foreground=fg_w)
    time_button2 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="17:00", font=global_font, foreground=fg_w)
    time_button3 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="18:00", font=global_font, foreground=fg_w)
    time_button4 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="18:30", font=global_font, foreground=fg_w)
    time_button5 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="19:00", font=global_font, foreground=fg_w)
    time_button6 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="20:00", font=global_font, foreground=fg_w)
    time_button7 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="20:30", font=global_font, foreground=fg_w)
    time_button8 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="21:00", font=global_font, foreground=fg_w)
    time_button9 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                          text="21:30", font=global_font, foreground=fg_w)
    time_button10 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                           compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                           text="22:00", font=global_font, foreground=fg_w)
    time_button11 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                           compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                           text="22:30", font=global_font, foreground=fg_w)
    time_button12 = Button(W, image=date_btn_img, borderwidth=0,  # , command=next_win
                           compound="center", bg=bg_peach_color, activebackground=bg_peach_color,
                           text="23:00", font=global_font, foreground=fg_w)

    time_button1.bind('<Enter>', lambda event: date_btn_on(event, time_button1))
    time_button1.bind('<Leave>', lambda event: date_btn_off(event, time_button1))
    time_button1.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button1))
    time_button2.bind('<Enter>', lambda event: date_btn_on(event, time_button2))
    time_button2.bind('<Leave>', lambda event: date_btn_off(event, time_button2))
    time_button2.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button2))
    time_button3.bind('<Enter>', lambda event: date_btn_on(event, time_button3))
    time_button3.bind('<Leave>', lambda event: date_btn_off(event, time_button3))
    time_button3.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button3))
    time_button4.bind('<Enter>', lambda event: date_btn_on(event, time_button4))
    time_button4.bind('<Leave>', lambda event: date_btn_off(event, time_button4))
    time_button4.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button4))
    time_button5.bind('<Enter>', lambda event: date_btn_on(event, time_button5))
    time_button5.bind('<Leave>', lambda event: date_btn_off(event, time_button5))
    time_button5.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button5))
    time_button6.bind('<Enter>', lambda event: date_btn_on(event, time_button6))
    time_button6.bind('<Leave>', lambda event: date_btn_off(event, time_button6))
    time_button6.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button6))
    time_button7.bind('<Enter>', lambda event: date_btn_on(event, time_button7))
    time_button7.bind('<Leave>', lambda event: date_btn_off(event, time_button7))
    time_button7.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button7))
    time_button8.bind('<Enter>', lambda event: date_btn_on(event, time_button8))
    time_button8.bind('<Leave>', lambda event: date_btn_off(event, time_button8))
    time_button8.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button8))
    time_button9.bind('<Enter>', lambda event: date_btn_on(event, time_button9))
    time_button9.bind('<Leave>', lambda event: date_btn_off(event, time_button9))
    time_button9.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button9))
    time_button10.bind('<Enter>', lambda event: date_btn_on(event, time_button10))
    time_button10.bind('<Leave>', lambda event: date_btn_off(event, time_button10))
    time_button10.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button10))
    time_button11.bind('<Enter>', lambda event: date_btn_on(event, time_button11))
    time_button11.bind('<Leave>', lambda event: date_btn_off(event, time_button11))
    time_button11.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button11))
    time_button12.bind('<Enter>', lambda event: date_btn_on(event, time_button12))
    time_button12.bind('<Leave>', lambda event: date_btn_off(event, time_button12))
    time_button12.bind('<Button-1>', lambda event: date_btn_clicked(event, time_button12))

    # Количество человек:
    people_label = Label(W, borderwidth=0, font=label_font, text="Выберите количество гостей",
                         fg=label_green_color, bg=bg_peach_color)

    counter_img_bg = PhotoImage(file=Path(counter_bg))
    counter_block = Label(W, image=counter_img_bg, borderwidth=0, compound="center", bg=bg_peach_color,
                          text="1", foreground=fg_b, font=global_font)

    minus_img = PhotoImage(file=Path(minus_normal))
    minus_light_img = PhotoImage(file=Path(minus_light))
    minus_dark_img = PhotoImage(file=Path(minus_dark))
    plus_img = PhotoImage(file=Path(plus_normal))
    plus_light_img = PhotoImage(file=Path(plus_light))
    plus_dark_img = PhotoImage(file=Path(plus_dark))

    minus_button = Button(W, image=minus_img, borderwidth=0,  # , command=next_win
                          compound="center", bg=fg_w, activebackground=fg_w)
    plus_button = Button(W, image=plus_img, borderwidth=0,  # , command=next_win
                         compound="center", bg=fg_w, activebackground=fg_w)

    minus_button.bind('<Enter>', minus_btn_on)
    minus_button.bind('<Leave>', minus_btn_off)
    minus_button.bind('<Button-1>', minus_btn_clicked)
    plus_button.bind('<Enter>', plus_btn_on)
    plus_button.bind('<Leave>', plus_btn_off)
    plus_button.bind('<Button-1>', plus_btn_clicked)

    # ====================== Третье окно ======================
    menu_label = Label(W, borderwidth=0, font=label_font, text="Выберите состав меню",
                       fg=label_green_color, bg=bg_peach_color)


    # ====================== Вызовы окон ======================
    window1()  # Отображение элементов интерфейса первого окна

    W.mainloop()
