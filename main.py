from tkinter import *
from tkinter import ttk


def getInfo():
    # Открытие текстового файла для записи
    file = open('info.txt', 'w', encoding='utf-8')

    # Запись информации в файл построчно

    # Записываем имя в файл
    file.write('Имя: ' + nameT.get() + '\n')

    # Записываем фамилию в файл
    file.write('Фамилия: ' + lastNameT.get() + '\n')

    # Проверяем значение переменной пола и записываем соответствующую информацию в файл
    if polvar.get() == 'm':
        file.write('Пол: мужской\n')
    elif polvar.get() == 'w':
        file.write('Пол: женский\n')
    else:
        file.write('Пол не указан\n')

    # Записываем выбранные предметы в файл
    file.write('Любимые предметы:\n')

    # Проверяем состояние переменных var1, var2 и var3 и записываем выбранные предметы в файл
    if var1.get() == 1:
        file.write(' - математика\n')
    if var2.get() == 1:
        file.write(' - английский язык\n')
    if var3.get() == 1:
        file.write(' - информационные технологии\n')

    # Закрытие файла
    file.close()


# Создание главного окна
window = Tk()
window.title('Регистрация')

# Создание и настройка меток для полей ввода
name = Label(window, text='Имя', width=20, height=1, fg='blue', font='arial 18')
lastName = Label(window, text='Фамилия', width=20, height=1, fg='blue', font='arial 18')
pol = Label(window, text='Пол', width=20, height=1, fg='blue', font='arial 18')
likePr = Label(window, text='Любимые предметы', width=20, height=1, fg='blue', font='arial 18')

# Создание и настройка полей ввода
nameT = Entry(window, width=30, font='arial 14')
lastNameT = Entry(window, width=30, font='arial 14')

# Создание и настройка переменной для выбора пола
polvar = StringVar()
polvar.set(' ')

# Создание и настройка переключателей для выбора пола
radio1 = Radiobutton(window, text='мужской', variable=polvar, value='m')
radio2 = Radiobutton(window, text='женский', variable=polvar, value='w')

# Создание и настройка переменных для выбора предметов
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# Создание и настройка флажков для выбора предметов
check1 = Checkbutton(window, text='математика', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(window, text='английский язык', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(window, text='информационные технологии', variable=var3, onvalue=1, offvalue=0)

# Создание и настройка кнопки для отправки данных
btn = Button(window, text='Принять', width=25, height=5, fg='blue', font='arial 14', command=getInfo)

# Размещение элементов на главном окне
name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()

# Запуск главного цикла обработки событий
window.mainloop()