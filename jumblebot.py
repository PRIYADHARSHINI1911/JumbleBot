import tkinter 
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers=["America","India","Canada","Australia","London"]

questions =[]

for i in answers:
    words=list(i)
    shuffle(words)
    questions.append(words)

num=random.randint(0,len(questions)-1)

def initial():
    global questions,num
    lbl.configure(text=questions[num])
def answercheck():
    global  questions,num,answers
    userinput =e1.get()
    if userinput==answers[num]:
        messagebox.showinfo('Success','Your answer was correct')
    else:
        messagebox.showinfo('Wrong','Your answer is not correct')    
        e1.delete(0,END)
def resetswitch():
    global questions,num,answers
    num=random.randint(0,len(questions)-1)
    lbl.configure(text=questions[num])
    e1.delete(0,END)

window=Tk()
window.geometry("300x300")
window.configure(background='#242B2E')
window.title("JumbleBot")
window.iconbitmap("favicon (1).ico")

lbl=Label(window,font='times 20')
lbl.pack(pady=30,ipady=10,ipadx=10)

answer=StringVar()
e1=Entry(window,textvariable=answer)
e1.pack(ipadx=5,ipady=5,pady=10)

button1=Button(window,text="Check",width=20,command=answercheck)
button1.pack(padx=40,pady=20)
button1.configure(background='#00D84A')

button2=Button(window,text="Reset",width=20,command=resetswitch)
button2.pack(padx=40,pady=20)
button2.configure(background='#E21717')

initial()

window.mainloop()