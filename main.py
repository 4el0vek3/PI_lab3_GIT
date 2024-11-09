from tkinter import *
from tkinter import ttk

marc_car = []
model_car = []
year_of_release = []
color_car = []
price_car = []
fari_car = []
door_car = []
power_car = []

marc = ""
model = ""
year = ""
color = "1"
price = ""
fari = ""
door = ""
power = ""

carina = open('carina.txt', 'r')
j = carina.readline()
file = j.split('&')
if j != "":
    if len(file[0].split()) == 1:
        marc_car = [file[0]]
        model_car = [file[1]]
        year_of_release = [file[2]]
        color_car = [file[3]]
        price_car = [file[4]]
        fari_car = [file[5]]
        door_car = [file[6]]
        power_car = [file[7]]
    else:
        marc_car = file[0].split(' ; ')
        model_car = file[1].split(' ; ')
        year_of_release = file[2].split(' ; ')
        color_car = file[3].split(' ; ')
        price_car = file[4].split(' ; ')
        fari_car = file[5].split(' ; ')
        door_car = file[6].split(' ; ')
        power_car = file[7].split(' ; ')
vegitables = []
for i in range(len(marc_car)):
    veg = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]), (fari_car[i]),
           (door_car[i]), (power_car[i])]
    vegitables.append(veg)


