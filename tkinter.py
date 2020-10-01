from tkinter import *
import math
task = Tk()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
task.title('Python Calculator')
task.minsize(600, 400)

def addnum():
    try:
        res = float(a.get()) + float(b.get())
        text1.set(res)
        text2.set('')
        text3.set('')
        text4.set('')
    except:
        text1.set('Input Value!')
        text2.set('')
        text3.set('')
        text4.set('')
def subnum():
    try:
        res = float(a.get()) - float(b.get())
        text1.set(res)
        text2.set('')
        text3.set('')
        text4.set('')
    except:
        text1.set('Input Value!')
        text2.set('')
        text3.set('')
        text4.set('')
def multnum():
    try:
        res = float(a.get()) * float(b.get())
        text1.set(res)
        text2.set('')
        text3.set('')
        text4.set('')
    except:
        text1.set('Input Value!')
        text2.set('')
        text3.set('')
        text4.set('')
def divnum():
    try:
        try:
            res = float(a.get()) / float(b.get())
            text1.set(res)
            text2.set('')
            text3.set('')
            text4.set('')
        except ZeroDivisionError: 
            text1.set("You Noob!!!")
            text2.set('')
            text3.set('')
            text4.set('')
    except:
        text1.set('Input Value!')
        text2.set('')
        text3.set('')
        text4.set('')
def sinnum():
    try:
        try:
            num1 = float(a.get())*(180/math.pi)
            num2 = float(b.get())*(180/math.pi)
            res = math.sin(num1)
            res1 = math.sin(num2)
            text1.set(res)
            text2.set(res1)
            text3.set(num1)
            text4.set(num2)
        except:
            num1 = float(a.get())*(180/math.pi)
            res = math.sin(num1)
            text1.set(res)
            text2.set('')
            text3.set(num1)
            text4.set('')
    except:
        text1.set('Input Value!')
        text2.set('')
        text3.set('')
        text4.set('')
def cosnum():

    try:
        try:
            num1 = float(a.get())*(180/math.pi)
            num2 = float(b.get())*(180/math.pi)
            res = math.cos(num1)
            res1 = math.cos(num2)
            text1.set(res)
            text2.set(res1)
            text3.set(num1)
            text4.set(num2)
        except:
            num1 = float(a.get())*(180/math.pi)
            res = math.cos(num1)
            text1.set(res)
            text2.set('')
            text3.set(num1)
            text4.set('')
    except:
            text1.set('Input Value!')
            text2.set('')
            text3.set('')
            text4.set('')
def inverse():
    try:
        a1 = float(a.get())
        res = 1/a1
        text1.set(res)
        text2.set('')
        text3.set('')
        text4.set('')
    except:
        text1.set('Input Value!')
        text2.set('')
        text3.set('')
        text4.set('')
def squared():
    try:
        res = (float(a.get()))**2
        text1.set(res)
        text2.set('')
        text3.set('')
        text4.set('')
    except:
        text1.set('Input Value!')
        text2.set('')
        text3.set('')
        text4.set('')
def tannum():
    try:
        try:
            num1 = float(a.get())*(180/math.pi)
            num2 = float(b.get())*(180/math.pi)
            res = math.tan(num1)
            res1 = math.tan(num2)
            text1.set(res)
            text2.set(res1)
            text3.set(num1)
            text4.set(num2)
        except:
            num1 = float(a.get())*(180/math.pi)
            res = math.tan(num1)
            text1.set(res)
            text2.set('')
            text3.set(num1)
            text4.set('')
    except ValueError:
        text1.set('Input Value!')



Label(task, text = 'First number:').grid(row = 1, sticky=W)
Label(task, text = 'Second number:       ').grid(row = 2, sticky=W)
Label(task, text = 'Result/s: ').grid(row = 6, sticky=W)
Label(task, text = 'Radians').grid(row = 0, column = 1, sticky = W)
Label(task, text = 'Degrees').grid(row = 0, column = 2, sticky = W)
Label(task, text = 'Type:').grid(row = 0, column = 0, sticky = W)
result1 = Label(task, bg = "white", text = '', textvariable = text1).grid(row = 6, column = 1, sticky = W)
result2 = Label(task, bg = "white", text = '', textvariable = text2).grid(row = 6, column = 2, sticky = W)
degree1 = Entry(task, fg = "green", text = '', textvariable = text3).grid(row = 1, column = 2)
degree2 = Entry(task, fg = "green", text = '', textvariable = text4).grid(row = 2, column = 2)
a = Entry(task)
b = Entry(task)
a.grid(row = 1, column = 1)
b.grid(row = 2, column = 1)
Button(task, text = '+', command = addnum).grid(row = 3, column = 0, sticky=W+E+N+S)
Button(task, text = '1/X', command = inverse).grid(row = 5, column = 0, sticky=W+E+N+S)
Button(task, text = 'X^2', command = squared).grid(row = 5, column = 1, sticky=W+E+N+S)
Button(task, text = 'TAN', command = tannum).grid(row = 5, column = 2, sticky=W+E+N+S)
Button(task, text = 'SIN', command = sinnum, width = 16).grid(row = 3, column = 2, sticky=W+E+N+S)
Button(task, text = 'COS', command = cosnum, width = 16).grid(row = 4, column = 2, sticky=W+E+N+S)
Button(task, text = '-', command = subnum).grid(row = 3, column = 1, sticky=W+E+N+S)
Button(task, text = 'X', command = multnum).grid(row = 4, column = 0, sticky=W+E+N+S)
Button(task, text = '/', command = divnum).grid(row = 4, column = 1, sticky=W+E+N+S)
task.mainloop()
