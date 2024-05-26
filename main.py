from tkinter import *
from tkinter.ttk import Frame
from pathlib import Path

from settings import *
import copy


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
    if back_button["state"] != "disabled":
        back_button["image"] = arrow_back_dark_img


def off_back(event=None):
    if back_button["state"] != "disabled":
        back_button["image"] = arrow_back_img


def change_color_back(event=None):
    if back_button["state"] != "disabled":
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
    if minus_button["state"] != "disabled":
        minus_button["image"] = minus_dark_img


def minus_btn_off(event):
    if minus_button["state"] != "disabled":
        minus_button["image"] = minus_img


def minus_btn_clicked(event):
    if minus_button["state"] == "disabled":
        return
    global user_selected_people_amount
    minus_button["image"] = minus_light_img
    if user_selected_people_amount > 1:
        user_selected_people_amount -= 1
    if user_selected_people_amount == 1:
        minus_button["state"] = "disabled"
    else:
        minus_button["state"] = "active"
    plus_button["image"] = plus_img
    plus_button["state"] = "active"
    counter_block["text"] = str(user_selected_people_amount)


def plus_btn_on(event):
    if plus_button["state"] != "disabled":
        plus_button["image"] = plus_dark_img


def plus_btn_off(event):
    if plus_button["state"] != "disabled":
        plus_button["image"] = plus_img


def plus_btn_clicked(event):
    if plus_button["state"] == "disabled":
        return
    global user_selected_people_amount
    plus_button["image"] = plus_light_img
    if user_selected_people_amount < 6:
        user_selected_people_amount += 1
    if user_selected_people_amount == 6:
        plus_button["state"] = "disabled"
    else:
        plus_button["state"] = "active"
    minus_button["image"] = minus_img
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
    global user_selected_page, user_selected_type, user_selected_dishes
    global user_selected_dishes_backup, user_selected_drinks

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

            user_selected_drinks = copy.deepcopy(user_selected_dishes)
            user_selected_dishes = copy.deepcopy(user_selected_dishes_backup)
            user_selected_dishes_backup = copy.deepcopy(user_selected_drinks)
        else:
            button_dish['image'] = button_dd
            button_dish['foreground'] = fg_w
            user_selected_type = 2

            user_selected_dishes_backup = copy.deepcopy(user_selected_dishes)
            user_selected_dishes = copy.deepcopy(user_selected_drinks)
        button.clicked = True

        window5()
        pages = 4
        for page in range(pages):
            try:
                btn = globals().get(f"number_button_{page + 1}")
                if page == 0:
                    btn.clicked = True
                    btn["image"] = number_img
                    btn["foreground"] = fg_w
                    user_selected_page = page + 1
                    window5(event)
                else:
                    btn["image"] = number_light_img
                    btn["foreground"] = fg_w
                    btn.clicked = False
            except Exception as e:
                pass

        if not user_selected_dishes[0][2]:
            button_buy_1["image"] = image_buy
            food_minus_button_1["state"] = "active"
            food_plus_button_1["state"] = "active"
            if user_selected_dishes[0][0] == 1:
                food_minus_button_1["state"] = "disabled"
            if user_selected_dishes[0][0] == 10:
                food_plus_button_1["state"] = "disabled"
        else:
            button_buy_1["image"] = image_check
            food_minus_button_1["state"] = "disabled"
            food_plus_button_1["state"] = "disabled"

        if not user_selected_dishes[0][3]:
            button_buy_2["image"] = image_buy
            food_minus_button_2["state"] = "active"
            food_plus_button_2["state"] = "active"
            if user_selected_dishes[0][1] == 1:
                food_minus_button_2["state"] = "disabled"
            if user_selected_dishes[0][1] == 10:
                food_plus_button_2["state"] = "disabled"
        else:
            button_buy_2["image"] = image_check
            food_minus_button_2["state"] = "disabled"
            food_plus_button_2["state"] = "disabled"


def dd_minus_btn_on(event, button):
    if button["state"] != "disabled":
        button["image"] = food_minus_dark_img


def dd_minus_btn_off(event, button):
    if button["state"] != "disabled":
        button["image"] = food_minus_img


