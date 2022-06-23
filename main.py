import tkinter as tk

"Создаем класс Klicker с переменными allclick(все очки), click(очки за клик), upgrade(стоимость улучшения)"
class Klicker:
    def __init__(self, allclick, click, upgrade):
        self.allclick = allclick
        self.click = click
        self.upgrade = upgrade
    "Создаем функцию для кнопки которая будет добавлять очки за клик"



"Открываем файл чтобы считать сохраненные данные"
f = open('rezults.txt')
Klicker.allclick = float(f.readline())
Klicker.click = float(f.readline())
Klicker.upgrade = float(f.readline())
f.close()

"Создаем окно гдще будет располагаться программа"
root = tk.Tk()
root.title('Clicker')
root.geometry("1500x800")


"Создаем лейблы чтобы видеть значения наших переменных"
label1 = tk.Label(root, text=str(round(Klicker.allclick, 3))+'$', font='Helvetica 100')
label1.pack()

label2 = tk.Label(root, text='За клик: '+str(round(Klicker.click, 3))+'$', font='Helvetica 30')
label2.pack()
label3 = tk.Label(root, text='Стоимость улучшения: '+str(round(Klicker.upgrade, 3))+'$', font='Helvetica 30')
label3.pack()

def nplus():
    Klicker.allclick = round((Klicker.allclick + Klicker.click), 3)
    label1['text'] = str(Klicker.allclick) + '$'
    "Создаем функцкцию для кнопки которая будет сбрасывать значения"
def nsbros():
    Klicker.allclick = 0
    Klicker.click = 0.1
    Klicker.upgrade = 0.4
    label1['text'] = str(Klicker.allclick) + '$'
    label2['text'] = 'За клик: ' + str(round(Klicker.click, 3)) + '$'
    label3['text'] = 'Стоимость улучшения: ' + str(round(Klicker.upgrade, 3)) + '$'
"Создаем функцию для кнопки которая будет увеличивать значение за клик"
def dopclick():
    if Klicker.allclick >= Klicker.upgrade:
        Klicker.allclick = round((Klicker.allclick - Klicker.upgrade), 3)
        Klicker.click = Klicker.click + Klicker.click / 4
        Klicker.upgrade = Klicker.click * 4
    label1['text'] = str(Klicker.allclick) + '$'
    label2['text'] = 'За клик: ' + str(round(Klicker.click, 3)) + '$'
    label3['text'] = 'Стоимость улучшения: ' + str(round(Klicker.upgrade, 3)) + '$'
if __name__ == '__main__':
    "Создаем кнопки которые будут выполнять функции, размещаем их и придаем вид"
    btn1 = tk.Button(root, text="Клик", background="#000", foreground="#fff",
                     padx="60", pady="30", font="Helvetica 50", command=nplus)
    btn1.pack()
    label4 = tk.Label(root, text='', font='Helvetica 30')
    label4.pack()
    btn3 = tk.Button(root, text="Улучшение", background="#000", foreground="#fff",
                     padx="60", pady="10", font="Helvetica 25", command=dopclick)
    btn3.pack()
    label5 = tk.Label(root, text='', font='Helvetica 30')
    label5.pack()
    btn2 = tk.Button(root, text="Сброс", background="#000", foreground="#fff",
                     padx="20", pady="8", font="16", command=nsbros)
    btn2.pack()
    label6 = tk.Label(root, text='', font='Helvetica 30')
    label6.pack()

"Создаем бесконечный цикл для нашего окна и программы"
tk.mainloop()
"Отрывает работу с файлом для записи наших результатов"
f = open('rezults.txt', "w")
f.write(str(Klicker.allclick) + '\n')
f.write(str(Klicker.click) + '\n')
f.write(str(Klicker.upgrade) + '\n')
f.close()
