from tkinter import *  

def d_v():#Нахождение среднего числа ввод
    global txt_d_v
    global btn_d_v_1
    btn_1.destroy()
    btn_2.destroy()
    btn_3.destroy()
    lbl_d_v = Label()
    lbl_d_v.place(x = 60, y = 0)
    lbl_d_v.configure(text = 'Введите все числа', font = ('Arial Bold', 15), bg = '#24587A', fg = 'white')
    txt_d_v = Entry(window, width = 30)
    txt_d_v.place(x = 57, y = 40)
    btn_d_v_1 = Button(window, text = "Расчитать", command = d, font = ('Arial Bold', 10))
    btn_d_v_1.place(x = 113, y = 70)
    btn_d_v_2 = Button(window, text = "Выйти", command = quiting, font = ('Arial Bold', 10))
    btn_d_v_2.place(x = 125, y = 200)

def prost_v():#Проверка числа на простоту ввод
    global txt_prost_v_1
    global btn_prost_v_1
    btn_1.destroy()
    btn_2.destroy()
    btn_3.destroy()
    lbl = Label()
    lbl.place(x = 80, y = 0)
    lbl.configure(text = 'Введите число', font = ('Arial Bold', 15), bg = '#24587A', fg = 'white')
    txt_prost_v_1 = Entry(window, width = 30)
    txt_prost_v_1.place(x = 57, y = 40)
    btn_prost_v_1 = Button(window, text = "Расчитать", command = prost, font = ('Arial Bold', 10))
    btn_prost_v_1.place(x = 113, y = 70)
    btn_prost_v_2 = Button(window, text = "Выйти", command = quiting, font = ('Arial Bold', 10))
    btn_prost_v_2.place(x = 125, y = 200)

    
def prost():#Проверка числа на прототу
    btn_prost_v_1.destroy()
    flag = True
    l = txt_prost_v_1.get()
    try:
        l = int(l)
        for i in range(2, l):
            if l%i==0 and flag == True:
                lbl_prost_1 = Label()
                lbl_prost_1.place(x = 65, y = 120)
                lbl_prost_1.configure(text = 'Число не простое.', font = ('Arial Bold', 15), bg = '#24587A', fg = 'white')
                flag = False
        if flag == True:
            lbl_prost_2 = Label()
            lbl_prost_2.place(x = 80, y = 120)
            lbl_prost_2.configure(text = 'Число простое.', font = ('Arial Bold', 15), bg = '#24587A', fg = 'white')
    except ValueError:
        lbl_prost_2 = Label()
        lbl_prost_2.place(x = 15, y = 120)
        lbl_prost_2.configure(text = 'Неправильный ввод данных.', font = ('Arial Bold', 15), bg = '#24587A', fg = 'white')


def d():#Нахождение среднего числа
    btn_d_v_1.destroy()
    lst=[]
    l = txt_d_v.get()
    if ',' in l:
        l=l.replace(',', ' ')
    l = l.split()
    for i in range(len(l)):
        count=0
        for j in range(len(l[i])):
            if l[i][j].isalpha() == False:
                count+=1
                if count == len(l[i]):
                    lst.append(int(l[i]))
    if lst:
        l = sum(lst) / len(lst)
        lbl_d_1 = Label(window, text = 'Среднее число:', font = ('Arial Bold', 15), bg = '#24587A', fg = 'white')
        lbl_d_1.place(x = 55, y = 130)
        lbl_d_2 = Label(window, text = l, font = ('Arial Bold', 15), bg = '#24587A', fg = 'white')
        lbl_d_2.place(x = 200, y = 130)
    
def quiting():#Выход
    window.destroy()
    start()

def quiting_window():#Окончательный выход
    window.destroy()
            
def start():#Начальное окно
    global window
    global btn_1
    global btn_2
    global btn_3
    window = Tk()
    window.title('Файл от компании ANTONENTERTAINMENT')
    window.geometry('300x250+800+350')
    window.resizable(width=False, height=False)
    window["bg"] = "#24587A"
    btn_1 = Button(window, text = " Посчитать среднее значение числа.", command = d_v, font = ('Arial Bold', 10))
    btn_1.place(x = 35, y = 10)
    btn_2 = Button(window, text = " Проверить число на простоту.", command = prost_v, font = ('Arial Bold', 10))
    btn_2.place(x = 50, y = 50)
    btn_3 = Button(window, text = "Выйти.", command = quiting_window, font = ('Arial Bold', 10))
    btn_3.place(x = 120, y = 220)
    window.mainloop()

start()