def dd_minus_btn_clicked(event, button, side):
    if button["state"] == "disabled":
        return
    global user_selected_people_amount
    minus_button["image"] = food_minus_light_img
    product = user_selected_dishes[user_selected_page - 1][side]

    if product > 1:
        user_selected_dishes[user_selected_page - 1][side] -= 1
    if product - 1 == 1:
        button["state"] = "disabled"
    if side == 0:
        food_plus_button_1["state"] = "active"
        food_minus_button_1["image"] = food_minus_img
        counter_food_1["text"] = str(user_selected_dishes[user_selected_page - 1][side])
    else:
        food_plus_button_2["state"] = "active"
        food_minus_button_2["image"] = food_minus_img
        counter_food_2["text"] = str(user_selected_dishes[user_selected_page - 1][side])


def dd_plus_btn_on(event, button):
    if button["state"] != "disabled":
        button["image"] = food_plus_dark_img


def dd_plus_btn_off(event, button):
    if button["state"] != "disabled":
        button["image"] = food_plus_img


def dd_plus_btn_clicked(event, button, side):
    if button["state"] == "disabled":
        return
    global user_selected_people_amount
    minus_button["image"] = food_minus_light_img
    product = user_selected_dishes[user_selected_page - 1][side]

    if product < 10:
        user_selected_dishes[user_selected_page - 1][side] += 1
    if product + 1 == 10:
        button["state"] = "disabled"
    if side == 0:
        food_minus_button_1["state"] = "active"
        food_plus_button_1["image"] = food_plus_img
        counter_food_1["text"] = str(user_selected_dishes[user_selected_page - 1][side])
    else:
        food_minus_button_2["state"] = "active"
        food_plus_button_2["image"] = food_plus_img
        counter_food_2["text"] = str(user_selected_dishes[user_selected_page - 1][side])


def buy_button_on(event, button, side):
    global user_selected_dishes, user_selected_page
    if user_selected_dishes[user_selected_page - 1][side+2]:
        button["image"] = image_check_dark
    else:
        button["image"] = image_buy_dark


def buy_button_off(event, button, side):
    global user_selected_dishes, user_selected_page
    if user_selected_dishes[user_selected_page - 1][side + 2]:
        button["image"] = image_check
    else:
        button["image"] = image_buy


def buy_button_clicked(event, button, side):
    global user_selected_dishes, user_selected_page
    if user_selected_dishes[user_selected_page - 1][side + 2]:
        user_selected_dishes[user_selected_page - 1][side + 2] = False
        button["image"] = image_buy
        if side == 0:
            food_minus_button_1["state"] = "active"
            food_plus_button_1["state"] = "active"
        else:
            food_minus_button_2["state"] = "active"
            food_plus_button_2["state"] = "active"
        if side == 0:
            if user_selected_dishes[user_selected_page - 1][side] == 1:
                food_minus_button_1["state"] = "disabled"
            if user_selected_dishes[user_selected_page - 1][side] == 10:
                food_plus_button_1["state"] = "disabled"
        else:
            if user_selected_dishes[user_selected_page - 1][side] == 1:
                food_minus_button_2["state"] = "disabled"
            if user_selected_dishes[user_selected_page - 1][side] == 10:
                food_plus_button_2["state"] = "disabled"
    else:
        user_selected_dishes[user_selected_page - 1][side + 2] = True
        button["image"] = image_check
        if side == 0:
            food_minus_button_1["state"] = "disabled"
            food_plus_button_1["state"] = "disabled"
        else:
            food_minus_button_2["state"] = "disabled"
            food_plus_button_2["state"] = "disabled"
# ==============================================================


# =================== Кнопки цифры =============================
def number_button_on(event, button):
    if not button.clicked:
        button['image'] = number_light_dark_img
    else:
        button['image'] = number_dark_img
    button['foreground'] = fg_w


def number_button_off(event, button):
    if not button.clicked:
        button['image'] = number_light_img
    else:
        button['image'] = number_img
    button['foreground'] = fg_w


def number_button_clicked(event, button):
    global user_selected_page
    if button.clicked:
        return
    button.clicked = True
    pages = 4
    for page in range(pages):
        try:
            btn = globals().get(f"number_button_{page + 1}")
            if btn["text"] == button["text"]:
                button["image"] = number_img
                btn["foreground"] = fg_w
                user_selected_page = page + 1
                window5(event)
            else:
                btn["image"] = number_light_img
                btn["foreground"] = fg_w
                btn.clicked = False
        except Exception as e:
            pass
