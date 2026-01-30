import tkinter as tk
import threading
import serial
import time

# Serial setup
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

# Sensor states
stolen = False
not_stolen = False

# --- Serial reading ---
def read_serial():
    global stolen, not_stolen
    while True:
        try:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if line.startswith("STOLEN"):
                stolen = True
                not_stolen = False
            elif line.startswith("NOT_STOLEN"):
                not_stolen = True
                stolen = False
        except Exception as e:
            print("Serial read error:", e)

# --- Send commands ---
def send(cmd):
    if ser:
        ser.write(f"{cmd}\n".encode("utf-8"))

def sensor_on():
    send("ON")

def sensor_off():
    send("OFF")


def update_labels():
    if stolen:
        status_label.config(text="ALERT! Stolen!", fg="red")
    elif not_stolen:
        status_label.config(text="Not stolen", fg="green")
    else:
        status_label.config(text="Waiting...", fg="orange")
    
    root.after(500, update_labels)


root = tk.Tk()
root.title("Tilt Sensor Monitor")
root.config(bg="orange")
root.geometry("400x200")

status_label = tk.Label(root, text="Waiting...", font=("Arial", 16), bg="orange")
status_label.pack(pady=20)

on_btn = tk.Button(root, text="Sensor ON", command=sensor_on, width=15, font=("Arial", 12))
on_btn.pack(pady=5)

off_btn = tk.Button(root, text="Sensor OFF", command=sensor_off, width=15, font=("Arial", 12))
off_btn.pack(pady=5)

# --- Start threads ---
threading.Thread(target=read_serial, daemon=True).start()
update_labels()

root.mainloop()
