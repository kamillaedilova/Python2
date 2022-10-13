
from math import *
from tkinter import *
import re
root= Tk()
root.geometry("350x350")
root.title("Calculator")
root["bg"] = "white"

p= "" #принтуем добавляя к "" цифры(вывод цифр на экран)
s = "" #решение выводится с помощью b=""

#окно ввода
def show(a): 
    output = Label(root, text = a, width = 39, height = 2)
    output['bg']= "yellow"
    output.grid(row = 0, column = 0, columnspan = 7)
    
#bыполнение различных операций с помощью eval    
def equal():
    global p, s 
    print(s) 
    try: eval(s)
    except: print(show("Error"))
    else:
        solve = int(eval(s)) if eval(s) - int(eval(s)) == 0.0 else eval(s) # избегаем чисел вида 3.0,4.0
        show(solve)
        p= str(solve)
        s = p
        
#ввод цифр и скобок
def one():
    global p, s
    p = p + "1"
    s = s + "1"
    show(a)
def two():
    global p, s
    p = p + "2"
    s = s + "2"
    show(p)
def three():
    global p, s
    p = p + "3"
    s = s + "3"
    show(a)
def four():
    global p, s
    p = p + "4"
    s = s + "4"
    show(p)
def five():
    global p, s
    p = p + "5"
    s = s + "5"
    show(p)
def six():
    global p, s
    p = p + "6"
    s = s + "6"
    show(p)
def seven():
    global p, s
    p = s + "7"
    p = s + "7"
    show(p)
def eight():
    global p, s
    p = p + "8"
    s = s + "8"
    show(p)
def nine():
    global p, p
    p = p + "9"
    s = s + "9"
    show(p)
def zero():
    global p, s
    p = p + "0"
    s = s + "0"
    show(p)
def bracketl():
    global p, s
    p = p + "("
    s = s + "("
    show(p)
def bracketr():
    global p, s
    p = p + ")"
    s = s + ")"
    show(p)   
def point():
    global p, s
    p = p + "."
    s = s + "."
    show(p)
def sqrt():
    global p, s
    p = p + "√"
    s = s + "sqrt("
    show(p)
def plus():
    global p, s
    if not len(p) == 0 and (p[len(p)-1].isdigit() or p[len(p)-1] == ")" or p[len(p)-1] == "e"):
        p = p + "+" 
        s = s + "+"
        show(p)
def minus():
    global p, s
    p = p + "-"
    s = s + "-"
    show(p)
def multip():
    global p, s
    p = p + "x"
    s = s + "*"
    show(p)
def division():
    global p, s
    p = p + "÷"
    s = s + "/"
    show(p)
def mod():
    global a, b
    a = a + "abs("
    b = b + "abs("
    show(a)

def sin():
    global p, s
    p = p + "sin("
    s = s + "sin("
    show(p)
def cos():
    global p, s
    p = p + "cos("
    s = s + "cos("
    show(p)
def tan():
    global p, s
    p = p + "tan("
    s = s + "tan("
    show(p)
def pii():
    global p, s
    p = p + "𝜋"
    s = s + "pi"
    show(p)
def ln():
    global p, s
    p = p + "ln("
    s = s + "log(e,"
    show(p)
def percent():
    global p, s
    p = p + "%"
    s = s + "/100"
    show(p)
def clean():
    global p, s
    p = ""
    s = ""
    show(p)
def sqr():
    global p, s
    p = p + "²"
    s = s + "**2"
    show(p)
def rad():
    global p, s
    p += "rad("
    s += "radians("
    show(s)  

