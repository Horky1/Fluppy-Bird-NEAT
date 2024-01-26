from tkinter import *
import pygame
from tkinter import *
import webbrowser
import configparser
from flappy_bird import run
import flappy_bird

def start_game_processes():
    # Функція, яка виконується при натисканні кнопки "Старт"
    window.withdraw()  # Приховати вікно меню
    run('config-feedforward.txt')
    window.deiconify()  # Показати вікно меню після завершення гри

# Розміри вікна Tk
WIN_WIDTH = 700
WIN_HEIGHT = 860

# Створення вікна програми
window = Tk()
window.title("Меню")
window.config(bg="gray")

# Отримання розмірів екрану
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Розташування вікна Tk по центру екрану
x = (screen_width - WIN_WIDTH) // 2
y = (screen_height - WIN_HEIGHT) // 2

# Встановлення розміру і розташування вікна Tk
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{x}+{y}")

# Створення кнопки "Старт"
start_button = Button(window, text="Старт", command=start_game_processes)
start_button.config(width=100, height=5)
start_button.config(bg="green")
start_button.pack()

def save_config():
    # Отримання значення з текстового поля
    new_pop_size = pop_size_entry.get()
    # Завантаження конфігураційного файлу
    config = configparser.RawConfigParser()
    config.read('config-feedforward.txt')
    # Зміна значення pop_size
    config.set('NEAT', 'pop_size', new_pop_size)
    # Запис зміненого вмісту назад у файл
    with open('config-feedforward.txt', 'w') as config_file:
        config.write(config_file)


# Створення лейблу для відображення кількості юнітів
units_label = Label(window, text="Кількість юнітів:")
units_label.pack()
maxgen_label = Label(window, text="Кількість генерацій:")
maxgen_label.pack()
maxschore_label = Label(window, text="Максимальний рахунок:")
maxgen_label.pack()
# Створення текстового поля для введення нового значення pop_size
pop_size_entry = Entry(window)
maxgen_entry = Entry(window)
maxschore_entry = Entry(window)
# Створення кнопки "Зберегти"
save_button = Button(window, text="Зберегти зміни", command=save_config)
save_button.config(width=100, height=5)
save_button.config(bg="blue")
# Функція, яка виконується при натисканні кнопки "Відкрити документ"
def open_document():
    webbrowser.open('output.txt')

# Створення кнопки "Відкрити документ"
open_button = Button(window, text="Відкрити файл із результатами", command=open_document)
open_button.config(width=100, height=5)
open_button.config(bg="orange")
open_button.pack()

def close_application():
    window.destroy()

# Створення кнопки "Закрити"
close_button = Button(window, text="Закрити програму", command=close_application)
close_button.config(width=20, height=5)
close_button.config(bg="red")
close_button.pack()

# Розміщення елементів на вікні
units_label.place(relx=0.2, rely=0.25, anchor=CENTER)
pop_size_entry.place(relx=0.2, rely=0.29, anchor=CENTER)
save_button.place(relx=0.5, rely=0.4, anchor=CENTER)
open_button.place(relx=0.5, rely=0.8, anchor=CENTER)
start_button.place(relx=0.5, rely=0.1, anchor=CENTER)
maxgen_label.place(relx=0.45, rely=0.25, anchor=CENTER)
maxgen_entry.place(relx=0.45, rely=0.29, anchor=CENTER)
maxschore_label.place(relx=0.7, rely=0.25, anchor=CENTER)
maxschore_entry.place(relx=0.7, rely=0.29, anchor=CENTER)
open_button.place(relx=0.5, rely=0.55, anchor=CENTER)
close_button.place(relx=0.5, rely=0.7, anchor=CENTER)
# Запуск головного циклу програми
window.mainloop()
