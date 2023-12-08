from tkinter import *
from tkinter import ttk  # Импортировать модуль ttk для Progressbar

# функция для табулирования функции
def tabulate_function():
    # Очистить список перед табуляцией функции
    listbox.delete(0, END)

    # Получить значение шага и диапазон параметра
    шаг = 0.01
    начало = 0.01
    конец = 0.9

    # Вычислить количество итераций для табуляции
    итерации = int((конец - начало) / шаг) + 1

    # Отобразить формулу функции
    label_function_formula.config(text="y = 2 * x + 0.33")

    # Отобразить заголовки таблицы
    listbox.insert(END, "    x         |         y")

    # Табулировать функцию и добавить результаты в список
    for i in range(итерации):
        x = начало + i * шаг
        y = 2 * x + 0.33
        result = f"   {x:.2f}              {y:.2f}"
        listbox.insert(END, result)

# создать графический интерфейс
root = Tk()
root.title("Расчет функции")

# создать метку для отображения формулы
label_function_formula = Label(root, text="")
label_function_formula.pack()

# создать кнопку для табуляции функции
tabulate_button = Button(root, text="Расчет", command=tabulate_function)
tabulate_button.pack()

# создать список для отображения результатов табуляции
listbox = Listbox(root)
listbox.pack()

# запустить графический интерфейс
root.mainloop()