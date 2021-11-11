import tkinter

#input variables

valString = ""

#button press functions

def press(val):
    global valString 
    valString = valString + str(val)
    equation.set(valString)

def equalsPress():
    try:
        global valString
        total = str(eval(valString))
        equation.set(total)
        valString = ''

    except:
        equation.set('ERROR')
        valString = ''
#gui

def clearPress():
    global valString
    valString = ''
    equation.set(valString)

window = tkinter.Tk()
window.geometry("300x100")

equation = tkinter.StringVar()

screen = tkinter.Entry(window, textvariable=equation)
screen.grid(row=0, columnspan=4)

# keypad gui

button7 = tkinter.Button(window, text = '7', command= lambda : press(7), height=1, width=7)
button7.grid(row = 1, column=0)

button8 = tkinter.Button(window, text='8', command=lambda : press(8), height=1, width=7)
button8.grid(row=1, column=1)

button9 = tkinter.Button(window, text='9', command=lambda : press(9), height=1, width=7)
button9.grid(row=1, column=2)

button4 = tkinter.Button(window, text='4', command=lambda : press(4), height=1, width=7)
button4.grid(row=2, column=0)

button5 = tkinter.Button(window, text='5', command=lambda : press(5), height=1, width=7)
button5.grid(row=2,column=1)

button6 = tkinter.Button(window, text='6', command=lambda : press(6), height=1, width=7)
button6.grid(row=2, column=2)

button1 = tkinter.Button(window, text='1', command=lambda : press(1), height=1, width=7)
button1.grid(row=3, column=0)

button2 =tkinter.Button(window, text='2', command=lambda : press(2), height=1, width=7)
button2.grid(row=3, column=1)

button3 = tkinter.Button(window, text='3', command=lambda : press(3), height=1, width=7)
button3.grid(row=3,column=2)

#operator buttons

clear = tkinter.Button(window, text='C', command=lambda : clearPress(), height=1, width=7)
clear.grid(row=1, column=3)

plus = tkinter.Button(window, text='+', command=lambda : press('+'), height=1, width=7)
plus.grid(row=2, column=3)

minus = tkinter.Button(window, text='-', command=lambda : press('-'), height=1, width=7)
minus.grid(row=3,column=3)

divide = tkinter.Button(window,text='%', command=lambda : press('/'), height=1, width=7)
divide.grid(row=1, column=4)

multiply = tkinter.Button(window, text='x', command=lambda : press('x'), height=1, width=7)
multiply.grid(row=2, column=4)

equalsButton = tkinter.Button(window, text='=', command=lambda : equalsPress(), height=1, width=7)
equalsButton.grid(row=3, column=4)



window.mainloop()