# ==============================================================


# =================== Радио батоны пожеланий ===================
def radiobutton_on(event, button):
    if button.clicked:
        button['image'] = radio_button_1
    else:
        button['image'] = radio_button_2


def radiobutton_off(event, button):
    if button.clicked:
        button['image'] = radio_button_1
    else:
        button['image'] = radio_button_0


def radiobutton_clicked(event, button):
    if not button.clicked:
        button.clicked = True
    for radio in range(5):
        try:
            btn = globals().get(f"radiobutton_{radio + 1}")
            if btn != button:
                btn.clicked = False
        except Exception as e:
            pass

    check_radios(event)


def check_radios(event):
    for radio in range(5):
        try:
            btn = globals().get(f"radiobutton_{radio + 1}")
            if btn.clicked:
                btn["image"] = radio_button_1
            else:
                btn["image"] = radio_button_0
        except Exception as e:
            pass
    if radiobutton_5.clicked:
        canvas.place(x=95, y=535)
    else:
        canvas.place(x=-300, y=-300)
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
    match window_number:
        case 5:
            clearing_w_start()
            window2()
            window3()
            window4()
        case 6:
            clearing_w_start()
            window5()
        case 7:
            clearing_w_start()
            window6()
        case 8:
            clearing_w_start()
            window7()
        case _:
            pass


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


def cards(event=None):
    global user_selected_page, user_selected_dishes, user_selected_type
    try:
        if user_selected_type == 1:
            card1 = globals().get(f"card_dish_{(user_selected_page - 1) * 2 + 1}")
            card1.place(x=24, y=250 + 50)
            card2 = globals().get(f"card_dish_{(user_selected_page - 1) * 2 + 2}")
            card2.place(x=width - 24 - 217, y=250 + 50)
        else:
            card1 = globals().get(f"card_drink_{(user_selected_page - 1) * 2 + 1}")
            card1.place(x=24, y=250 + 50)
            card2 = globals().get(f"card_drink_{(user_selected_page - 1) * 2 + 2}")
            card2.place(x=width - 24 - 217, y=250 + 50)

        if user_selected_dishes[user_selected_page - 1][2]:
            food_plus_button_1["state"] = "disabled"
            food_plus_button_2["state"] = "disabled"
        else:
            food_plus_button_1["state"] = "active"
            food_plus_button_2["state"] = "active"
        if user_selected_dishes[user_selected_page - 1][2]:
            food_minus_button_1["state"] = "disabled"
            food_minus_button_2["state"] = "disabled"
        else:
            food_minus_button_1["state"] = "active"
            food_minus_button_2["state"] = "active"

        amount1 = user_selected_dishes[user_selected_page - 1][0]
        amount2 = user_selected_dishes[user_selected_page - 1][1]

        counter_food_1["text"] = amount1
        counter_food_2["text"] = amount2

        if amount1 == 1:
            food_minus_button_1["state"] = "disabled"
        if amount2 == 1:
            food_minus_button_2["state"] = "disabled"
        if amount1 == 10:
            food_plus_button_1["state"] = "disabled"
        if amount2 == 10:
            food_plus_button_2["state"] = "disabled"

    except Exception as e:
        pass