bracketl_b = Button(root, text = "(", relief = GROOVE, width = 4, heigh = 2, command = bracketl).grid(row = 1, column = 0)
bracketr_b = Button(root, text = ")", relief = GROOVE, width = 4, heigh = 2, command = bracketr).grid(row = 1, column = 1)
clean_b = Button(root, text = "C", relief = GROOVE, width = 4, heigh = 2, command = clean).grid(row = 1, column = 2)
seven = Button(root, text = "7", relief = GROOVE, width = 4, heigh = 2, command = seven).grid(row = 1, column = 3)
eight = Button(root, text = "8", relief = GROOVE, width = 4, heigh = 2, command = eight).grid(row = 1, column = 4)
nine = Button(root, text = "9", relief = GROOVE, width = 4, heigh = 2, command = nine).grid(row = 1, column = 5)
division_b = Button(root, text = "÷", relief = GROOVE, width = 4, heigh = 2, command = division).grid(row = 1, column = 6)
sqrt_b = Button(root, text = "√", relief = GROOVE, width = 4, heigh = 2, command = sqrt).grid(row = 2, column = 0)
sqr_b = Button(root, text = "x²", relief = GROOVE, width = 4, heigh = 2, command = sqr).grid(row = 2, column = 1)
mod_b = Button(root, text = "|x|", relief = GROOVE, width = 4, heigh = 2, command = mod).grid(row = 2, column = 2)
four = Button(root, text = "4", relief = GROOVE, width = 4, heigh = 2, command = four).grid(row = 2, column = 3)
five = Button(root, text = "5", relief = GROOVE, width = 4, heigh = 2, command = five).grid(row = 2, column = 4)
six= Button(root, text = "6", relief = GROOVE, width = 4, heigh = 2, command = six).grid(row = 2, column = 5)
multip = Button(root, text = "x", relief = GROOVE, width = 4, heigh = 2, command = multip).grid(row = 2, column = 6)
sin_b = Button(root, text = "sin", relief = GROOVE, width = 4, heigh = 2, command = sin).grid(row = 3, column = 0)

cos_b = Button(root, text = "cos", relief = GROOVE, width = 4, heigh = 2, command = cos).grid(row = 3, column = 1)
tan_b = Button(root, text = "tan", relief = GROOVE, width = 4, heigh = 2, command = tan).grid(row = 3, column = 2)
one = Button(root, text = "1", relief = GROOVE, width = 4, heigh = 2, command = one).grid(row = 3, column = 3)
two = Button(root, text = "2", relief = GROOVE, width = 4, heigh = 2, command = two).grid(row = 3, column = 4)
three = Button(root, text = "3", relief = GROOVE, width = 4, heigh = 2, command = three).grid(row = 3, column = 5)
minus_b = Button(root, text = "-", relief = GROOVE, width = 4, heigh = 2, command = minus).grid(row = 3, column = 6)
pi_b = Button(root, text = "𝜋", relief = GROOVE, width = 4, heigh = 2, command = pii).grid(row = 4, column = 0)
ln_b = Button(root, text = "ln", relief = GROOVE, width = 4, heigh = 2, command = ln).grid(row = 4, column = 1)
percent_b = Button(root, text = "%", relief = GROOVE, width = 4, heigh = 2, command = percent).grid(row = 4, column = 2)
point_b = Button(root, text = ".", relief = GROOVE, width = 4, heigh = 2, command = point).grid(row = 4, column = 3)
zero_b = Button(root, text = "0", relief = GROOVE, width = 4, heigh = 2, command = zero).grid(row = 4, column = 4)
equal_b = Button(root, text = "=", relief = GROOVE, width = 4, heigh = 2, command = equal).grid(row = 4, column = 5)
plus_b = Button(root, text = "+", relief = GROOVE, width = 4, heigh = 2, command = plus).grid(row = 4, column = 6)

rad_b = Button(root, text = "rad", relief = GROOVE, width = 4, heigh = 2, command = rad).grid(row = 5, column = 0)

root.grid_columnconfigure(0, minsize = 50)
root.grid_columnconfigure(1, minsize = 50)
root.grid_columnconfigure(2, minsize = 50)
root.grid_columnconfigure(3, minsize = 50)
root.grid_columnconfigure(4, minsize = 50)
root.grid_columnconfigure(5, minsize = 50)
root.grid_columnconfigure(6, minsize = 50)
root.grid_rowconfigure(0, minsize = 50)
root.grid_rowconfigure(1, minsize = 50)
root.grid_rowconfigure(2, minsize = 50)
root.grid_rowconfigure(3, minsize = 50)
root.grid_rowconfigure(4, minsize = 50)
root.grid_rowconfigure(5, minsize = 50)
root.grid_rowconfigure(6, minsize = 50)

root.mainloop()
