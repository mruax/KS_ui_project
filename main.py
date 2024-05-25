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
    return f"#{r:02x}{g:02x}{b:02x}"


# ======================== Кнопка начала ========================
def on_start(event=None):
    Button_start["image"] = b_start_dark


def off_start(event=None):
    Button_start["image"] = b_start


def change_color_start(event=None):
    Button_start["image"] = b_start_light
# ===============================================================


# ======================== Кнопка вперед ========================
def on_forward(event=None):
    forward_button["image"] = arrow_forward_dark_img
    forward_button["foreground"] = fg_w


def off_forward(event=None):
    forward_button["image"] = arrow_forward_img
    forward_button["foreground"] = fg_w


def change_color_forward(event=None):
    forward_button["image"] = arrow_forward_light_img
    forward_button["foreground"] = fg_b
# ===============================================================


# ======================== Кнопка назад =========================
def on_back(event=None):
    back_button["image"] = arrow_back_dark_img


def off_back(event=None):
    back_button["image"] = arrow_back_img


def change_color_back(event=None):
    back_button["image"] = arrow_back_light_img
# ===============================================================


# ========================= Кнопки дат ==========================
def date_btn_on(event, button):
    if not button.clicked:
        button["image"] = date_btn_img_dark
    else:
        button["image"] = date_btn_img_dark
    button["foreground"] = fg_w


def date_btn_off(event, button):
    if not button.clicked:
        button["image"] = date_btn_img
        button["foreground"] = fg_w
    else:
        button["image"] = date_btn_img_on
        button["foreground"] = fg_b


def date_btn_clicked(event, button):
    if button.clicked is False:
        button.clicked = True
    else:
        button.clicked = False
    select_date(event, button)

    null_other_date_buttons(event, button)


def null_other_date_buttons(event, button):
    for id in range(5):
        try:
            btn = globals().get(f"date_button{id + 1}")
            if btn["text"] == button["text"]:
                btn["foreground"] = fg_b
                button["image"] = date_btn_img_light
            else:
                btn["image"] = date_btn_img
                btn["foreground"] = fg_w
                btn.clicked = False
        except Exception as e:
            pass


def select_date(event, button):
    global user_selected_date
    if not user_selected_date:
        user_selected_date = button["text"]
        if window_number == 2:
            window3()
    elif not button.clicked:
        user_selected_date = None
# ===============================================================


# ======================= Кнопки времени ========================
def time_btn_clicked(event, button):
    if button.clicked is False:
        button.clicked = True
    else:
        button.clicked = False
    select_time(event, button)

    null_other_time_buttons(event, button)


def null_other_time_buttons(event, button):
    for id in range(12):
        try:
            btn = globals().get(f"time_button{id + 1}")
            if btn["text"] == button["text"]:
                btn["foreground"] = fg_b
                button["image"] = date_btn_img_light
            else:
                btn["image"] = date_btn_img
                btn["foreground"] = fg_w
                btn.clicked = False
        except Exception as e:
            pass


def select_time(event, button):
    global user_selected_time
    if not user_selected_time:
        user_selected_time = button["text"]
        if window_number == 3:
            window4()
    elif not button.clicked:
        user_selected_time = None
# ===============================================================


# ======================== Кнопки + и - =========================
def minus_btn_on(event):
    minus_button["image"] = minus_dark_img


def minus_btn_off(event):
    minus_button["image"] = minus_img


def minus_btn_clicked(event):
    global user_selected_people_amount
    minus_button["image"] = minus_light_img
    if user_selected_people_amount > 1:
        user_selected_people_amount -= 1
    if user_selected_people_amount == 1:
        minus_button["state"] = "disabled"
    else:
        minus_button["state"] = "active"
    plus_button["state"] = "active"
    counter_block["text"] = str(user_selected_people_amount)


def plus_btn_on(event):
    plus_button["image"] = plus_dark_img


def plus_btn_off(event):
    plus_button["image"] = plus_img


def plus_btn_clicked(event):
    global user_selected_people_amount
    plus_button["image"] = plus_light_img
    if user_selected_people_amount < 6:
        user_selected_people_amount += 1
    if user_selected_people_amount == 6:
        plus_button["state"] = "disabled"
    else:
        plus_button["state"] = "active"
    minus_button["state"] = "active"
    counter_block["text"] = str(user_selected_people_amount)