def add():
    def dismis(add_open):
        if len(marc_car) > len(price_car):
            ib = len(door_car)
            marc_car.pop(-1)
            if len(model_car) > ib:
                model_car.pop(-1)
            if len(year_of_release) > ib:
                year_of_release.pop(-1)
            if len(color_car) > ib:
                color_car.pop(-1)
            if len(price_car) > ib:
                price_car.pop(-1)
            if len(power_car) > ib:
                power_car.pop(-1)
        add_open.grab_release()
        add_open.destroy()

    def far_and_doorgo():
        def dismisi(far_and_door):
            if len(marc_car) > len(door_car):
                ib = len(door_car)
                marc_car.pop(-1)
                if len(model_car) > ib:
                    model_car.pop(-1)
                if len(year_of_release) > ib:
                    year_of_release.pop(-1)
                if len(color_car) > ib:
                    color_car.pop(-1)
                if len(price_car) > ib:
                    price_car.pop(-1)
                if len(fari_car) > ib:
                    fari_car.pop(-1)
                if len(door_car) > ib:
                    door.car.pop(-1)
                if len(power_car) > ib:
                    power_car.pop(-1)
            else:
                idd = len(marc_car)
                fj = [(marc_car[idd - 1], model_car[idd - 1], year_of_release[idd - 1], color_car[idd - 1],
                       price_car[idd - 1], fari_car[idd - 1], door_car[idd - 1], power_car[idd - 1])]
                for component in fj:
                    text1.insert('', END, idd, values=component)
                carina = open('carina.txt', 'w')
                if len(marc_car) != 1:
                    marc_car_save = ' ; '.join(marc_car) + '&'
                    model_car_save = ' ; '.join(model_car) + '&'
                    year_of_release_save = ' ; '.join(year_of_release) + '&'
                    color_car_save = ' ; '.join(color_car) + '&'
                    price_car_save = ' ; '.join(price_car) + '&'
                    fari_car_save = ' ; '.join(fari_car) + "&"
                    door_car_save = ' ; '.join(door_car) + "&"
                    power_car_save = ' ; '.join(power_car)
                else:
                    marc_car_save = ''.join(marc_car) + '&'
                    model_car_save = ''.join(model_car) + '&'
                    year_of_release_save = ''.join(year_of_release) + '&'
                    color_car_save = ''.join(color_car) + '&'
                    price_car_save = ''.join(price_car) + '&'
                    fari_car_save = ''.join(fari_car) + "&"
                    door_car_save = ''.join(door_car) + "&"
                    power_car_save = ''.join(power_car)

                carina.writelines(marc_car_save)
                carina.writelines(model_car_save)
                carina.writelines(year_of_release_save)
                carina.writelines(color_car_save)
                carina.writelines(price_car_save)
                carina.writelines(fari_car_save)
                carina.writelines(door_car_save)
                carina.writelines(power_car_save)
                carina.close()
                far_and_door.grab_release()
                far_and_door.destroy()

        def opendoor():
            door = "Открыты"
            door_car.append(door)
            dismisi(far_and_door)

        def notopendoor():
            door = "Закрыты"
            door_car.append(door)
            dismisi(far_and_door)

        def working():
            fari = "Включены"
            fari_car.append(fari)
            far_and_door.title("Состояние дверей")
            truebut["text"] = "Открыты"
            falsebut["text"] = "Закрыты"
            flab["text"] = "Состояние дверей"
            truebut["command"] = opendoor
            falsebut["command"] = notopendoor

        def notworking():
            fari = "Выключены"
            fari_car.append(fari)
            far_and_door.title("Состояние дверей")
            truebut["text"] = "Открыты"
            falsebut["text"] = "Закрыты"
            flab["text"] = "Состояние дверей"
            truebut["command"] = opendoor
            falsebut["command"] = notopendoor

        dismis(add_open)
        far_and_door = Toplevel()
        far_and_door.title("Состояние фар")
        far_and_door.geometry("250x130")
        far_and_door.protocol("WM_DELETE_WINDOW", lambda: dismisi(far_and_door))
        flab = Label(far_and_door, text="Состояние фар")
        truebut = Button(far_and_door, width=14, height=2, text='Включены', command=working)
        falsebut = Button(far_and_door, width=14, height=2, text='Выключены', command=notworking)
        flab.pack(side=TOP, pady=4)
        truebut.pack(side=TOP, pady=4)
        falsebut.pack(side=TOP, pady=4)
        far_and_door.grab_set()

    def colorgo1():
        color = "Жёлтый"
        color_car.append(color)
        far_and_doorgo()

    def colorgo2():
        color = "Красный"
        color_car.append(color)
        far_and_doorgo()

    def colorgo3():
        color = "Синий"
        color_car.append(color)
        far_and_doorgo()

    def colorgo4():
        color = "Зелёный"
        color_car.append(color)
        far_and_doorgo()

    def colorgo5():
        color = "Белый"
        color_car.append(color)
        far_and_doorgo()

    def colorgo6():
        color = "Чёрый"
        color_car.append(color)
        far_and_doorgo()

    def colorgo7():
        color = "Серый"
        color_car.append(color)
        far_and_doorgo()

    def colorgo8():
        color = "Серебряный"
        color_car.append(color)
        far_and_doorgo()

    def colorgo9():
        color = "Коричневый"
        color_car.append(color)
        far_and_doorgo()

    def colorgo10():
        color = "Оранжевый"
        color_car.append(color)
        far_and_doorgo()

    def colorgo11():
        color = "Фиолетовый"
        color_car.append(color)
        far_and_doorgo()

    def yeargo():
        try:
            year = inputing.get()
            a = int(year)
            if a < 1885 or a > 2024:
                raise ValueError
            year_of_release.append(year)
            add_open.title("Цвет")
            add_open.geometry("300x300")
            label_add["text"] = ""
            inputing.delete(0, END)
            button_add.pack_forget()
            label_add.pack_forget()
            inputing.pack_forget()
            f1 = Frame(add_open)
            f2 = Frame(add_open)
            f3 = Frame(add_open)
            f4 = Frame(add_open)
            f5 = Frame(add_open)

            b10 = Button(f1, width=9, height=4, bg='yellow', text='Жёлтый', command=colorgo1)
            b11 = Button(f1, width=9, height=4, bg='red', text='Красный', command=colorgo2)
            b12 = Button(f1, width=9, height=4, bg='blue', text='Синий', command=colorgo3)
            b13 = Button(f1, width=9, height=4, bg='green', text='Зеленый', command=colorgo4)
            b14 = Button(f2, width=9, height=4, bg='white', text='Белый', command=colorgo5)
            b15 = Button(f2, width=9, height=4, bg='black', text='Черный', foreground='white', command=colorgo6)
            b16 = Button(f2, width=9, height=4, bg='grey', text='Серый', command=colorgo7)
            b17 = Button(f2, width=9, height=4, bg='silver', text='Серебряный', command=colorgo8)
            b18 = Button(f3, width=9, height=4, bg='brown', text='Коричневый', command=colorgo9)
            b19 = Button(f3, width=9, height=4, bg='orange', text='Оранжевый', command=colorgo10)
            b20 = Button(f3, width=9, height=4, bg='violet', text='Фиолетовый', command=colorgo11)
            # b21 = Button(f3, width=9, height=4, bg='', text='')
            # b22 = Button(f4, width=9, height=4, bg='', text='')
            # b23 = Button(f4, width=9, height=4, bg='', text='')
            # b24 = Button(f4, width=9, height=4, bg='', text='')
            # b25 = Button(f4, width=9, height=4, bg='', text='')
            # b26 = Button(f5, width=9, height=4, bg='', text='')
            # b27 = Button(f5, width=9, height=4, bg='', text='')
            # b28 = Button(f5, width=9, height=4, bg='', text='')
            # b29 = Button(f5, width=9, height=4, bg='', text='')

            f1.pack()
            f2.pack()
            f3.pack()
            f4.pack()
            f5.pack()

            b10.pack(side=LEFT)
            b11.pack(side=LEFT)
            b12.pack(side=LEFT)
            b13.pack(side=LEFT)
            b14.pack(side=LEFT)
            b15.pack(side=LEFT)
            b16.pack(side=LEFT)
            b17.pack(side=LEFT)
            b18.pack(side=LEFT)
            b19.pack(side=LEFT)
            b20.pack(side=LEFT)
            # b21.pack(side=LEFT)
            # b22.pack(side=LEFT)
            # b23.pack(side=LEFT)
            # b24.pack(side=LEFT)
            # b25.pack(side=LEFT)
            # b26.pack(side=LEFT)
            # b27.pack(side=LEFT)
            # b28.pack(side=LEFT)
            # b29.pack(side=LEFT)
        except:
            label_add["foreground"] = "#B71C1C"


    def powergo():
        try:
            label_add["foreground"] = "#000000"
            power = inputing.get()
            a = int(power)
            if a < 1 or a > 2000:
                raise ValueError
            power_car.append(power)
            add_open.title("Год")
            label_add["text"] = "Введите год"
            inputing.delete(0, END)
            button_add["command"] = yeargo
        except:
            label_add["foreground"] = "#B71C1C"
    def pricego():
        try:
            label_add["foreground"] = "#000000"
            price = inputing.get()
            a = int(price)
            if a < 1:
                raise ValueError
            price_car.append(price)
            add_open.title("Мощность")
            label_add["text"] = "Введите мощность"
            inputing.delete(0, END)
            button_add["command"] = powergo
        except:
            label_add["foreground"] = "#B71C1C"

    def modelgo():
        model = inputing.get()
        model_car.append(model)
        add_open.title("Цена")
        label_add["text"] = "Введите цену"
        inputing.delete(0, END)
        button_add["command"] = pricego

    def marcago():
        marc = inputing.get()
        marc_car.append(marc)
        add_open.title("Модель")
        label_add["text"] = "Введите модель"
        inputing.delete(0, END)
        button_add["command"] = modelgo

    add_open = Toplevel()
    add_open.title("Марка")
    add_open.geometry("250x100")
    add_open.protocol("WM_DELETE_WINDOW", lambda: dismis(add_open))
    inputing = Entry(add_open, width=40)
    label_add = Label(add_open, text="Введите марку")
    button_add = Button(add_open, width=14, height=2, text='Далее')
    button_add["command"] = marcago
    label_add.pack()
    label['text'] = ''
    inputing.pack()
    button_add.pack()
    add_open.grab_set()


