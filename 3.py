from tkinter import *
from tkinter import ttk  # Импорт необходимых модулей

window = Tk()  # Создание главного окна
window.geometry("300x80")  # Установка размеров окна

value_var = IntVar()  # Создание переменной для хранения значения прогрессбара
pb = ttk.Progressbar(window, orient="horizontal", length=280, variable=value_var, mode='determinate')  # Создание горизонтального прогрессбара
pb.pack()  # Размещение прогрессбара в окне

# Функция для запуска прогрессбара
def start():
    pb.start(100)

# Функция для остановки прогрессбара
def stop():
    pb.stop()

start_btn = ttk.Button(text="Start", command=start)  # Создание кнопки "Start" и привязка к функции start
start_btn.pack()  # Размещение кнопки "Start" в окне
stop_btn = ttk.Button(text="Stop", command=stop)  # Создание кнопки "Stop" и привязка к функции stop
stop_btn.pack()  # Размещение кнопки "Stop" в окне

window.mainloop()  # Запуск главного цикла обработки событий