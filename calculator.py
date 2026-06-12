#calculator

from tkinter import *


expr = ""

window = Tk()
window.geometry('500x300')
window.title('CALCULATOR')

display = StringVar()
entry = Entry(window, textvariable=display,bg="#E8F0FE",fg="#DE1818",font=("Arial", 12),width=30)
entry.grid(columnspan=5, ipadx=100,ipady=15)

def p(key):
    global expr 
    expr += str(key)
    print(expr)
    display.set("  "+expr)

def equals():
    global expr
    try:     
        expr = str(eval(expr))
        print(expr)
        display.set("   "+expr)
    except:
        display.set("    SYNTAX ERROR")
        expr = ""
    
def clear():
    global expr
    expr = ""  
    display.set(expr)


b1 = Button(text = '1',command= lambda :p(1),height=3, width=13,activebackground="light grey", bg="white")
b2 = Button(text = '2',command= lambda :p(2),height=3, width=13,activebackground="light grey", background="white")
b3 = Button(text = '3',command= lambda :p(3),height=3, width=13,activebackground="light grey", background="white")
b4 = Button(text = '4',command= lambda :p(4),height=3, width=13,activebackground="light grey", bg="white")
b5 = Button(text = '5',command= lambda :p(5),height=3, width=13,activebackground="light grey", bg="white")
b6 = Button(text = '6',command= lambda :p(6),height=3, width=13,activebackground="light grey", bg="white")
b7 = Button(text = '7',command= lambda :p(7),height=3, width=13,activebackground="light grey", bg="white")
b8 = Button(text = '8',command= lambda :p(8),height=3, width=13,activebackground="light grey", bg="white")
b9 = Button(text = '9',command= lambda :p(9),height=3, width=13,activebackground="light grey", bg="white")
b0 = Button(text = '0',command= lambda :p(0),height=3, width=13,activebackground="light grey", bg="white")

plus = Button(text = '+',command = lambda : p('+'),height=3, width=13,activebackground="light grey", bg="#BEFBF3")
minus = Button(text = '-',command = lambda : p('-'),height=3, width=13,activebackground="light grey", bg="#BEFBF3")
mul = Button(text = '*',command = lambda : p('*'),height=3, width=13,activebackground="light grey",  bg="#BEFBF3")
div = Button(text = '/',command = lambda : p('/'),height=3, width=13,activebackground="light grey",  bg="#BEFBF3")


clr = Button(text = 'clear',command = clear,height=3, width=13,activebackground="light grey", activeforeground="red",bg="#F32424")
eq = Button(text = '=',command = equals,height=3, width=13,activebackground="light grey", activeforeground="green",bg="#3CF658")

b1.grid(row = 2,column = 1)
b2.grid(row = 2,column = 2)
b3.grid(row = 2,column = 3)
b4.grid(row = 3,column = 1)
b5.grid(row = 3,column = 2)
b6.grid(row = 3,column = 3)
b7.grid(row = 4,column = 1)
b8.grid(row = 4,column = 2)
b9.grid(row = 4,column = 3)
b0.grid(row = 5,column = 1)

plus.grid(row = 2,column = 4)
minus.grid(row = 3,column = 4)
mul.grid(row = 4,column = 4)
div.grid(row = 5,column = 4)

clr.grid(row = 5,column= 3)
eq.grid(row = 5,column= 2)



window.mainloop()