def delite():
    if str(text1.selection()) == "()":
        label["foreground"] = "#B71C1C"
        label["text"] = "Выберите строку!"
    else:
        carina = open('carina.txt', 'w')
        po = str(text1.selection())
        po = int(po[2:-3])
        sel = text1.selection()
        variant = []
        yol = po
        marc_car.pop(po - 1)
        model_car.pop(po - 1)
        year_of_release.pop(po - 1)
        color_car.pop(po - 1)
        price_car.pop(po - 1)
        fari_car.pop(po - 1)
        door_car.pop(po - 1)
        power_car.pop(po - 1)
        colel = len(marc_car)

        for i in range(po, colel + 2):
            text1.delete(i)

        for i in range(po - 1, len(marc_car)):
            veg = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]), (fari_car[i]),
                   (door_car[i]), (power_car[i])]
            variant.append(veg)

        for component1 in variant:
            text1.insert('', END, yol, values=component1)
            yol += 1
        if len(marc_car) == 0:
            ""
        else:
            marc_car_save = ' ; '.join(marc_car) + '&'
            model_car_save = ' ; '.join(model_car) + '&'
            year_of_release_save = ' ; '.join(year_of_release) + '&'
            color_car_save = ' ; '.join(color_car) + '&'
            price_car_save = ' ; '.join(price_car) + "&"
            fari_car_save = ' ; '.join(fari_car) + "&"
            door_car_save = ' ; '.join(door_car) + "&"
            power_car_save = ' ; '.join(power_car)

            carina.writelines(marc_car_save)
            carina.writelines(model_car_save)
            carina.writelines(year_of_release_save)
            carina.writelines(color_car_save)
            carina.writelines(price_car_save)
            carina.writelines(fari_car_save)
            carina.writelines(door_car_save)
            carina.writelines(power_car_save)

        label["text"] = ""
        if len(marc_car) >= po:
            text1.selection_add(po)
        elif len(marc_car) == 0:
            ""
        else:
            text1.selection_add(po - 1)
        carina.close()