# ===============================================================


# =================== Кнопки блюд и напитков ====================
def button_dd_on(event, button):
    if not button.clicked:
        button['image'] = button_dd_dark
        button['foreground'] = fg_w


def button_dd_off(event, button):
    if not button.clicked:
        button['image'] = button_dd
        button['foreground'] = fg_w


def button_dd_clicked(event, button):
    global user_selected_page, user_selected_type
    if not button.clicked:
        user_selected_page = 1
        button['image'] = button_dd_white
        button['foreground'] = fg_b
        button_drinks.clicked = False
        button_dish.clicked = False
        if button == button_dish:
            button_drinks['image'] = button_dd
            button_drinks['foreground'] = fg_w
            user_selected_type = 1
        else:
            button_dish['image'] = button_dd
            button_dish['foreground'] = fg_w
            user_selected_type = 2
        button.clicked = True
# ==============================================================


# =================== Кнопки цифры =============================
def number_button_on(event, button):
    global user_selected_page, user_selected_type
    button['image'] = number_dark
    button['foreground'] = fg_w


def number_button_off(event, button):
    global user_selected_page, user_selected_type
    button['image'] = number
    button['foreground'] = fg_w


def number_button_clicked(event, button):
    global user_selected_page, user_selected_type
    button['image'] = number_light
    button['foreground'] = fg_b

# ==============================================================


def clearing_w_start():
    """
    Удаление всех виджетов из окна.

    :return: None
    """
    for widget in W.winfo_children():
        widget.place_forget()


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
        window3()
        window4()


def additional_elements(event=None):
    """
    Одинаковые элементы окон - лого, фон и тп.

    :param event: None
    :return: None
    """
    background_label.place(x=0, y=0)
    logo_label.place(x=36, y=50)


def add_arrows(event=None):
    """
    Добавляет блок к с кнопками.

    :param event: None
    :return: None
    """
    arrows_block.place(x=24, y=height - 24 - 88)
    back_button.place(x=24 + 48, y=height - 24 - 24 - 48)
    forward_button.place(x=24 + 48 + 100 + 20, y=height - 24 - 24 - 48)


def window1(event=None):
    """
    Размещает элементы интерфейса n-нного окна.

    :param event: None
    :return: None
    """
    global window_number
    window_number = 1
    bg_start.place(x=0, y=0)
    Button_start.place(x=130, y=600, width=243, height=54)


def window2(event=None):
    global window_number
    window_number = 2
    additional_elements()

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

    add_arrows()


