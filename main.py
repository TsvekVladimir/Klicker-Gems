from tkinter import *

tk = Tk()
tk.title('Clicker')
tk.geometry("1000x550")
n = 0


def nplus():
    global n
    n = n + 1
    label['text'] = str(n) + 'GEMS'

def nsbros():
    global n
    n = 0
    label['text'] = str(n) + 'GEMS'

btn1 = Button(text="Клик", background="#000", foreground="#fff",
             padx="20", pady="8", font="16", command=nplus)
btn1.pack()

label = Label(tk, text=str(n)+'GEMS', font=('Helvetica 100'))
label.pack()
btn2 = Button(text="Сброс", background="#000", foreground="#fff",
             padx="20", pady="8", font="16", command=nsbros)
btn2.pack()
mainloop()