def find():
    def dismis(find_open):
        find_open.grab_release()
        find_open.destroy()

    def pmarc():
        def pm():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i in range(1, len(marc_car2) + 1):
                    text1.delete(i)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            poisk = inputing2.get()
            DP = len(poisk)
            i2 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            if poisk == '':
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                bat4['command'] = otmenapoiska
                find_open.destroy()
            else:
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                for pmar in marc_car:
                    i2 += 1
                    pmar = str(pmar.replace('ё', 'е'))
                    pmar = str(pmar.lower())
                    poisk = str(poisk.replace('ё', 'е'))
                    poisk = str(poisk.lower())
                    if str(poisk) == pmar[0:DP]:
                        marc_car2.append(marc_car[i2 - 1])
                        model_car2.append(model_car[i2 - 1])
                        year_car2.append(year_of_release[i2 - 1])
                        color_car2.append(color_car[i2 - 1])
                        price_car2.append(price_car[i2 - 1])
                        fari_car2.append(fari_car[i2 - 1])
                        door_car2.append(door_car[i2 - 1])
                        power_car2.append(power_car[i2 - 1])
                        idd = len(marc_car2)
                        fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                               price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                        for component in fj:
                            text1.insert('', END, idd, values=component)
                        bat4['command'] = otmenapoiska
                    else:
                        bat4['command'] = otmenapoiska
                find_open.destroy()
            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск по марки")
        inputing2 = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        inputing2.pack(side=TOP, pady=5)
        bat21["command"] = pm
        bat21.pack(side=TOP, pady=5)
        find_open.geometry("400x200")
        label_find.pack()

    def pmod():
        def pmo():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i in range(1, len(marc_car2) + 1):
                    text1.delete(i)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            poisk = inputing.get()
            DP = len(poisk)
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            i3 = 0
            if poisk == '':
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                bat4['command'] = otmenapoiska
                find_open.destroy()
            else:
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                for pmar in model_car:
                    i3 += 1
                    pmar = str(pmar.replace('ё', 'е'))
                    pmar = str(pmar.lower())
                    poisk = str(poisk.replace('ё', 'е'))
                    poisk = str(poisk.lower())
                    if str(poisk) == pmar[0:DP]:
                        marc_car2.append(marc_car[i3 - 1])
                        model_car2.append(model_car[i3 - 1])
                        year_car2.append(year_of_release[i3 - 1])
                        color_car2.append(color_car[i3 - 1])
                        price_car2.append(price_car[i3 - 1])
                        fari_car2.append(fari_car[i3 - 1])
                        door_car2.append(door_car[i3 - 1])
                        power_car2.append(power_car[i3 - 1])
                        idd = len(marc_car2)
                        fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                               price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                        for component in fj:
                            text1.insert('', END, idd, values=component)
                        bat4['command'] = otmenapoiska
                    else:
                        bat4['command'] = otmenapoiska
                    find_open.destroy()
            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск по модели")
        label_find["foreground"] = "#000000"
        inputing = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        inputing.pack(side=TOP, pady=5)
        bat21['command'] = pmo
        bat21.pack(side=TOP, pady=5)
        find_open.geometry("400x200")
        label.pack()

    def pyear():
        def py():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i in range(1, len(marc_car2) + 1):
                    text1.delete(i)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            poisk = inputing.get()
            DP = len(poisk)
            i5 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            if poisk == '':
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                bat4['command'] = otmenapoiska
                find_open.destroy()
            else:
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                for pmar in year_of_release:
                    i5 += 1
                    pmar = str(pmar.replace('ё', 'е'))
                    pmar = str(pmar.lower())
                    poisk = str(poisk.replace('ё', 'е'))
                    poisk = str(poisk.lower())
                    if str(poisk) == pmar[0:DP]:
                        marc_car2.append(marc_car[i5 - 1])
                        model_car2.append(model_car[i5 - 1])
                        year_car2.append(year_of_release[i5 - 1])
                        color_car2.append(color_car[i5 - 1])
                        price_car2.append(price_car[i5 - 1])
                        fari_car2.append(fari_car[i5 - 1])
                        door_car2.append(door_car[i5 - 1])
                        power_car2.append(power_car[i5 - 1])
                        idd = len(marc_car2)
                        fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                               price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                        for component in fj:
                            text1.insert('', END, idd, values=component)
                        bat4['command'] = otmenapoiska
                    else:
                        bat4['command'] = otmenapoiska
                    find_open.destroy()
            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск году")
        label_find["foreground"] = "#000000"
        inputing = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        inputing.pack(side=TOP, pady=5)
        bat21['command'] = py
        bat21.pack(side=TOP, pady=5)
        find_open.geometry("400x200")
        label.pack()

    def pcolor():
        def pc():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i7 in range(1, len(marc_car2) + 1):
                    text1.delete(i7)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            poisk = inputing.get()
            DP = len(poisk)
            i4 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            if poisk == '':
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                bat4['command'] = otmenapoiska
                find_open.destroy()
            else:
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                for pmar in color_car:
                    i4 += 1
                    pmar = str(pmar.replace('ё', 'е'))
                    pmar = str(pmar.lower())
                    poisk = str(poisk.replace('ё', 'е'))
                    poisk = str(poisk.lower())
                    if str(poisk) == pmar[0:DP]:
                        marc_car2.append(marc_car[i4 - 1])
                        model_car2.append(model_car[i4 - 1])
                        year_car2.append(year_of_release[i4 - 1])
                        color_car2.append(color_car[i4 - 1])
                        price_car2.append(price_car[i4 - 1])
                        fari_car2.append(fari_car[i4 - 1])
                        door_car2.append(door_car[i4 - 1])
                        power_car2.append(door_car[i4 - 1])
                        idd = len(marc_car2)
                        fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                               price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                        for component in fj:
                            text1.insert('', END, idd, values=component)
                        bat4['command'] = otmenapoiska
                    else:
                        bat4['command'] = otmenapoiska
                find_open.destroy()
            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск по цвету")
        label_find["foreground"] = "#000000"
        inputing = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        inputing.pack(side=TOP, pady=5)
        bat21['command'] = pc
        bat21.pack(side=TOP, pady=5)
        find_open.geometry("400x200")
        label.pack()

    def pprice():
        def price():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i7 in range(1, len(marc_car2) + 1):
                    text1.delete(i7)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            poisk = inputing.get()
            DP = len(poisk)
            i4 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            if poisk == '':
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                bat4['command'] = otmenapoiska
                find_open.destroy()
            else:
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                for pmar in price_car:
                    i4 += 1
                    if poisk == pmar[0:DP]:
                        marc_car2.append(marc_car[i4 - 1])
                        model_car2.append(model_car[i4 - 1])
                        year_car2.append(year_of_release[i4 - 1])
                        color_car2.append(color_car[i4 - 1])
                        price_car2.append(price_car[i4 - 1])
                        fari_car2.append(fari_car[i4 - 1])
                        door_car2.append(door_car[i4 - 1])
                        power_car2.append(door_car[i4 - 1])
                        idd = len(marc_car2)
                        fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                               price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                        for component in fj:
                            text1.insert('', END, idd, values=component)
                        bat4['command'] = otmenapoiska
                    else:
                        bat4['command'] = otmenapoiska
                    find_open.destroy()
            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск по цене")
        label_find["foreground"] = "#000000"
        inputing = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        inputing.pack(side=TOP, pady=5)
        bat21['command'] = price
        bat21.pack(side=TOP, pady=5)
        find_open.geometry("400x200")
        label.pack()

    def ppower():
        def power():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i7 in range(1, len(marc_car2) + 1):
                    text1.delete(i7)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            poisk = inputing.get()
            DP = len(poisk)
            i4 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            if poisk == '':
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                bat4['command'] = otmenapoiska
                find_open.destroy()
            else:
                for i in range(1, len(marc_car) + 1):
                    text1.delete(i)
                for pmar in power_car:
                    i4 += 1
                    if poisk == pmar[0:DP]:
                        marc_car2.append(marc_car[i4 - 1])
                        model_car2.append(model_car[i4 - 1])
                        year_car2.append(year_of_release[i4 - 1])
                        color_car2.append(color_car[i4 - 1])
                        price_car2.append(price_car[i4 - 1])
                        fari_car2.append(fari_car[i4 - 1])
                        door_car2.append(door_car[i4 - 1])
                        power_car2.append(power_car[i4 - 1])
                        idd = len(marc_car2)
                        fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                               price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                        for component in fj:
                            text1.insert('', END, idd, values=component)
                        bat4['command'] = otmenapoiska
                    else:
                        bat4['command'] = otmenapoiska
                    find_open.destroy()
            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск по мощности")
        label_find["foreground"] = "#000000"
        inputing = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        inputing.pack(side=TOP, pady=5)
        bat21['command'] = power
        bat21.pack(side=TOP, pady=5)
        find_open.geometry("400x200")
        label.pack()

    def pfari():
        def pfarvkl():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i7 in range(1, len(marc_car2) + 1):
                    text1.delete(i7)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            i4 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            for i in range(1, len(marc_car) + 1):
                text1.delete(i)
            for pmar in fari_car:
                i4 += 1
                if pmar == 'Включены':
                    marc_car2.append(marc_car[i4 - 1])
                    model_car2.append(model_car[i4 - 1])
                    year_car2.append(year_of_release[i4 - 1])
                    color_car2.append(color_car[i4 - 1])
                    price_car2.append(price_car[i4 - 1])
                    fari_car2.append(fari_car[i4 - 1])
                    door_car2.append(door_car[i4 - 1])
                    power_car2.append(power_car[i4 - 1])
                    idd = len(marc_car2)
                    fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                           price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                    for component in fj:
                        text1.insert('', END, idd, values=component)
                    bat4['command'] = otmenapoiska
                else:
                    bat4['command'] = otmenapoiska
                find_open.destroy()

            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        def pfarvikl():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i7 in range(1, len(marc_car2) + 1):
                    text1.delete(i7)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            i4 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            for i in range(1, len(marc_car) + 1):
                text1.delete(i)
            for pmar in fari_car:
                i4 += 1
                if pmar == 'Выключены':
                    marc_car2.append(marc_car[i4 - 1])
                    model_car2.append(model_car[i4 - 1])
                    year_car2.append(year_of_release[i4 - 1])
                    color_car2.append(color_car[i4 - 1])
                    price_car2.append(price_car[i4 - 1])
                    fari_car2.append(fari_car[i4 - 1])
                    door_car2.append(door_car[i4 - 1])
                    power_car2.append(power_car[i4 - 1])
                    idd = len(marc_car2)
                    fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                           price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                    for component in fj:
                        text1.insert('', END, idd, values=component)
                    bat4['command'] = otmenapoiska
                else:
                    bat4['command'] = otmenapoiska
                find_open.destroy()

            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск по состоянию фар")
        bat30 = Button(find_open, width=14, height=2, text='Выключены')
        bat31 = Button(find_open, width=14, height=2, text='Включены')
        label_find["foreground"] = "#000000"
        # inputing = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        # inputing.pack(side=TOP, pady=5)
        bat30.pack(side=TOP, pady=5)
        bat30['command'] = pfarvikl
        bat31.pack(side=TOP, pady=5)
        bat31['command'] = pfarvkl
        find_open.geometry("400x200")
        label.pack()

    def pdoor():
        def pdvervikl():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i7 in range(1, len(marc_car2) + 1):
                    text1.delete(i7)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            i4 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            for i in range(1, len(marc_car) + 1):
                text1.delete(i)
            for pmar in door_car:
                i4 += 1
                if pmar == 'Закрыты':
                    marc_car2.append(marc_car[i4 - 1])
                    model_car2.append(model_car[i4 - 1])
                    year_car2.append(year_of_release[i4 - 1])
                    color_car2.append(color_car[i4 - 1])
                    price_car2.append(price_car[i4 - 1])
                    fari_car2.append(fari_car[i4 - 1])
                    door_car2.append(door_car[i4 - 1])
                    power_car2.append(power_car[i4 - 1])
                    idd = len(marc_car2)
                    fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                           price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                    for component in fj:
                        text1.insert('', END, idd, values=component)
                    bat4['command'] = otmenapoiska
                else:
                    bat4['command'] = otmenapoiska
                find_open.destroy()

            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        def pdvervkl():
            def otmenapoiska():
                bat4.pack_forget()
                bat1.pack(side=LEFT, padx=5)
                bat2.pack(side=LEFT, padx=5)
                bat3.pack(side=LEFT, padx=5)
                bat4.pack(side=LEFT, padx=5)
                bat4['text'] = 'Поиск'
                for i7 in range(1, len(marc_car2) + 1):
                    text1.delete(i7)
                mas = []
                you = 0
                for i in range(len(marc_car)):
                    fj = [(marc_car[i]), (model_car[i]), (year_of_release[i]), (color_car[i]), (price_car[i]),
                          (fari_car[i]), (door_car[i]), (power_car[i])]
                    mas.append(fj)
                for component in mas:
                    you += 1
                    text1.insert('', END, you, values=component)
                bat4['command'] = find

            i4 = 0
            marc_car2 = []
            model_car2 = []
            year_car2 = []
            color_car2 = []
            price_car2 = []
            fari_car2 = []
            door_car2 = []
            power_car2 = []
            for i in range(1, len(marc_car) + 1):
                text1.delete(i)
            for pmar in door_car:
                i4 += 1
                if pmar == 'Открыты':
                    marc_car2.append(marc_car[i4 - 1])
                    model_car2.append(model_car[i4 - 1])
                    year_car2.append(year_of_release[i4 - 1])
                    color_car2.append(color_car[i4 - 1])
                    price_car2.append(price_car[i4 - 1])
                    fari_car2.append(fari_car[i4 - 1])
                    door_car2.append(door_car[i4 - 1])
                    power_car2.append(power_car[i4 - 1])
                    idd = len(marc_car2)
                    fj = [(marc_car2[idd - 1], model_car2[idd - 1], year_car2[idd - 1], color_car2[idd - 1],
                           price_car2[idd - 1], fari_car2[idd - 1], door_car2[idd - 1], power_car2[idd - 1])]
                    for component in fj:
                        text1.insert('', END, idd, values=component)
                    bat4['command'] = otmenapoiska
                else:
                    bat4['command'] = otmenapoiska
                find_open.destroy()

            bat1.pack_forget()
            bat2.pack_forget()
            bat3.pack_forget()
            bat4['text'] = 'Отмена поиска'

        bat20.pack_forget()
        bat22.pack_forget()
        bat23.pack_forget()
        bat24.pack_forget()
        bat25.pack_forget()
        bat26.pack_forget()
        bat27.pack_forget()
        bat28.pack_forget()
        label_find = Label(find_open, text="Поиск по состоянию фар")
        bat30 = Button(find_open, width=14, height=2, text='Закрыты')
        bat31 = Button(find_open, width=14, height=2, text='Открыты')
        label_find["foreground"] = "#000000"
        # inputing = Entry(find_open, width=40)
        bat21 = Button(find_open, width=14, height=2, text='Найти')
        label_find.pack(side=TOP, pady=5)
        # inputing.pack(side=TOP, pady=5)
        bat30.pack(side=TOP, pady=5)
        bat30['command'] = pdvervikl
        bat31.pack(side=TOP, pady=5)
        bat31['command'] = pdvervkl
        find_open.geometry("400x200")
        label.pack()

    find_open = Toplevel()
    find_open.title("Поиск")
    find_open.geometry("1150x100")
    find_open.protocol("WM_DELETE_WINDOW", lambda: dismis(find_open))
    bat20 = Button(find_open, width=14, height=2, text='По марке')
    bat22 = Button(find_open, width=14, height=2, text='По модели')
    bat23 = Button(find_open, width=14, height=2, text='По году')
    bat24 = Button(find_open, width=14, height=2, text='По цвету')
    bat25 = Button(find_open, width=14, height=2, text='По цене')
    bat26 = Button(find_open, width=22, height=2, text='По состоянию фар')
    bat27 = Button(find_open, width=22, height=2, text='По состоянию дверей')
    bat28 = Button(find_open, width=22, height=2, text='По мощности')

    bat20["command"] = pmarc
    bat22["command"] = pmod
    bat23["command"] = pyear
    bat24["command"] = pcolor
    bat25["command"] = pprice
    bat26["command"] = pfari
    bat27["command"] = pdoor
    bat28["command"] = ppower

    bat20.pack(side=LEFT, padx=10)
    bat22.pack(side=LEFT, padx=10)
    bat23.pack(side=LEFT, padx=10)
    bat24.pack(side=LEFT, padx=10)
    bat25.pack(side=LEFT, padx=10)
    bat26.pack(side=LEFT, padx=10)
    bat27.pack(side=LEFT, padx=10)
    bat28.pack(side=LEFT, padx=10)
    find_open.grab_set()