def window5(event=None):
    global window_number
    window_number = 5
    clearing_w_start()
    additional_elements()
    add_arrows()

    number_block.place(x=143, y=height - 24 - 88 - 110)
    menu_label.place(x=90, y=120)

    button_dish.place(x=23, y=200)
    button_drinks.place(x=260, y=200)

    # card_dish_1.place(x=24, y=250 + 50)
    # card_dish_2.place(x=width - 24 - 217, y=250 + 50)
    card_dish_1.place(x=24, y=250 + 50)
    card_dish_2.place(x=width - 24 - 217, y=250 + 50)
    card_dish_1.place(x=24, y=250 + 50)
    card_dish_2.place(x=width - 24 - 217, y=250 + 50)

    number_block.place(x=(width - 214) // 2, y=height - 24 - 88 - 90)
    number_button_1.place(x=(width - 214 + 2 + 6) // 2, y=height - 24 - 88 - 90 + 2)
    number_button_2.place(x=(width - 90) // 2, y=height - 24 - 88 - 90 + 2)
    number_button_3.place(x=(width + 26) // 2, y=height - 24 - 88 - 90 + 2)
    number_button_4.place(x=(width + 214 - 72) // 2, y=height - 24 - 88 - 90 + 2)


def window6(event=None):
    global window_number
    window_number = 6
    clearing_w_start()
    additional_elements()
    add_arrows()

    number_block.place(x=143, y=760)
    menu_label.place(x=132, y=100)

    button_dish.place(x=23, y=150)
    button_drinks.place(x=260, y=150)

    ...


if __name__ == "__main__":
    # ===================== Логика и параметры ===================
    window_number = 1  # Номер окна

    # Кнопки для дат:
    activated_date_button = False  # Либо номер кнопки 1-5, либо никакая - False

    # Доп цвета:
    label_green_color = rgbtohex(r=109, g=191, b=102)  # светло-зеленый
    bg_peach_color = rgbtohex(r=252, g=240, b=227)  # персиковый
    fg_brown_color = rgbtohex(r=119, g=55, b=8)  # коричневый с лого
    # fg_b = fg_brown_color
    # label_green_color = fg_brown_color

    # ====================== Стартовое окно ====================== (window1)
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
    Button_start.bind("<Enter>", on_start)
    Button_start.bind("<Leave>", off_start)
    Button_start.bind("<Button-1>", change_color_start)

    # ====================== Второе окно ====================== (window2, window3, window4)
    # Переменные:
    user_selected_date = None
    user_selected_time = None
    user_selected_people_amount = 1

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
    back_button.bind("<Enter>", on_back)
    back_button.bind("<Leave>", off_back)
    back_button.bind("<Button-1>", change_color_back)

    arrow_forward_img = PhotoImage(file=Path(arrow_forward))
    arrow_forward_dark_img = PhotoImage(file=Path(arrow_forward_dark))
    arrow_forward_light_img = PhotoImage(file=Path(arrow_forward_light))

    forward_button = Button(W, image=arrow_forward_img, borderwidth=0,
                            text="ДАЛЕЕ", font=global_font, foreground=fg_w,
                            compound="center", command=next_win, bg=bg_w, activebackground=bg_w)
    forward_button.bind("<Enter>", on_forward)
    forward_button.bind("<Leave>", off_forward)
    forward_button.bind("<Button-1>", change_color_forward)

    # back_button["state"] = "disabled"
    # forward_button["state"] = "disabled"

    # Даты:
    date_label = Label(W, borderwidth=0, font=label_font, text="Выберите дату",
                       fg=label_green_color, bg=bg_peach_color)

    date_btn_img = PhotoImage(file=Path(date_button))
    date_btn_img_light = PhotoImage(file=Path(date_button_light))
    date_btn_img_dark = PhotoImage(file=Path(date_button_dark))
    date_btn_img_on = PhotoImage(file=Path(date_button_on))
    date_btn_gray = PhotoImage(file=Path(date_button_gray))

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

    date_button1.clicked = False
    date_button2.clicked = False
    date_button3.clicked = False
    date_button4.clicked = False
    date_button5.clicked = False

    date_button1.bind("<Enter>", lambda event: date_btn_on(event, date_button1))
    date_button1.bind("<Leave>", lambda event: date_btn_off(event, date_button1))
    date_button1.bind("<Button-1>", lambda event: date_btn_clicked(event, date_button1))
    date_button2.bind("<Enter>", lambda event: date_btn_on(event, date_button2))
    date_button2.bind("<Leave>", lambda event: date_btn_off(event, date_button2))
    date_button2.bind("<Button-1>", lambda event: date_btn_clicked(event, date_button2))
    date_button3.bind("<Enter>", lambda event: date_btn_on(event, date_button3))
    date_button3.bind("<Leave>", lambda event: date_btn_off(event, date_button3))
    date_button3.bind("<Button-1>", lambda event: date_btn_clicked(event, date_button3))
    date_button4.bind("<Enter>", lambda event: date_btn_on(event, date_button4))
    date_button4.bind("<Leave>", lambda event: date_btn_off(event, date_button4))
    date_button4.bind("<Button-1>", lambda event: date_btn_clicked(event, date_button4))
    date_button5.bind("<Enter>", lambda event: date_btn_on(event, date_button5))
    date_button5.bind("<Leave>", lambda event: date_btn_off(event, date_button5))
    date_button5.bind("<Button-1>", lambda event: date_btn_clicked(event, date_button5))

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

    time_button1.clicked = False
    time_button2.clicked = False
    time_button3.clicked = False
    time_button4.clicked = False
    time_button5.clicked = False
    time_button6.clicked = False
    time_button7.clicked = False
    time_button8.clicked = False
    time_button9.clicked = False
    time_button10.clicked = False
    time_button11.clicked = False
    time_button12.clicked = False

    time_button1.bind("<Enter>", lambda event: date_btn_on(event, time_button1))
    time_button1.bind("<Leave>", lambda event: date_btn_off(event, time_button1))
    time_button1.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button1))
    time_button2.bind("<Enter>", lambda event: date_btn_on(event, time_button2))
    time_button2.bind("<Leave>", lambda event: date_btn_off(event, time_button2))
    time_button2.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button2))
    time_button3.bind("<Enter>", lambda event: date_btn_on(event, time_button3))
    time_button3.bind("<Leave>", lambda event: date_btn_off(event, time_button3))
    time_button3.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button3))
    time_button4.bind("<Enter>", lambda event: date_btn_on(event, time_button4))
    time_button4.bind("<Leave>", lambda event: date_btn_off(event, time_button4))
    time_button4.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button4))
    time_button5.bind("<Enter>", lambda event: date_btn_on(event, time_button5))
    time_button5.bind("<Leave>", lambda event: date_btn_off(event, time_button5))
    time_button5.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button5))
    time_button6.bind("<Enter>", lambda event: date_btn_on(event, time_button6))
    time_button6.bind("<Leave>", lambda event: date_btn_off(event, time_button6))
    time_button6.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button6))
    time_button7.bind("<Enter>", lambda event: date_btn_on(event, time_button7))
    time_button7.bind("<Leave>", lambda event: date_btn_off(event, time_button7))
    time_button7.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button7))
    time_button8.bind("<Enter>", lambda event: date_btn_on(event, time_button8))
    time_button8.bind("<Leave>", lambda event: date_btn_off(event, time_button8))
    time_button8.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button8))
    time_button9.bind("<Enter>", lambda event: date_btn_on(event, time_button9))
    time_button9.bind("<Leave>", lambda event: date_btn_off(event, time_button9))
    time_button9.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button9))
    time_button10.bind("<Enter>", lambda event: date_btn_on(event, time_button10))
    time_button10.bind("<Leave>", lambda event: date_btn_off(event, time_button10))
    time_button10.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button10))
    time_button11.bind("<Enter>", lambda event: date_btn_on(event, time_button11))
    time_button11.bind("<Leave>", lambda event: date_btn_off(event, time_button11))
    time_button11.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button11))
    time_button12.bind("<Enter>", lambda event: date_btn_on(event, time_button12))
    time_button12.bind("<Leave>", lambda event: date_btn_off(event, time_button12))
    time_button12.bind("<Button-1>", lambda event: time_btn_clicked(event, time_button12))

    # Количество человек:
    people_label = Label(W, borderwidth=0, font=label_font, text="Выберите количество гостей",
                         fg=label_green_color, bg=bg_peach_color)

    counter_img_bg = PhotoImage(file=Path(counter_bg))
    counter_block = Label(W, image=counter_img_bg, borderwidth=0, compound="center", bg=bg_peach_color,
                          text=str(user_selected_people_amount), foreground=fg_b, font=global_font)

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

    minus_button.bind("<Enter>", minus_btn_on)
    minus_button.bind("<Leave>", minus_btn_off)
    minus_button.bind("<Button-1>", minus_btn_clicked)
    plus_button.bind("<Enter>", plus_btn_on)
    plus_button.bind("<Leave>", plus_btn_off)
    plus_button.bind("<Button-1>", plus_btn_clicked)

    minus_button["state"] = "disabled"

    # ====================== Третье окно ====================== (window5)
    # Переменные:
    user_selected_page = 1
    user_selected_type = 1  # 1 - food, 2 - drinks

    menu_label = Label(W, borderwidth=0, font=label_font, text="Выберите состав меню",
                       fg=label_green_color, bg=bg_peach_color)

    number_block = Label(W, image=counter_img_bg, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)

    button_dd = PhotoImage(file=Path(dd_button))
    button_dd_white = PhotoImage(file=Path(dd_button_white))
    button_dd_dark = PhotoImage(file=Path(dd_button_dark))
    button_fd = PhotoImage(file=Path(fd_button))
    button_fd_light = PhotoImage(file=Path(fd_button_light))
    button_fd_dark = PhotoImage(file=Path(fd_button_dark))

    button_dish = Label(W, image=button_fd, borderwidth=0, compound="center", bg=bg_peach_color,
                        text="Блюда", foreground=fg_b, font=global_font, fg=fg_b)
    button_drinks = Label(W, image=button_dd, borderwidth=0, compound="center", bg=bg_peach_color,
                          text="Напитки", foreground=fg_b, font=global_font, fg=fg_w)

    button_dish.bind('<Enter>', lambda event: button_dd_on(event, button_dish))
    button_dish.bind('<Leave>', lambda event: button_dd_off(event, button_dish))
    button_dish.bind('<Button-1>', lambda event: button_dd_clicked(event, button_dish))
    button_drinks.bind('<Enter>', lambda event: button_dd_on(event, button_drinks))
    button_drinks.bind('<Leave>', lambda event: button_dd_off(event, button_drinks))
    button_drinks.bind('<Button-1>', lambda event: button_dd_clicked(event, button_drinks))

    card_1 = PhotoImage(file=Path(card1))
    card_2 = PhotoImage(file=Path(card2))
    card_3 = PhotoImage(file=Path(card3))
    card_4 = PhotoImage(file=Path(card4))
    card_5 = PhotoImage(file=Path(card5))
    card_6 = PhotoImage(file=Path(card6))
    card_7 = PhotoImage(file=Path(card7))
    card_8 = PhotoImage(file=Path(card8))
    card_d1 = PhotoImage(file=Path(cardn1))
    card_d2 = PhotoImage(file=Path(cardn2))
    card_d3 = PhotoImage(file=Path(cardn3))
    card_d4 = PhotoImage(file=Path(cardn4))
    card_d5 = PhotoImage(file=Path(cardn5))
    card_d6 = PhotoImage(file=Path(cardn6))

    card_dish_1 = Label(W, image=card_1, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_dish_2 = Label(W, image=card_2, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_dish_3 = Label(W, image=card_3, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_dish_4 = Label(W, image=card_4, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_dish_5 = Label(W, image=card_5, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_dish_6 = Label(W, image=card_6, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_dish_7 = Label(W, image=card_7, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_dish_8 = Label(W, image=card_8, borderwidth=0, compound="center", bg=bg_peach_color,
                        foreground=fg_b, font=global_font)
    card_drink_1 = Label(W, image=card_d1, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    card_drink_2 = Label(W, image=card_d2, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    card_drink_3 = Label(W, image=card_d3, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    card_drink_4 = Label(W, image=card_d4, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    card_drink_5 = Label(W, image=card_d5, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    card_drink_6 = Label(W, image=card_d6, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    button_dish.clicked = True
    button_drinks.clicked = False

    number = PhotoImage(file=Path(number))
    number_light = PhotoImage(file=Path(number_light))
    number_dark = PhotoImage(file=Path(number_dark))

    number_button_1 = Button(W, image=number, borderwidth=0, compound="center", bg=bg_w, text="1",
                             foreground=fg_w, font=global_font, activebackground=bg_w)
    number_button_2 = Button(W, image=number, borderwidth=0, compound="center", bg=bg_w, text="2",
                             foreground=fg_w, font=global_font, activebackground=bg_w)
    number_button_3 = Button(W, image=number, borderwidth=0, compound="center", bg=bg_w, text="3",
                             foreground=fg_w, font=global_font, activebackground=bg_w)
    number_button_4 = Button(W, image=number, borderwidth=0, compound="center", bg=bg_w, text="4",
                             foreground=fg_w, font=global_font, activebackground=bg_w)

    number_button_1.bind("<Enter>", lambda event: number_button_on(event, number_button_1))
    number_button_2.bind("<Enter>", lambda event: number_button_on(event, number_button_2))
    number_button_3.bind("<Enter>", lambda event: number_button_on(event, number_button_3))
    number_button_4.bind("<Enter>", lambda event: number_button_on(event, number_button_4))
    number_button_1.bind("<Leave>", lambda event: number_button_off(event, number_button_1))
    number_button_2.bind("<Leave>", lambda event: number_button_off(event, number_button_2))
    number_button_3.bind("<Leave>", lambda event: number_button_off(event, number_button_3))
    number_button_4.bind("<Leave>", lambda event: number_button_off(event, number_button_4))
    number_button_1.bind("<Button-1>", lambda event: number_button_clicked(event, number_button_1))
    number_button_2.bind("<Button-1>", lambda event: number_button_clicked(event, number_button_2))
    number_button_3.bind("<Button-1>", lambda event: number_button_clicked(event, number_button_3))
    number_button_4.bind("<Button-1>", lambda event: number_button_clicked(event, number_button_4))



    # ====================== Вызовы окон ======================
    window1()  # Отображение элементов интерфейса первого окна

    W.mainloop()
