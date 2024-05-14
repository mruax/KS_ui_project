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


def window1():
    """
    Стартовое окно.

    :param e:
    :return: None
    """
    bg_start.place(x=0, y=0)
    Button_start.place(x=130, y=600, width=243, height=54)


def window2(e):
    """
    Второе окно.

    :param e:
    :return: None
    """
    bg_2.place(x=0, y=0)


if __name__ == "__main__":
    # ====================== Стартовое окно ======================
    W = Tk()
    W.geometry("502x932")
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
                          command=clearing_w_start)
    Button_start.bind('<Enter>', on_start)
    Button_start.bind('<Leave>', off_start)
    Button_start.bind('<Button-1>', change_color_start)

    window1()  # Отображение элементов интерфейса первого окна

    # ====================== Второе окно ======================
    image_2 = PhotoImage(file=Path(solid_bg))
    bg_2 = Label(W, image=image_2, borderwidth=0)

    W.mainloop()