def redact():
    def dismiss(mainredact):
        mainredact.grab_release()
        mainredact.destroy()

    if str(text1.selection()) == "()":
        label["foreground"] = "#B71C1C"
        label["text"] = "Выберите строку!"
    else:
        label["text"] = ""
        lox = text1.selection()
        loz = int(str(text1.selection())[2:-3]) - 1

        def red_a():
            def dismiss(reda_open):
                reda_open.grab_release()
                reda_open.destroy()

            def colorgo1r(color = str):
                lox = text1.selection()
                loz = int(str(text1.selection())[2:-3]) - 1
                text1.delete(lox)
                mar = marc_car[loz]
                mod = model_car[loz]
                year = year_of_release[loz]
                color_car[loz] = color
                price = price_car[loz]
                fari = fari_car[loz]
                door = door_car[loz]
                power = power_car[loz]

                fj = [(mar, mod, year, color, price, fari, door, power)]

                for component in fj:
                    text1.insert('', loz, lox, values=component)
                carina = open('carina.txt', 'w')
                marc_car_save = ' ; '.join(marc_car) + '&'
                model_car_save = ' ; '.join(model_car) + '&'
                year_of_release_save = ' ; '.join(year_of_release) + '&'
                color_car_save = ' ; '.join(color_car) + '&'
                price_car_save = ' ; '.join(price_car) + '&'
                fari_car_save = ' ; '.join(fari_car) + "&"
                door_car_save = ' ; '.join(door_car) + "&"
                power_car_save = ' ; '.join(power_car)

                carina.writelines(marc_car_save)
                carina.writelines(model_car_save)
                carina.writelines(year_of_release_save)
                carina.writelines(color_car_save)
                carina.writelines(price_car_save)
                carina.writelines(fari_car_save)
                carina.writelines(door_car_save)
                carina.writelines(power_car_save)
                carina.close()
                dismiss(reda_open)



            reda_open = Toplevel()
            reda_open.title("Цвет")
            reda_open.geometry("300x300")
            reda_open.protocol("WM_DELETE_WINDOW", lambda: dismiss(reda_open))
            f1r = Frame(reda_open)
            f2r = Frame(reda_open)
            f3r = Frame(reda_open)
            f4r = Frame(reda_open)
            f5r = Frame(reda_open)

            b10r = Button(f1r, width=9, height=4, bg='yellow', text='Желтый', command=lambda: colorgo1r('Желтый'))
            b11r = Button(f1r, width=9, height=4, bg='red', text='Красный', command=lambda: colorgo1r('Красный'))
            b12r = Button(f1r, width=9, height=4, bg='blue', text='Синий', command=lambda: colorgo1r('Синий'))
            b13r = Button(f1r, width=9, height=4, bg='green', text='Зеленый', command=lambda: colorgo1r('Зеленый'))
            b14r = Button(f2r, width=9, height=4, bg='white', text='Белый', command=lambda: colorgo1r('Белый'))
            b15r = Button(f2r, width=9, height=4, bg='black', text='Черный', foreground='white',
                          command=lambda: colorgo1r('Черный'))
            b16r = Button(f2r, width=9, height=4, bg='grey', text='Серый', command=lambda: colorgo1r('Серый'))
            b17r = Button(f2r, width=9, height=4, bg='silver', text='Серебряный', command=lambda: colorgo1r('Серебряный'))
            b18r = Button(f3r, width=9, height=4, bg='brown', text='Коричневый', command=lambda: colorgo1r('Коричневый'))
            b19r = Button(f3r, width=9, height=4, bg='orange', text='Оранжевый', command=lambda: colorgo1r('Оранжевый'))
            b20r = Button(f3r, width=9, height=4, bg='violet', text='Фиолетовый', command=lambda: colorgo1r('Фиолетовый'))
            # b21r = Button(f3r, width=9, height=4, bg='', text='')
            # b22r = Button(f4r, width=9, height=4, bg='', text='')
            # b23r = Button(f4r, width=9, height=4, bg='', text='')
            # b24r = Button(f4r, width=9, height=4, bg='', text='')
            # b25r = Button(f4r, width=9, height=4, bg='', text='')
            # b26r = Button(f5r, width=9, height=4, bg='', text='')
            # b27r = Button(f5r, width=9, height=4, bg='', text='')
            # b28r = Button(f5r, width=9, height=4, bg='', text='')
            # b29r = Button(f5r, width=9, height=4, bg='', text='')

            f1r.pack()
            f2r.pack()
            f3r.pack()
            f4r.pack()
            f5r.pack()

            b10r.pack(side=LEFT)
            b11r.pack(side=LEFT)
            b12r.pack(side=LEFT)
            b13r.pack(side=LEFT)
            b14r.pack(side=LEFT)
            b15r.pack(side=LEFT)
            b16r.pack(side=LEFT)
            b17r.pack(side=LEFT)
            b18r.pack(side=LEFT)
            b19r.pack(side=LEFT)
            b20r.pack(side=LEFT)
            # b21r.pack(side=LEFT)
            # b22r.pack(side=LEFT)
            # b23r.pack(side=LEFT)
            # b24r.pack(side=LEFT)
            # b25r.pack(side=LEFT)
            # b26r.pack(side=LEFT)
            # b27r.pack(side=LEFT)
            # b28r.pack(side=LEFT)
            # b29r.pack(side=LEFT)
            reda_open.grab_set()
            dismiss(mainredact)

        def red_b():
            def dismiss(redb_open):
                redb_open.grab_release()
                redb_open.destroy()

            def rb():
                try:
                    price = inputingr.get()
                    a = int(price)
                    if a < 1:
                        raise ValueError
                    lox = text1.selection()
                    loz = int(str(text1.selection())[2:-3]) - 1
                    text1.delete(lox)
                    mar = marc_car[loz]
                    mod = model_car[loz]
                    year = year_of_release[loz]
                    color = color_car[loz]
                    price_car[loz] = price
                    fari = fari_car[loz]
                    door = door_car[loz]
                    power = power_car[loz]

                    fj = [(mar, mod, year, color, price, fari, door, power)]

                    for component in fj:
                        text1.insert('', loz, lox, values=component)
                    carina = open('carina.txt', 'w')
                    marc_car_save = ' ; '.join(marc_car) + '&'
                    model_car_save = ' ; '.join(model_car) + '&'
                    year_of_release_save = ' ; '.join(year_of_release) + '&'
                    color_car_save = ' ; '.join(color_car) + '&'
                    price_car_save = ' ; '.join(price_car) + '&'
                    fari_car_save = ' ; '.join(fari_car) + "&"
                    door_car_save = ' ; '.join(door_car) + "&"
                    power_car_save = ' ; '.join(power_car)

                    carina.writelines(marc_car_save)
                    carina.writelines(model_car_save)
                    carina.writelines(year_of_release_save)
                    carina.writelines(color_car_save)
                    carina.writelines(price_car_save)
                    carina.writelines(fari_car_save)
                    carina.writelines(door_car_save)
                    carina.writelines(power_car_save)
                    carina.close()
                    dismiss(redb_open)
                except:
                    label_red["foreground"] = "#B71C1C"

            redb_open = Toplevel()
            redb_open.title("Цена")
            redb_open.geometry("250x100")
            #redb_open.protocol("WM_DELETE_WINDOW", lambda: dismis(redb_open))
            inputingr = Entry(redb_open, width=40)
            label_red = Label(redb_open, text="Введите Цену")
            button_r = Button(redb_open, width=14, height=2, text='Далее', command=rb)
            label_red.pack()
            inputingr.pack()
            button_r.pack()
            redb_open.grab_set()
            dismiss(mainredact)

        def red_i():
            def dismiss(redb_open):
                redb_open.grab_release()
                redb_open.destroy()

            def rb():
                try:
                    power = inputingr.get()
                    a = int(power)
                    if a < 1 or a > 2000:
                        raise ValueError
                    lox = text1.selection()
                    loz = int(str(text1.selection())[2:-3]) - 1
                    text1.delete(lox)
                    mar = marc_car[loz]
                    mod = model_car[loz]
                    year = year_of_release[loz]
                    color = color_car[loz]
                    price = price_car[loz]
                    fari = fari_car[loz]
                    door = door_car[loz]
                    power_car[loz] = power

                    fj = [(mar, mod, year, color, price, fari, door, power)]

                    for component in fj:
                        text1.insert('', loz, lox, values=component)
                    carina = open('carina.txt', 'w')
                    marc_car_save = ' ; '.join(marc_car) + '&'
                    model_car_save = ' ; '.join(model_car) + '&'
                    year_of_release_save = ' ; '.join(year_of_release) + '&'
                    color_car_save = ' ; '.join(color_car) + '&'
                    price_car_save = ' ; '.join(price_car) + '&'
                    fari_car_save = ' ; '.join(fari_car) + "&"
                    door_car_save = ' ; '.join(door_car) + "&"
                    power_car_save = ' ; '.join(power_car)

                    carina.writelines(marc_car_save)
                    carina.writelines(model_car_save)
                    carina.writelines(year_of_release_save)
                    carina.writelines(color_car_save)
                    carina.writelines(price_car_save)
                    carina.writelines(fari_car_save)
                    carina.writelines(door_car_save)
                    carina.writelines(power_car_save)
                    carina.close()
                    dismiss(redb_open)
                except:
                    label_red["foreground"] = "#B71C1C"

            redb_open = Toplevel()
            redb_open.title("Мощность")
            redb_open.geometry("250x100")
            #redb_open.protocol("WM_DELETE_WINDOW", lambda: dismis(redb_open))
            inputingr = Entry(redb_open, width=40)
            label_red = Label(redb_open, text="Введите Мощность")
            button_r = Button(redb_open, width=14, height=2, text='Далее', command=rb)
            label_red.pack()
            inputingr.pack()
            button_r.pack()
            redb_open.grab_set()
            dismiss(mainredact)

        def red_c():
            def dismiss(far_and_door_r):
                far_and_door_r.grab_release()
                far_and_door_r.destroy()

            def working_r():
                fari = "Включены"
                lox = text1.selection()
                loz = int(str(text1.selection())[2:-3]) - 1
                text1.delete(lox)
                mar = marc_car[loz]
                mod = model_car[loz]
                year = year_of_release[loz]
                color = color_car[loz]
                price = price_car[loz]
                fari_car[loz] = fari
                door = door_car[loz]
                power = power_car[loz]

                fj = [(mar, mod, year, color, price, fari, door, power)]

                for component in fj:
                    text1.insert('', loz, lox, values=component)
                carina = open('carina.txt', 'w')
                marc_car_save = ' ; '.join(marc_car) + '&'
                model_car_save = ' ; '.join(model_car) + '&'
                year_of_release_save = ' ; '.join(year_of_release) + '&'
                color_car_save = ' ; '.join(color_car) + '&'
                price_car_save = ' ; '.join(price_car) + '&'
                fari_car_save = ' ; '.join(fari_car) + "&"
                door_car_save = ' ; '.join(door_car) + "&"
                power_car_save = ' ; '.join(power_car)

                carina.writelines(marc_car_save)
                carina.writelines(model_car_save)
                carina.writelines(year_of_release_save)
                carina.writelines(color_car_save)
                carina.writelines(price_car_save)
                carina.writelines(fari_car_save)
                carina.writelines(door_car_save)
                carina.writelines(power_car_save)
                carina.close()
                dismiss(far_and_door_r)

            def notworking_r():
                fari = "Выключены"
                lox = text1.selection()
                loz = int(str(text1.selection())[2:-3]) - 1
                text1.delete(lox)
                mar = marc_car[loz]
                mod = model_car[loz]
                year = year_of_release[loz]
                color = color_car[loz]
                price = price_car[loz]
                fari_car[loz] = fari
                door = door_car[loz]
                power = power_car[loz]

                fj = [(mar, mod, year, color, price, fari, door, power)]

                for component in fj:
                    text1.insert('', loz, lox, values=component)
                carina = open('carina.txt', 'w')
                marc_car_save = ' ; '.join(marc_car) + '&'
                model_car_save = ' ; '.join(model_car) + '&'
                year_of_release_save = ' ; '.join(year_of_release) + '&'
                color_car_save = ' ; '.join(color_car) + '&'
                price_car_save = ' ; '.join(price_car) + '&'
                fari_car_save = ' ; '.join(fari_car) + "&"
                door_car_save = ' ; '.join(door_car) + "&"
                power_car_save = ' ; '.join(power_car)

                carina.writelines(marc_car_save)
                carina.writelines(model_car_save)
                carina.writelines(year_of_release_save)
                carina.writelines(color_car_save)
                carina.writelines(price_car_save)
                carina.writelines(fari_car_save)
                carina.writelines(door_car_save)
                carina.writelines(power_car_save)
                carina.close()
                dismiss(far_and_door_r)

            far_and_door_r = Toplevel()
            far_and_door_r.title("Состояние фар")
            far_and_door_r.geometry("250x130")
            #far_and_door_r.protocol("WM_DELETE_WINDOW", lambda: dismisi(far_and_door_r))
            flab = Label(far_and_door_r, text="Состояние фар")
            truebut = Button(far_and_door_r, width=14, height=2, text='Включены', command=working_r)
            falsebut = Button(far_and_door_r, width=14, height=2, text='Выключены', command=notworking_r)
            flab.pack(side=TOP, pady=4)
            truebut.pack(side=TOP, pady=4)
            falsebut.pack(side=TOP, pady=4)
            far_and_door_r.grab_set()
            dismiss(mainredact)

        def red_d():
            def dismiss(far_and_door_r2):
                far_and_door_r2.grab_release()
                far_and_door_r2.destroy()

            def opend_r():
                door = "Открыты"
                lox = text1.selection()
                loz = int(str(text1.selection())[2:-3]) - 1
                text1.delete(lox)
                mar = marc_car[loz]
                mod = model_car[loz]
                year = year_of_release[loz]
                color = color_car[loz]
                price = price_car[loz]
                fari = fari_car[loz]
                door_car[loz] = door
                power = power_car[loz]

                fj = [(mar, mod, year, color, price, fari, door, power)]

                for component in fj:
                    text1.insert('', loz, lox, values=component)
                carina = open('carina.txt', 'w')
                marc_car_save = ' ; '.join(marc_car) + '&'
                model_car_save = ' ; '.join(model_car) + '&'
                year_of_release_save = ' ; '.join(year_of_release) + '&'
                color_car_save = ' ; '.join(color_car) + '&'
                price_car_save = ' ; '.join(price_car) + '&'
                fari_car_save = ' ; '.join(fari_car) + "&"
                door_car_save = ' ; '.join(door_car) + "&"
                power_car_save = ' ; '.join(power_car)

                carina.writelines(marc_car_save)
                carina.writelines(model_car_save)
                carina.writelines(year_of_release_save)
                carina.writelines(color_car_save)
                carina.writelines(price_car_save)
                carina.writelines(fari_car_save)
                carina.writelines(door_car_save)
                carina.writelines(power_car_save)
                carina.close()
                dismiss(far_and_door_r2)

            def notopend_r():
                door = "Закрыты"
                lox = text1.selection()
                loz = int(str(text1.selection())[2:-3]) - 1
                text1.delete(lox)
                mar = marc_car[loz]
                mod = model_car[loz]
                year = year_of_release[loz]
                color = color_car[loz]
                price = price_car[loz]
                fari = fari_car[loz]
                door_car[loz] = door
                power_car[loz] = power

                fj = [(mar, mod, year, color, price, fari, door, power)]
                carina = open('carina.txt', 'w')
                for component in fj:
                    text1.insert('', loz, lox, values=component)

                marc_car_save = ' ; '.join(marc_car) + '&'
                model_car_save = ' ; '.join(model_car) + '&'
                year_of_release_save = ' ; '.join(year_of_release) + '&'
                color_car_save = ' ; '.join(color_car) + '&'
                price_car_save = ' ; '.join(price_car) + '&'
                fari_car_save = ' ; '.join(fari_car) + "&"
                door_car_save = ' ; '.join(door_car) + "&"
                power_car_save = ' ; '.join(power_car)

                carina.writelines(marc_car_save)
                carina.writelines(model_car_save)
                carina.writelines(year_of_release_save)
                carina.writelines(color_car_save)
                carina.writelines(price_car_save)
                carina.writelines(fari_car_save)
                carina.writelines(door_car_save)
                carina.writelines(power_car_save)
                carina.close()
                dismiss(far_and_door_r2)

            far_and_door_r2 = Toplevel()
            far_and_door_r2.title("Состояние дверей")
            far_and_door_r2.geometry("250x130")
            #far_and_door_r2.protocol("WM_DELETE_WINDOW", lambda: dismisi(far_and_door_r2))
            flab = Label(far_and_door_r2, text="Состояние дверей")
            truebut = Button(far_and_door_r2, width=14, height=2, text='Открыты', command=opend_r)
            falsebut = Button(far_and_door_r2, width=14, height=2, text='Закрыты', command=notopend_r)
            flab.pack(side=TOP, pady=4)
            truebut.pack(side=TOP, pady=4)
            falsebut.pack(side=TOP, pady=4)
            far_and_door_r2.grab_set()
            dismiss(mainredact)

        mainredact = Toplevel()
        mainredact.title("Изменение")
        mainredact.geometry("380x150")
        mainredact.protocol("WM_DELETE_WINDOW", lambda: dismiss(mainredact))
        delbat = Button(mainredact, text="Отмена", command=lambda: dismiss(mainredact))
        bat_a = Button(mainredact, text="Цвет", command=red_a)
        bat_b = Button(mainredact, text="Цена", command=red_b)
        bat_c = Button(mainredact, text="Сост.фар", command=red_c)
        bat_d = Button(mainredact, text="Сос.дверей", command=red_d)
        bat_i = Button(mainredact, text="Мощность", command=red_i)
        labelred = Label(mainredact, text="Выберете, что изменить")
        labelred.pack(pady=10)
        bat_a.pack(side=LEFT, padx=10)
        bat_b.pack(side=LEFT, padx=10)
        bat_c.pack(side=LEFT, padx=10)
        bat_d.pack(side=LEFT, padx=10)
        bat_i.pack(side=LEFT, padx=10)
        mainredact.grab_set()


