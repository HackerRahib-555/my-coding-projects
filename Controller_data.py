import tkinter as tk
from datetime import datetime
import serial
import threading
import os
import time

# Serial port
ser = serial.Serial("/dev/ttyACM0", 9600)

# Global variables
joystick_x = "Unknown"
joystick_y = "Unknown"
joystick_btn = "Unknown"
buttonA = "Unknown"
buttonB = "Unknown"

# File names
files = {
    "Joystick X": "Joystick_X.txt",
    "Joystick Y": "Joystick_Y.txt",
    "Joystick Button": "Joystick_Button.txt",
    "ButtonA": "ButtonA.txt",
    "ButtonB": "ButtonB.txt"
}

# Ensure files exist
for f in files.values():
    if not os.path.exists(f):
        open(f, "w").close()

def read_serial():
    global joystick_x, joystick_y, joystick_btn, buttonA, buttonB
    while True:
        try:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            
            if line.startswith("Joystick X: "):
                joystick_x = line.split(":")[1].strip()
            elif line.startswith("Joystick Y: "):
                joystick_y = line.split(":")[1].strip()
            elif line.startswith("Joystick Pressed: "):
                joystick_btn = line.split(":")[1].strip()
            elif line.startswith("ButtonA: "):
                buttonA = line.split(":")[1].strip()
            elif line.startswith("ButtonB: "):
                buttonB = line.split(":")[1].strip()
        except Exception as e:
            print("Serial read error:", e)

def save_data():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(files["Joystick X"], "a") as f:
            f.write(f"{timestamp}: {joystick_x}\n")
        with open(files["Joystick Y"], "a") as f:
            f.write(f"{timestamp}: {joystick_y}\n")
        with open(files["Joystick Button"], "a") as f:
            f.write(f"{timestamp}: {joystick_btn}\n")
        with open(files["ButtonA"], "a") as f:
            f.write(f"{timestamp}: {buttonA}\n")
        with open(files["ButtonB"], "a") as f:
            f.write(f"{timestamp}: {buttonB}\n")
        time.sleep(1)  # Save every second

def update_labels():
    joystick_x_label.config(text=f"Joystick X: {joystick_x}")
    joystick_y_label.config(text=f"Joystick Y: {joystick_y}")
    joystick_btn_label.config(text=f"Joystick Button: {joystick_btn}")
    buttonA_label.config(text=f"ButtonA: {buttonA}")
    buttonB_label.config(text=f"ButtonB: {buttonB}")
    root.after(500, update_labels)

def open_history(filename, title):
    window = tk.Toplevel(root)
    window.title(title)
    text = tk.Text(window, width=60, height=20)
    text.pack()
    try:
        with open(filename, "r") as f:
            content = f.read()
        text.insert(tk.END, content)
    except FileNotFoundError:
        text.insert(tk.END, "No data yet.")

# Tkinter GUI
root = tk.Tk()
root.title("Joystick Monitor")
root.geometry("450x400")

joystick_x_label = tk.Label(root, text=f"Joystick X: {joystick_x}", font=("Arial", 12))
joystick_x_label.pack(pady=5)
joystick_y_label = tk.Label(root, text=f"Joystick Y: {joystick_y}", font=("Arial", 12))
joystick_y_label.pack(pady=5)
joystick_btn_label = tk.Label(root, text=f"Joystick Button: {joystick_btn}", font=("Arial", 12))
joystick_btn_label.pack(pady=5)
buttonA_label = tk.Label(root, text=f"ButtonA: {buttonA}", font=("Arial", 12))
buttonA_label.pack(pady=5)
buttonB_label = tk.Label(root, text=f"ButtonB: {buttonB}", font=("Arial", 12))
buttonB_label.pack(pady=5)

# History buttons
for label, file in files.items():
    b = tk.Button(root, text=f"{label} History", font=("Arial", 10),
                  command=lambda f=file, l=label: open_history(f, l))
    b.pack(pady=2)

# Start threads
threading.Thread(target=read_serial, daemon=True).start()
threading.Thread(target=save_data, daemon=True).start()

update_labels()
root.mainloop()