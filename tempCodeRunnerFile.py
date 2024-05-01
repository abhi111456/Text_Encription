from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    screen=Tk()
    screen.geometry("375x398")
    screen.title("pctApp")
    Label(text="Enter text for encription and decription ",fg="black" ,font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    Label(text="Enter secret key for encription and decription",fg="black",font=("calbri",13)).place(x=10,y=170)
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    
    screen.mainloop()

main_screen()