def check_cart(event=None):
    global user_selected_page, user_selected_dishes
    if user_selected_dishes[user_selected_page - 1][2]:
        button_buy_1["image"] = image_check
    else:
        button_buy_1["image"] = image_buy
    if user_selected_dishes[user_selected_page - 1][3]:
        button_buy_2["image"] = image_check
    else:
        button_buy_2["image"] = image_buy


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

    back_button["state"] = "disabled"


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

    number_block.place(x=143, y=height - 24 - 88 - 83)
    menu_label.place(x=90, y=120)

    button_dish.place(x=23, y=200)
    button_drinks.place(x=260, y=200)

    cards(event)
    check_cart(event)

    button_buy_1.place(x=24 + 8 + 105 + 8, y=250 + 50 + 335)
    counter_food_1.place(x=24 + 8, y=250 + 50 + 335 - 8 - 36)
    food_minus_button_1.place(x=24 + 8 + 4 + 2, y=250 + 50 + 335 - 8 - 36 + 4 + 1)
    food_plus_button_1.place(x=24 + 8 + 3 + 137 + 24 + 5 - 1, y=250 + 50 + 335 - 8 - 36 + 4)

    button_buy_2.place(x=width - 32 - 88, y=250 + 50 + 335)
    counter_food_2.place(x=width - 32 - 201, y=250 + 50 + 335 - 8 - 36)
    food_minus_button_2.place(x=width - 36 - 201 + 8 + 2, y=250 + 50 + 335 - 8 - 36 + 4)
    food_plus_button_2.place(x=width - 32 - 28 - 4 - 1, y=250 + 50 + 335 - 8 - 36 + 4)

    number_button_1.place(x=(width - 214 + 2 + 6) // 2, y=height - 24 - 88 - 83 + 2)
    number_button_2.place(x=(width - 90) // 2, y=height - 24 - 88 - 83 + 2)
    number_button_3.place(x=(width + 26) // 2, y=height - 24 - 88 - 83 + 2)
    number_button_4.place(x=(width + 214 - 72) // 2, y=height - 24 - 88 - 83 + 2)

    back_button["state"] = "active"
    back_button["image"] = arrow_back_img


def window6(event=None):
    global window_number
    window_number = 6
    clearing_w_start()
    additional_elements()
    add_arrows()

    special_wish.place(x=118, y=200)
    hbday.place(x=95, y=300)
    date.place(x=95, y=350)
    wedding.place(x=95, y=400)
    not_other.place(x=95, y=450)
    other.place(x=95, y=500)

    radiobutton_1.place(x=53, y=300)
    radiobutton_2.place(x=53, y=350)
    radiobutton_3.place(x=53, y=400)
    radiobutton_4.place(x=53, y=450)
    radiobutton_5.place(x=53, y=500)

    check_radios(event)

    label_wish_1.place(x=100, y=755)
    label_wish_2.place(x=28, y=785)


def window7(event=None):
    global window_number
    window_number = 7
    clearing_w_start()
    additional_elements()
    add_arrows()

    canvas2.place(x=-300, y=-300)
    canvas3.place(x=-300, y=-300)
    canvas4.place(x=-300, y=-300)


def window8(event=None):
    global window_number
    window_number = 8
    clearing_w_start()
    additional_elements()
    add_arrows()

    canvas2.place(x=51, y=242)
    canvas3.place(x=51, y=368)
    canvas4.place(x=51, y=494)


if __name__ == "__main__":
    # ===================== Логика и параметры ===================
    window_number = 1  # Номер окна

    # Кнопки для дат:
    activated_date_button = False  # Либо номер кнопки 1-5, либо никакая - False

    # Доп цвета:
    label_green_color = rgbtohex(r=109, g=191, b=102)  # светло-зеленый
    bg_peach_color = rgbtohex(r=252, g=240, b=227)  # персиковый
    fg_brown_color = rgbtohex(r=119, g=55, b=8)  # коричневый с лого
    bg_light_gray_color = rgbtohex(r=239, g=239, b=239)  # светло-серый с карточки
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

    # amount1, amount2, confirmed1, confirmed2
    user_selected_dishes = [[1, 1, False, False], [1, 1, False, False], [1, 1, False, False], [1, 1, False, False]]
    user_selected_dishes_backup = [[1, 1, False, False], [1, 1, False, False],
                                   [1, 1, False, False], [1, 1, False, False]]
    user_selected_drinks = [[1, 1, False, False], [1, 1, False, False], [1, 1, False, False], [1, 1, False, False]]

    # Блюда:
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

    button_dish = Button(W, image=button_fd, borderwidth=0, compound="center", bg=bg_peach_color,
                         activebackground=bg_peach_color, text="Блюда", foreground=fg_b, font=global_font, fg=fg_b)
    button_drinks = Button(W, image=button_dd, borderwidth=0, compound="center", bg=bg_peach_color,
                           activebackground=bg_peach_color, text="Напитки", foreground=fg_b, font=global_font, fg=fg_w)

    button_dish.bind('<Enter>', lambda event: button_dd_on(event, button_dish))
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
    card_d7 = PhotoImage(file=Path(cardn7))
    card_d8 = PhotoImage(file=Path(cardn8))

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
    card_drink_7 = Label(W, image=card_d7, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    card_drink_8 = Label(W, image=card_d8, borderwidth=0, compound="center", bg=bg_peach_color,
                         foreground=fg_b, font=global_font)
    button_dish.clicked = True
    button_drinks.clicked = False

    image_buy = PhotoImage(file=Path(buy))
    image_buy_dark = PhotoImage(file=Path(buy_dark))
    image_buy_light = PhotoImage(file=Path(buy_light))

    image_check = PhotoImage(file=Path(check))
    image_check_dark = PhotoImage(file=Path(check_dark))
    image_check_light = PhotoImage(file=Path(check_light))

    button_buy_1 = Button(W, image=image_buy, borderwidth=0, compound="center", bg=bg_w,
                          activebackground=bg_w, foreground=fg_b, font=global_font, fg=fg_b)
    button_buy_2 = Button(W, image=image_buy, borderwidth=0, compound="center", bg=bg_w,
                          activebackground=bg_w, foreground=fg_b, font=global_font, fg=fg_b)

    button_buy_1.bind("<Enter>", lambda event: buy_button_on(event, button_buy_1, side=0))
    button_buy_1.bind("<Leave>", lambda event: buy_button_off(event, button_buy_1, side=0))
    button_buy_1.bind("<Button-1>", lambda event: buy_button_clicked(event, button_buy_1, side=0))
    button_buy_2.bind("<Enter>", lambda event: buy_button_on(event, button_buy_2, side=1))
    button_buy_2.bind("<Leave>", lambda event: buy_button_off(event, button_buy_2, side=1))
    button_buy_2.bind("<Button-1>", lambda event: buy_button_clicked(event, button_buy_2, side=1))

    image_bg_counter_food = PhotoImage(file=Path(bg_counter_food))

    counter_food_1 = Label(W, image=image_bg_counter_food, borderwidth=0, compound="center",
                           bg=bg_w, foreground=fg_b, font=global_font, text="1")
    counter_food_2 = Label(W, image=image_bg_counter_food, borderwidth=0, compound="center",
                           bg=bg_w, foreground=fg_b, font=global_font, text="1")

    food_minus_img = PhotoImage(file=Path(food_minus_normal))
    food_minus_light_img = PhotoImage(file=Path(food_minus_light))
    food_minus_dark_img = PhotoImage(file=Path(food_minus_dark))
    food_plus_img = PhotoImage(file=Path(food_plus_normal))
    food_plus_light_img = PhotoImage(file=Path(food_plus_light))
    food_plus_dark_img = PhotoImage(file=Path(food_plus_dark))

    food_minus_button_1 = Button(W, image=food_minus_img, borderwidth=0,  # , command=next_win
                                 compound="center", bg=bg_light_gray_color, activebackground=bg_light_gray_color)
    food_plus_button_1 = Button(W, image=food_plus_img, borderwidth=0,  # , command=next_win
                                compound="center", bg=bg_light_gray_color, activebackground=bg_light_gray_color)
    food_minus_button_2 = Button(W, image=food_minus_img, borderwidth=0,  # , command=next_win
                                 compound="center", bg=bg_light_gray_color, activebackground=bg_light_gray_color)
    food_plus_button_2 = Button(W, image=food_plus_img, borderwidth=0,  # , command=next_win
                                compound="center", bg=bg_light_gray_color, activebackground=bg_light_gray_color)

    food_minus_button_1.bind("<Enter>", lambda event: dd_minus_btn_on(event, food_minus_button_1))
    food_minus_button_1.bind("<Leave>", lambda event: dd_minus_btn_off(event, food_minus_button_1))
    food_minus_button_1.bind("<Button-1>", lambda event: dd_minus_btn_clicked(event, food_minus_button_1, side=0))
    food_minus_button_2.bind("<Enter>", lambda event: dd_minus_btn_on(event, food_minus_button_2))
    food_minus_button_2.bind("<Leave>", lambda event: dd_minus_btn_off(event, food_minus_button_2))
    food_minus_button_2.bind("<Button-1>", lambda event: dd_minus_btn_clicked(event, food_minus_button_2, side=1))
    food_plus_button_1.bind("<Enter>", lambda event: dd_plus_btn_on(event, food_plus_button_1))
    food_plus_button_1.bind("<Leave>", lambda event: dd_plus_btn_off(event, food_plus_button_1))
    food_plus_button_1.bind("<Button-1>", lambda event: dd_plus_btn_clicked(event, food_plus_button_1, side=0))
    food_plus_button_2.bind("<Enter>", lambda event: dd_plus_btn_on(event, food_plus_button_2))
    food_plus_button_2.bind("<Leave>", lambda event: dd_plus_btn_off(event, food_plus_button_2))
    food_plus_button_2.bind("<Button-1>", lambda event: dd_plus_btn_clicked(event, food_plus_button_2, side=1))

    food_minus_button_1["state"] = "disabled"
    food_minus_button_2["state"] = "disabled"

    number_img = PhotoImage(file=Path(number))
    number_light_img = PhotoImage(file=Path(number_light))
    number_dark_img = PhotoImage(file=Path(number_dark))
    number_light_dark_img = PhotoImage(file=Path(number_light_dark))

    number_button_1 = Button(W, image=number_img, borderwidth=0, compound="center", bg=bg_w,
                             text="1", foreground=fg_w, font=global_font, activebackground=bg_w)
    number_button_2 = Button(W, image=number_light_img, borderwidth=0, compound="center", bg=bg_w,
                             text="2", foreground=fg_w, font=global_font, activebackground=bg_w)
    number_button_3 = Button(W, image=number_light_img, borderwidth=0, compound="center", bg=bg_w,
                             text="3", foreground=fg_w, font=global_font, activebackground=bg_w)
    number_button_4 = Button(W, image=number_light_img, borderwidth=0, compound="center", bg=bg_w,
                             text="4", foreground=fg_w, font=global_font, activebackground=bg_w)
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

    number_button_1.clicked = True
    number_button_2.clicked = False
    number_button_3.clicked = False
    number_button_4.clicked = False

    # ==================== Четвертое окно ===================== (window6)
    # Переменные:
    user_selected_preferences = None  # default None/3

    special_wish = Label(W, borderwidth=0, font=label_font, text="Особые пожелания",
                         fg=label_green_color, bg=bg_peach_color)
    hbday = Label(W, borderwidth=0, font=global_font, text="Столик на день рождения",
                  fg=label_green_color, bg=bg_peach_color)
    date = Label(W, borderwidth=0, font=global_font, text="Столик для свидания",
                 fg=label_green_color, bg=bg_peach_color)
    wedding = Label(W, borderwidth=0, font=global_font, text="Столик на свадьбу",
                    fg=label_green_color, bg=bg_peach_color)
    not_other = Label(W, borderwidth=0, font=global_font, text="Пожеланий нет",
                      fg=label_green_color, bg=bg_peach_color)
    other = Label(W, borderwidth=0, font=global_font, text="Другое",
                  fg=label_green_color, bg=bg_peach_color)

    radio_button_1 = PhotoImage(file=Path(radiobutton_0))  # с точкой
    radio_button_0 = PhotoImage(file=Path(radiobutton_1))  # пустая
    radio_button_2 = PhotoImage(file=Path(radiobutton_2))  # серая пустая
    input_field = PhotoImage(file=Path(inputfield))

    radiobutton_1 = Button(W, image=radio_button_0, borderwidth=0, compound="center", bg=bg_peach_color,  # hbday
                           foreground=fg_w, font=global_font, activebackground=bg_peach_color)
    radiobutton_2 = Button(W, image=radio_button_0, borderwidth=0, compound="center", bg=bg_peach_color,  # date
                           foreground=fg_w, font=global_font, activebackground=bg_peach_color)
    radiobutton_3 = Button(W, image=radio_button_0, borderwidth=0, compound="center", bg=bg_peach_color,  # wedding
                           foreground=fg_w, font=global_font, activebackground=bg_peach_color)
    radiobutton_4 = Button(W, image=radio_button_0, borderwidth=0, compound="center", bg=bg_peach_color,  # not_other
                           foreground=fg_w, font=global_font, activebackground=bg_peach_color)
    radiobutton_5 = Button(W, image=radio_button_0, borderwidth=0, compound="center", bg=bg_peach_color,  # _other
                           foreground=fg_w, font=global_font, activebackground=bg_peach_color)

    radiobutton_1.clicked = False
    radiobutton_2.clicked = False
    radiobutton_3.clicked = False
    radiobutton_4.clicked = False
    radiobutton_5.clicked = False

    radiobutton_1.bind("<Enter>", lambda event: radiobutton_on(event, radiobutton_1))
    radiobutton_1.bind("<Leave>", lambda event: radiobutton_off(event, radiobutton_1))
    radiobutton_1.bind("<Button-1>", lambda event: radiobutton_clicked(event, radiobutton_1))
    radiobutton_2.bind("<Enter>", lambda event: radiobutton_on(event, radiobutton_2))
    radiobutton_2.bind("<Leave>", lambda event: radiobutton_off(event, radiobutton_2))
    radiobutton_2.bind("<Button-1>", lambda event: radiobutton_clicked(event, radiobutton_2))
    radiobutton_3.bind("<Enter>", lambda event: radiobutton_on(event, radiobutton_3))
    radiobutton_3.bind("<Leave>", lambda event: radiobutton_off(event, radiobutton_3))
    radiobutton_3.bind("<Button-1>", lambda event: radiobutton_clicked(event, radiobutton_3))
    radiobutton_4.bind("<Enter>", lambda event: radiobutton_on(event, radiobutton_4))
    radiobutton_4.bind("<Leave>", lambda event: radiobutton_off(event, radiobutton_4))
    radiobutton_4.bind("<Button-1>", lambda event: radiobutton_clicked(event, radiobutton_4))
    radiobutton_5.bind("<Enter>", lambda event: radiobutton_on(event, radiobutton_5))
    radiobutton_5.bind("<Leave>", lambda event: radiobutton_off(event, radiobutton_5))
    radiobutton_5.bind("<Button-1>", lambda event: radiobutton_clicked(event, radiobutton_5))

    # field_wish = Entry(W, borderwidth=0, bg=bg_w, foreground=fg_b, font=global_font)
    # label_field_wish = Label(W, image=input_field, borderwidth=0, compound="center", bg=bg_peach_color,
    #                          font=global_font)

    label_wish_1 = Label(W, borderwidth=0, font=global_font, text="При выборе особого случая будет",
                         fg=label_green_color, bg=bg_peach_color)
    label_wish_2 = Label(W, borderwidth=0, font=global_font, text="предоставлена скидка 15% и комплимент от заведения",
                         fg=label_green_color, bg=bg_peach_color)

    canvas = Canvas(W, width=296, height=51, background=bg_peach_color, borderwidth=0)
    canvas.pack()
    label_field_wish = Label(W, bg=bg_peach_color, image=input_field)
    canvas.create_window(148, 25, window=label_field_wish, width=306, height=60)
    field_wish = Entry(W, borderwidth=0, font=global_font2)
    canvas.create_window(148, 25, window=field_wish, width=280, height=45)
    canvas.place(x=-300, y=-300)

    # ====================== Пятое окно ======================= (window7)
    entry_image = PhotoImage(file=Path(inputfield2))

    canvas2 = Canvas(W, width=400, height=52, background=bg_peach_color, borderwidth=0)
    canvas2.pack()
    fio_label = Label(W, bg=bg_peach_color, image=entry_image)
    canvas2.create_window(200, 26, window=fio_label, width=306, height=60)
    fio_entry = Entry(W, borderwidth=0, font=global_font2)
    canvas2.create_window(200, 26, window=fio_entry, width=280, height=45)
    canvas2.place(x=-300, y=-300)

    canvas3 = Canvas(W, width=400, height=52, background=bg_peach_color, borderwidth=0)
    canvas3.pack()
    fio_label = Label(W, bg=bg_peach_color, image=entry_image)
    canvas3.create_window(200, 26, window=fio_label, width=306, height=60)
    fio_entry = Entry(W, borderwidth=0, font=global_font2)
    canvas3.create_window(200, 26, window=fio_entry, width=280, height=45)
    canvas3.place(x=-300, y=-300)

    canvas4 = Canvas(W, width=296, height=52, background=bg_peach_color, borderwidth=0)
    canvas4.pack()
    fio_label = Label(W, bg=bg_peach_color, image=entry_image)
    canvas4.create_window(200, 26, window=fio_label, width=306, height=60)
    fio_entry = Entry(W, borderwidth=0, font=global_font2)
    canvas4.create_window(200, 26, window=fio_entry, width=280, height=45)
    canvas4.place(x=-300, y=-300)

    # ===================== Шестое окно ======================= (window8)



    # ====================== Вызовы окон ======================
    window1()  # Отображение элементов интерфейса первого окна

    W.mainloop()
