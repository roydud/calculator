from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background='white')
root.resizable(width=False, height=False)
root.geometry('465x380+0+0')
calc = Frame(root)
calc.grid()

txtin=StringVar()
op=''
txtin.set('')

txtdisplay = Entry(calc, font=('arial', 20, 'bold'),textvar=txtin, bg='black', bd=10, width=29, justify=RIGHT)
txtdisplay.grid(row=0, column=0, columnspan=4)


#************==========================CALCULATION'S FUNCTIONS=========================**************

def clickbut(num):
    global op
    op= op + str(num)
    txtin.set(op)


def allclr():
    global op
    op=''
    txtin.set('')


def equalbut():
    global op
    result = str(eval(op))
    txtin.set(result)
    op = result

def clr():
    global op
    op=op[:-1]
    txtin.set(op)



def sqar():
    global op
    op=str(eval(op))
    op=int(op)
    op=str(op*op)
    txtin.set(op)


def sqr():
    global op
    op=str(eval(op))
    op=int(op)
    op=str(math.sqrt(op))
    txtin.set(op)

def cuberoot():
    global op
    op=str(eval(op))
    op=int(op)
    op=str(math.pow(op,1/3))
    txtin.set(op)



def fact():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.factorial(op))
    txtin.set(op)

def exp():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.exp(op))
    txtin.set(op)

def pi():
    global op
    op = str(eval(op))
    op = int(op)
    op =op*math.pi
    txtin.set(op)
def deg():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.degrees(op))
    txtin.set(op)

def log10():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.log10(op))
    txtin.set(op)

def log():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.log(op))
    txtin.set(op)

def log2():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.log2(op))
    txtin.set(op)



def sin():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.sin(op))
    txtin.set(op)

def cos():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.cos(op))
    txtin.set(op)

def tan():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.tan(op))
    txtin.set(op)

def sinh():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.sinh(op))
    txtin.set(op)

def cosh():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.cosh(op))
    txtin.set(op)

def tanh():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.tanh(op))
    txtin.set(op)

def asinh():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.asinh(op))
    txtin.set(op)

def acosh():
    global op
    op = str(eval(op))
    op = int(op)
    op = str(math.acosh(op))
    txtin.set(op)



# ******=================================BUTTON=============================================*************


btn1 = Button(calc, text='1', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(1)).grid(row=2, column=0,
                                                                                                       pady=1)
btn2 = Button(calc, text='2', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(2)).grid(row=2, column=1,
                                                                                                      pady=1)
btn3 = Button(calc, text='3', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(3)).grid(row=2, column=2, pady=1)


btn4 = Button(calc, text='4', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(4)).grid(row=3, column=0,
                                                                                                       pady=1)
btn5 = Button(calc, text='5', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(5)).grid(row=3, column=1,
                                                                                                      pady=1)
btn6 = Button(calc, text='6', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(6)).grid(row=3, column=2, pady=1)

btn7 = Button(calc, text='7', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(7)).grid(row=4, column=0,
                                                                                                       pady=1)
btn8 = Button(calc, text='8', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(8)).grid(row=4, column=1,
                                                                                                      pady=1)
btn9 = Button(calc, text='9', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : clickbut(9)).grid(row=4, column=2, pady=1)

btnclear = Button(calc, text='C', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : clr()).grid(row=1, column=0,
                                                                                                        pady=1)
btnallclear = Button(calc, text='CE', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : allclr()).grid(row=1,
                                                                                                            column=1,
                                                                                                            pady=1)
btnsqrt = Button(calc, text='x²', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : sqar()).grid(row=1, column=2,
                                                                                                       pady=1)
btnsum = Button(calc, text='+', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : clickbut('+')).grid(row=5, column=3,
                                                                                                      pady=1)
btnsub = Button(calc, text='-', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : clickbut('-')).grid(row=2, column=3,
                                                                                                      pady=1)
btnmul = Button(calc, text='*', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : clickbut('*')).grid(row=3, column=3,
                                                                                                      pady=1)
btndiv = Button(calc, text='/', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : clickbut('/')).grid(row=4, column=3,
                                                                                                      pady=1)
btnequal = Button(calc, text='=', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : equalbut()).grid(row=5, column=2,
                                                                                                        pady=1)