main = Tk()
main.title("car")
main.geometry("1000x400")
columns = ("Марка", "Модель", "Год", "Цвет", "Цена", "Фары", "Двери", "Мощность")

label = Label(width=30, height=2, text="")
label.pack()
bat1 = Button(width=14, height=2, text='Добавить машину')
bat2 = Button(width=14, height=2, text='Убрать машину')
bat3 = Button(width=14, height=2, text='Изменить')
bat4 = Button(width=14, height=2, text='Поиск')
text1 = ttk.Treeview(columns=columns, show="headings")
scrollbar = ttk.Scrollbar(orient="vertical", command=text1.yview)
bat1["command"] = add
bat2["command"] = delite
bat3["command"] = redact
bat4['command'] = find
scrollbar.pack(side=RIGHT, fill=Y)
text1.pack()

text1.heading("Марка", text="Марка")
text1.heading("Модель", text="Модель")
text1.heading("Год", text="Год")
text1.heading("Цвет", text="Цвет")
text1.heading("Цена", text="Цена")
text1.heading("Фары", text="Фары")
text1.heading("Двери", text="Двери")
text1.heading("Мощность", text="Мощность")

text1.column("#1", width=120)
text1.column("#2", width=120)
text1.column("#3", width=120)
text1.column("#4", width=120)
text1.column("#5", width=120)
text1.column("#6", width=120)
text1.column("#7", width=120)
text1.column("#8", width=120)

if file[0] != "":
    you = 0
    for component in vegitables:
        you += 1
        text1.insert('', END, you, values=component)

bat1.pack(side=LEFT, padx=10)
bat2.pack(side=LEFT, padx=10)
bat3.pack(side=LEFT, padx=10)
bat4.pack(side=LEFT, padx=10)

main.mainloop()