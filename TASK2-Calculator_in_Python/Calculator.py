# Unfettered Calculator
from tkinter import *


e = ""
def press(num):
    global e
    e = e + str(num)
    equation.set(e)


def equal():
    try:
        global e
        total = str(eval(e))
        equation.set(total)
        e = ""
    except:
        equation.set(" error ")
        e = ""


def clear():
    global e
    e = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light green")

    gui.title("Simple Calculator")

    gui.geometry("866x474")

    equation = StringVar()

    ef = Entry(gui, textvariable=equation,font=('Times', 25, 'bold',))

    ef.grid(columnspan=4, ipadx=260)

    button1 = Button(gui, text=' 1 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(1), height=3, width=17, font=('Times', 15, 'bold',))
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(2), height=3, width=17, font=('Times', 15, 'bold'))
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(3), height=3, width=17, font=('Times', 15, 'bold'))
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(4), height=3, width=17, font=('Times', 15, 'bold'))
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(5), height=3, width=17, font=('Times', 15, 'bold'))
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(6), height=3, width=17, font=('Times', 15, 'bold'))
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(7), height=3, width=17, font=('Times', 15, 'bold'))
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(8), height=3, width=17, font=('Times', 15, 'bold'))
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(9), height=3, width=17, font=('Times', 15, 'bold'))
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='#290849', bg='#C99AF7',
                     command=lambda: press(0), height=3, width=17, font=('Times', 15, 'bold'))
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='blue', bg='#C99AF7',
                            command=lambda: press("+"), height=3, width=17, font=('Times', 15, 'bold'))
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='blue', bg='#C99AF7',
                   command=lambda: press("-"), height=3, width=17, font=('Times', 15, 'bold'))
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='blue', bg='#C99AF7',
                      command=lambda: press("*"), height=3, width=17, font=('Times', 15, 'bold'))
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='blue', bg='#C99AF7',
                    command=lambda: press("/"), height=3, width=17, font=('Times', 15, 'bold'))
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='green', bg='#C99AF7',
                   command=equal, height=3, width=17, font=('Times', 15, 'bold'))
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='red', bg='#C99AF7',
                   command=clear, height=3, width=17, font=('Times', 15, 'bold'))
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='#290849', bg='#C99AF7',
                     command=lambda: press('.'), height=3, width=17, font=('Times', 15, 'bold'))
    Decimal.grid(row=6, column=0)


    gui.mainloop()
