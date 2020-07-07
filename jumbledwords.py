
import tkinter
from tkinter import *
import random
from tkinter import messagebox


answer=[
"ruby",
"python",
"java",
"visualbasic",
"javascript",
"pascal",
"bootstrap",
"flop",
"hero",
"trip",
"love",

]

jumbled =[

"yuby",
"nothpy",
"ajav",
"siclausivab",
"ptavasricj",
"lscpaa",
"pbtsoroat",
"lopf",
"reho",
"iptr",
"ovle",
]
    #jumbled words of your choice
num = random.randrange(0, 11, 1)


def basic():
    global jumbled, answer,num
    lbl1.config(text=jumbled[num])


def reset():
    global jumbled, answer, num
    num = random.randrange(0, 11, 1)
    lbl1.config(text=jumbled[num])
    textbox1.delete(0, END)


def verifier():
    global jumbled, answer, num
    var = textbox1.get()
    if var == answer[num]:
        messagebox.showinfo("Well Done!!", "This is a correct answer")
        reset()
    else:
        messagebox.showerror("Ohh Noo!!", "This is not Correct")
        textbox1.delete(0, END)


window = Tk()

window.title("Jumbled WordPlay ")
window.geometry("500x300")

lbl=Label(window,text="Guess the correct word",  fg="Red",font=('Times New Roman','20'))
lbl.grid(row=0,column=0)
lbl.pack(pady = 10)

lbl1=Label(window,text="",  fg="Blue",font=('Times New Roman','20'))
lbl1.pack()


textbox1=Entry(window, font=('Times New Roman', '20'))
textbox1.pack()

btn1 = Button(window, text="Verify Answer", font=('Times New Roman', '20'), width=15, bg="#00b894", fg="#222f3e", relief=GROOVE, command=verifier)
btn1.pack(pady =20)

btn2=Button(window,text="Reset",font=('Times New Roman', '20'),width=10, bg="#00b894",fg="#222f3e",relief=GROOVE, command=reset)
btn2.pack()


basic()
window.mainloop()

