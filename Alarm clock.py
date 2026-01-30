import tkinter as tk
from tkinter import*

import time
from time import strftime


root = tk.Tk()
root.title('Alarm clock')
root.geometry('600x600')
root.config(bg='navy')
Current = tk.StringVar()
def Time():
    
    Current.set(time.strftime('%I:%M %p'))
    root.after(5000, Time)

Time()
def check_alarm():
    global alarm_time
    
    
    print(f"Alarm: {time_of_alarm.get()} ")
    if time_of_alarm.get() == Current.get():
        print("ALARM! ALARM! Time to wake up!")


def set_alarm():
    global alarm_time
    global time_of_alarm
    alarm_input.place(x=245, y=50)
    alarm_configure.place(x=455, y=50)
    alarm_time= time_of_alarm.get()
    root.after(5000, check_alarm)
    check_alarm()

TIme = tk.Label(root, textvariable=Current, font='Roboto 25', fg='white', bg='black')
TIme.place(x='240', y='240')

Set_time = tk.Button(root, text='Set alarm', command=set_alarm, bg='orange', fg='white', font='Roboto 15')
Set_time.place(x=245, y=280)





time_of_alarm = StringVar()
alarm_input = tk.Entry(root, textvariable=time_of_alarm, font='Roboto 16')
alarm_input.place_forget()

alarm_configure = tk.Button(root, text='Set alarm', bg='black', fg='white', command=check_alarm)
alarm_configure.place_forget()






root.mainloop()

