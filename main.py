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
    :return: rgb format string
    """
    return f'#{r:02x}{g:02x}{b:02x}'


def on_start(e=None):
    """
    Изменение стартовой кнопки при наведении курсора мыши.

    :param e: None
    :return: None
    """
    Button_start['image'] = b_start_dark
    # Button_start['fg'] = fg_b


def off_start(e=None):
    """
    Изменение стартовой кнопки при выходе курсора из зоны кнопки.

    :param e: None
    :return: None
    """
    Button_start['image'] = b_start
    # Button_start['fg'] = fg_w


def change_color_start(e=None):
    """
    Изменяет стартовую кнопку при нажатии.

    :param e: None
    :return: None
    """
    Button_start['image'] = b_start_light


def clearing_w_start():
    """
    Удаление всех виджетов из окна.

    :return: None
    """
    for widget in W.winfo_children():
        widget.destroy()


def back_win():
    """
    Функция для открытия предыдущего окна в зависимости от window_number.

    :return: None
    """
    print(123)


def next_win():
    """
    Функция для открытия следующего окна в зависимости от window_number.

    :return: None
    """
    print(321)


def window1(e=None):
    """
    Размещает элементы интерфейса стартового окна.

    :return: None
    """
    global window_number
    window_number = 1
    bg_start.place(x=0, y=0)
    Button_start.place(x=130, y=600, width=243, height=54)


def window2(e=None):
    """
    Размещает элементы интерфейса второго окна.

    :param e: None
    :return: None
    """
    # clearing_w_start()
    global window_number
    window_number = 2
    background_label.place(x=0, y=0)

    date_label.place(x=24, y=124)
    time_label.place(x=24, y=324)

    arrows_block.place(x=24, y=height - 24 - 88)
    back_button.place(x=24 + 138, y=height - 12 - 79)
    forward_button.place(x=24 + 138 + 79 + 20, y=height - 12 - 79)


if __name__ == "__main__":
    # Номер окна
    window_number = 1

    # Доп цвета
    label_green_color = rgbtohex(r=109, g=191, b=102)
    bg_color = rgbtohex(r=252, g=240, b=227)

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
                          fg=fg_w, font=global_font,
                          command=window2)
    Button_start.bind('<Enter>', on_start)
    Button_start.bind('<Leave>', off_start)
    Button_start.bind('<Button-1>', change_color_start)

    # ====================== Второе окно ======================
    solid_background = PhotoImage(file=Path(solid_bg))
    background_label = Label(W, image=solid_background, borderwidth=0)

    arrows_block_image = PhotoImage(file=Path(arrows_block_bg))
    arrows_block = Label(W, image=arrows_block_image, borderwidth=0)

    date_label = Label(W, borderwidth=0, font=label_font, text="Выберите дату:",
                       fg=label_green_color, bg=bg_color)
    time_label = Label(W, borderwidth=0, font=label_font, text="Выберите время:",
                       fg=label_green_color, bg=bg_color)

    arrow_back_img = PhotoImage(file=Path(arrow_back))
    arrow_back_dark_img = PhotoImage(file=Path(arrow_back_dark))
    arrow_back_light_img = PhotoImage(file=Path(arrow_back_light))

    back_button = Button(W, image=arrow_back_img, borderwidth=0,
                         compound="center", command=back_win)

    arrow_forward_img = PhotoImage(file=Path(arrow_forward))
    arrow_forward_dark_img = PhotoImage(file=Path(arrow_forward_dark))
    arrow_forward_light_img = PhotoImage(file=Path(arrow_forward_light))

    forward_button = Button(W, image=arrow_forward_img, borderwidth=0,
                            compound="center", command=next_win)

    # ====================== Вызовы окон ======================
    window1()  # Отображение элементов интерфейса первого окна

    W.mainloop()
