import tkinter as tk
from tkinter import messagebox
import serial
import threading
import os

# --- Serial Setup ---
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

# --- Global States ---
light_value = 0
brightness = 0
led_enabled = True
photo_enabled = True
running = True

# --- Functions ---

def read_serial():
    global light_value, brightness, led_enabled, photo_enabled, running
    while running:
        try:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    # Example: Light: 123 | Brightness: 200 | LED: ON | Photo: ENABLED
                    parts = line.split('|')
                    for part in parts:
                        key_val = part.strip().split(':')
                        if len(key_val) == 2:
                            key, val = key_val[0].strip(), key_val[1].strip()
                            if key == "Light":
                                light_value = int(val)
                            elif key == "Brightness":
                                brightness = int(val)
                            elif key == "LED":
                                led_enabled = True if val == "ON" else False
                            elif key == "Photo":
                                photo_enabled = True if val == "ENABLED" else False
        except Exception as e:
            print("Serial read error:", e)

def send(command):
    if ser:
        ser.write(f"{command}\n".encode('utf-8'))

def led_on():
    send('L')  # toggle LED ON/OFF
    update_labels()

def led_off():
    send('l')  # force LED OFF
    update_labels()

def sensor_on():
    send('P')  # toggle photoresistor
    update_labels()

def sensor_off():
    send('p')  # force photoresistor OFF
    update_labels()

# --- GUI ---
root = tk.Tk()
root.title("LED & Photoresistor Monitor")

# Labels
light_label = tk.Label(root, text="Light: 0")
light_label.pack()

brightness_label = tk.Label(root, text="Brightness: 0")
brightness_label.pack()

led_label = tk.Label(root, text="LED: ON")
led_label.pack()

photo_label = tk.Label(root, text="Photoresistor: ENABLED")
photo_label.pack()

# Buttons
tk.Button(root, text="LED ON", command=led_on).pack()
tk.Button(root, text="LED OFF", command=led_off).pack()
tk.Button(root, text="Sensor ON", command=sensor_on).pack()
tk.Button(root, text="Sensor OFF", command=sensor_off).pack()

# File saving
file_name = "light_log.txt"
if not os.path.exists(file_name):
    with open(file_name, 'w') as f:
        f.write("Light, Brightness, LED, Photo\n")

def update_labels():
    light_label.config(text=f"Light: {light_value}")
    brightness_label.config(text=f"Brightness: {brightness}")
    led_label.config(text=f"LED: {'ON' if led_enabled else 'OFF'}")
    photo_label.config(text=f"Photoresistor: {'ENABLED' if photo_enabled else 'DISABLED'}")
    
    # Log to file
    with open(file_name, 'a') as f:
        f.write(f"{light_value},{brightness},{'ON' if led_enabled else 'OFF'},{'ENABLED' if photo_enabled else 'DISABLED'}\n")

def gui_update():
    update_labels()
    root.after(500, gui_update)  # update GUI every 0.5s

# --- Threading ---
thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

# Start GUI update loop
gui_update()
root.mainloop()

# Stop thread when GUI closes
running = False
