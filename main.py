import tkinter as tk


f = open('rezults.txt')
n = float(f.readline())
z = float(f.readline())
count = float(f.readline())
f.close()

root = tk.Tk()
root.title('Clicker')
root.geometry("1500x800")


def nplus():
    global n
    n = round((n + z), 3)
    label1['text'] = str(n) + '$'


def nsbros():
    global n
    global z
    global count
    n = 0
    z = 0.1
    count = 0.4
    label1['text'] = str(n) + '$'
    label2['text'] = 'За клик: ' + str(round(z, 3)) + '$'
    label3['text'] = 'Стоимость улучшения: ' + str(round(count, 3)) + '$'


def dopclick():
    global n
    global z
    global count
    if n >= count:
        n = round((n - count), 3)
        z = z + z/4
        count = z * 4
    label1['text'] = str(n) + '$'
    label2['text'] = 'За клик: ' + str(round(z, 3)) + '$'
    label3['text'] = 'Стоимость улучшения: ' + str(round(count, 3)) + '$'


label1 = tk.Label(root, text=str(round(n, 3))+'$', font=('Helvetica 100'))
label1.pack()

label2 = tk.Label(root, text='За клик: '+str(round(z, 3))+'$', font=('Helvetica 30'))
label2.pack()
label3 = tk.Label(root, text='Стоимость улучшения: '+str(round(count, 3))+'$', font=('Helvetica 30'))
label3.pack()

btn1 = tk.Button(root, text="Клик", background="#000", foreground="#fff",
                 padx="60", pady="30", font="Helvetica 50", command=nplus)

btn1.pack()
label4 = tk.Label(root, text='', font=('Helvetica 30'))
label4.pack()
btn3 = tk.Button(root, text="Улучшение", background="#000", foreground="#fff",
                 padx="60", pady="10", font="Helvetica 25", command=dopclick)
btn3.pack()
label5 = tk.Label(root, text='', font=('Helvetica 30'))
label5.pack()
btn2 = tk.Button(root, text="Сброс", background="#000", foreground="#fff",
                 padx="20", pady="8", font="16", command=nsbros)
btn2.pack()

label6 = tk.Label(root, text='', font=('Helvetica 30'))
label6.pack()

tk.mainloop()
f = open('rezults.txt', "w")
f.write(str(n) + '\n')
f.write(str(z) + '\n')
f.write(str(count) + '\n')
f.close()