btnsign = Button(calc, text='√', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : sqr()).grid(row=1, column=3,
                                                                                                       pady=1)
btndot = Button(calc, text='.', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : clickbut('.')).grid(row=5, column=1,
                                                                                                      pady=1)
btnzero = Button(calc, text='0', width=6, height=1, font=('arial', 20, 'bold'),  command=lambda : clickbut(0), bd=4, bg='black').grid(row=5, column=0,
                                                                                                       pady=1)

# ****************=============================SCIENTIFIC CALCULATOR=====================================***************

lbldis = Label(calc, text='SCIENTIFIC CALCULATOR', font=('arial', 20, 'bold'), justify=CENTER)
lbldis.grid(row=0, column=4, columnspan=4)

btnpi = Button(calc, text='π', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black', command=lambda : pi()).grid(row=1, column=4,
                                                                                                     pady=1)
btnsin = Button(calc, text='Sin', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda :sin()).grid(row=1, column=5,
                                                                                                        pady=1)
btncos = Button(calc, text='Cos', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda :cos()).grid(row=1, column=6,
                                                                                                        pady=1)
btntan = Button(calc, text='Tan', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda :tan()).grid(row=1, column=7,
                                                                                                        pady=1)

btn2pi = Button(calc, text='n!', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : fact()
                ).grid(row=2, column=4,
                                                                                                       pady=1)
btnsinh = Button(calc, text='Sinh', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda :sinh()).grid(row=2,
                                                                                                          column=5,
                                                                                                          pady=1)
btncosh = Button(calc, text='Cosh', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda :cosh()).grid(row=2,
                                                                                                          column=6,
                                                                                                          pady=1)
btntanh = Button(calc, text='Tanh', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda :tanh()).grid(row=2,
                                                                                                          column=7,

                                                                                                          pady=1)

btncexp = Button(calc, text='Exp', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : exp()).grid(row=3,
                                                                                                         column=4,
                                                                                                         pady=1)
btnmod = Button(calc, text='x³', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : mod()).grid(row=3, column=5,
                                                                                                        pady=1)
btnE = Button(calc, text='3√', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',  command=lambda : cuberoot()).grid(row=3, column=6,
                                                                                                    pady=1)
btnlog = Button(calc, text='%', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda :clickbut('%')).grid(row=3, column=7,
                                                                                                        pady=1)

btndeg = Button(calc, text='Deg', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda : deg()).grid(row=4, column=4,
                                                                                                        pady=1)
btnasin = Button(calc, text='asinh', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : asinh()).grid(row=4,
                                                                                                           column=5,
                                                                                                           pady=1)
btnacos = Button(calc, text='acosh', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda : acosh()).grid(row=4,
                                                                                                           column=6,
                                                                                                           pady=1)
btnlog2 = Button(calc, text='Log', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='white',command=lambda :log()).grid(row=4,
                                                                                                          column=7,
                                                                                                          pady=1)

btnlog10 = Button(calc, text='Log10', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',command=lambda :log10()).grid(row=5,
                                                                                                            column=4,
                                                                                                            pady=1)
btnlogp1 = Button(calc, text='log2', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black', command= lambda :log2()).grid(row=5,
                                                                                                            column=5,
                                                                                                            pady=1)
btnexpm1 = Button(calc, text='(', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',  command=lambda : clickbut('(')).grid(row=5,
                                                                                                            column=6,
                                                                                                            pady=1)
btnlgamma = Button(calc, text=')', width=6, height=1, font=('arial', 20, 'bold'), bd=4, bg='black',  command=lambda : clickbut(')')).grid(row=5,
                                                                                                              column=7,
                                                                                                              pady=1)


# ******===========================================MENU AND FUNCTIONS====================================********************
def iexit():
    iexit = tkinter.messagebox.askyesno('Scientific Calculator', 'Confirm if you want to exit')
    if iexit > 0:
        root.destroy()
        return


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry('930x380+0+0')


def Standard():
    root.resizable(width=False, height=False)
    root.geometry('465x380+0+0')


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Standard', command=Standard)
filemenu.add_command(label='Scientific', command=Scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=iexit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='cut')
editmenu.add_command(label='Copy')
editmenu.add_separator()
editmenu.add_command(label='Paste')


helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='View Help')

root.config(menu=menubar)
root.mainloop()
