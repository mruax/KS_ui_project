from tkinter import *


# Функции для изменения вида кнопки
def on_start(e):
    Button_start['image'] = b_start_light
    Button_start['fg'] = fg_b


def off_start(e):
    Button_start['image'] = b_start
    Button_start['fg'] = fg_w


def change_color_start(e):
    Button_start['image'] = b_start


# Функция для очистки стартового окна, переход к окну 2
def clearing_w_start():
    # Удаление всех виджетов из окна
    for widget in W.winfo_children():
        widget.destroy()


def w_2(e):
    # Параметры для окна 2
    W.title("БРОНИРОВАНИЕ")
    image_2 = PhotoImage(file='bg_2.png')
    bg_2 = Label(W, image=image_2, borderwidth=0)
    bg_2.place(x=0, y=0)



if __name__ == "__main__":
    # Заготовки для шрифтов и цветов
    font1 = ('Aptos', '14')
    fg_w = 'white'
    fg_b = 'black'

    # Стартовое окно
    # Создание окна (параметры + фон)
    W = Tk()
    W.geometry("502x932")
    W.title("ХМЕЛИ СУНЕЛИ")
    W.resizable(False, False)
    image_start = PhotoImage(file='bg_start.png')
    bg_start = Label(W, image=image_start, borderwidth=0)
    bg_start.place(x=0, y=0)

    # Кнопка на стартовом окне
    # Изображения для разных фаз кнопки
    b_start = PhotoImage(file='b_start.png')
    b_start_light = PhotoImage(file='b_start_light.png')
    # Создание кнопки (параметры)
    Button_start = Button(W, image=b_start, borderwidth=0,
                          text="ЗАБРОНИРОВАТЬ", compound="center", fg=fg_w, font=font1,
                          command=clearing_w_start)
    Button_start.place(x=130, y=600, width=243, height=54)

    Button_start.bind('<Enter>', on_start)
    Button_start.bind('<Leave>', off_start)
    Button_start.bind('<Button-1>', change_color_start)

    W.mainloop()
