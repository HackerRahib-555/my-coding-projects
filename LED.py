import tkinter as tk
import serial
import time

# Initialize Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

def send_command(cmd):
    arduino.write(cmd.encode())

# Functions for LED 1
def led1_on(event=None):
    send_command('1')
    status_label.config(text="LED 1 is ON")

def led1_off(event=None):
    send_command('0')
    status_label.config(text="LED 1 is OFF")

# Functions for LED 2
def led2_on(event=None):
    send_command('3')
    status_label2.config(text="LED 2 is ON")

def led2_off(event=None):
    send_command('4')
    status_label2.config(text="LED 2 is OFF")

# Functions for Blink mode
def blink_on(event=None):
    send_command('5')
    status_label_blink.config(text="Blink Mode ON")

def blink_off(event=None):
    send_command('6')
    status_label_blink.config(text="Blink Mode OFF (LEDs OFF)")

# Quit function
def quit_app():
    arduino.close()  # Close serial connection safely
    root.destroy()

# Tkinter GUI
root = tk.Tk()
root.title("Dual LED Controller")
root.geometry("500x500")  # Bigger window

# Buttons
button_font = ("Arial", 16, "bold")

# LED 1 buttons
led1_on_button = tk.Button(root, text="Turn LED 1 On", command=led1_on, width=20, height=2, bg="green", fg="white", font=button_font)
led1_on_button.pack(pady=10)

led1_off_button = tk.Button(root, text="Turn LED 1 Off", command=led1_off, width=20, height=2, bg="red", fg="white", font=button_font)
led1_off_button.pack(pady=10)

# LED 2 buttons
led2_on_button = tk.Button(root, text="Turn LED 2 On", command=led2_on, width=20, height=2, bg="green", fg="white", font=button_font)
led2_on_button.pack(pady=10)

led2_off_button = tk.Button(root, text="Turn LED 2 Off", command=led2_off, width=20, height=2, bg="red", fg="white", font=button_font)
led2_off_button.pack(pady=10)

# Blink mode buttons
blink_on_button = tk.Button(root, text="Blink Mode On", command=blink_on, width=20, height=2, bg="blue", fg="white", font=button_font)
blink_on_button.pack(pady=10)

blink_off_button = tk.Button(root, text="Blink Mode Off", command=blink_off, width=20, height=2, bg="gray", fg="white", font=button_font)
blink_off_button.pack(pady=10)

# Quit button
quit_button = tk.Button(root, text="Quit", command=quit_app, width=20, height=2, font=button_font)
quit_button.pack(pady=15)

# Status label
status_label = tk.Label(root, text="LED1 is OFF", font=("Arial", 18))
status_label.pack(pady=30)
status_label2 = tk.Label(root, text="LED2 is OFF", font=("Arial", 18))
status_label2.pack(pady=20)
status_label_blink = tk.Label(root, text="Blink mode is OFF", font=("Arial", 18))
status_label_blink.pack(pady=10)

root.bind("<Key-1>", led1_on)
root.bind("<Key-2>", led1_off)
root.bind("<Key-3>", led2_on)
root.bind("<Key-4>", led2_off)
root.bind("<Key-5>", blink_on)
root.bind("<Key-6>", blink_off)
root.focus_set()
root.mainloop()
