import os
from tkinter import *
import tkinter as tk
# Create an instance of tkinter frame or window
window=Tk()
# Set the size of the tkinter windowdow
window.geometry("700x350")
window.title("PythonGeeks")#give title to the window
head=Label(window, text="Shutdown, Restart and Logout Using Pc", font=('Calibri 15'))# a lable
head.pack(pady=20)

def Shutdown():#function to shutdown
    os.system("shutdown /s /t 0")

def Restart():#function to restart
    os.system("shutdown /r /t 0")

def logout():#function to logout
    os.system("shutdown /l /t 0")
#creating buttons 
Button(window,text='Shutdown',command=Shutdown, font=('normal',11), bg='yellow').pack()
Button(window,text='Restart',command=Restart,font=('normal',11), bg='yellow').pack()
Button(window,text='Logout',command=logout,font=('normal',11), bg='yellow').pack()

window.mainloop()
