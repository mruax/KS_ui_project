from tkinter import *
from tkinter.ttk import Frame
from pathlib import Path

from settings import *


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


def window1(e=None):
    """
    Размещает элементы интерфейса стартового окна.

    :return: None
    """
    bg_start.place(x=0, y=0)
    Button_start.place(x=130, y=600, width=243, height=54)


def window2(e=None):
    """
    Размещает элементы интерфейса второго окна.

    :param e: None
    :return: None
    """
    # clearing_w_start()
    background_label.place(x=0, y=0)
    arrows_block.place(x=24, y=height-24-88)


if __name__ == "__main__":
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
                          text="ЗАБРОНИРОВАТЬ СТОЛ", compound="center", fg=fg_w, font=font1,
                          command=window2)
    Button_start.bind('<Enter>', on_start)
    Button_start.bind('<Leave>', off_start)
    Button_start.bind('<Button-1>', change_color_start)

    # ====================== Второе окно ======================
    solid_background = PhotoImage(file=Path(solid_bg))
    background_label = Label(W, image=solid_background, borderwidth=0)

    arrows_block_image = PhotoImage(file=Path(arrows_block_bg))
    arrows_block = Label(W, image=arrows_block_image, borderwidth=0)

    # ====================== Вызовы окон ======================
    window1()  # Отображение элементов интерфейса первого окна

    W.mainloop()
