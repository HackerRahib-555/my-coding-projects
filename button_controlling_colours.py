import tkinter as tk
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime", "teal", "brown"]
current = 0

def check_serial():
    global current
    if ser.in_waiting > 0:
        line = ser.readline().decode().strip()
        if line == "BUTTON":
            current = (current + 1) % len(colors)
            window.config(bg=colors[current])
            label.config(text=f"Colour: {colors[current]}")
    window.after(100, check_serial)

window = tk.Tk()
window.title("Button Colour Changer")
window.geometry("400x400")

label = tk.Label(text=f"Colour: {colors[current]}")
label.pack()

check_serial()
window.mainloop()
