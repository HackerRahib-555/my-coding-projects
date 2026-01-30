import tkinter as tk
import threading
import serial

ser = serial.Serial("/dev/ttyACM1", 9600)
alert = False
Temprature = "Unknown"
Humidity = "Unknown"

def read_serial():
    global Temprature, Humidity, alert
    while ser:
        line = ser.readline().decode("utf-8").strip()

        if line.startswith("TEMP:"):
            Temprature = line.split(":")[1].strip()
        elif line.startswith("HUM:"):
            Humidity = line.split(":")[1].strip()
        elif line.startswith("ALERT:"):
            alert = True
        

def send(command):
    if ser:
        ser.write(f"{command}\n".encode("utf-8"))

def sensor_on(event=None):
    send("ON")

def sensor_off(event=None):
    send("OFF")

def update_labels():
    global alert
    temp_label.config(text=f"Temperature: {Temprature}")
    hum_label.config(text=f"Humidity: {Humidity}")
    if alert:
        alert_label.config(text="ALERT: TEMPERATURE TOO HIGH!")
        alert = False  
    else:
        alert_label.config(text="")

    root.after(1000, update_labels)


root = tk.Tk()
root.title("DHT11 Sensor Monitor")

temp_label = tk.Label(root, text=f"Temperature: {Temprature}", font=("Arial", 14))
temp_label.pack(pady=5)

hum_label = tk.Label(root, text=f"Humidity: {Humidity}", font=("Arial", 14))
hum_label.pack(pady=5)

alert_label = tk.Label(root, text="", fg="red", font=("Arial", 14))
alert_label.pack(pady=5)

on_btn = tk.Button(root, text="Turn Sensor ON (1)", command=sensor_on, width=20, font=("Arial", 12))
on_btn.pack(pady=5)

off_btn = tk.Button(root, text="Turn Sensor OFF (2)", command=sensor_off, width=20, font=("Arial", 12))
off_btn.pack(pady=5)

root.bind("<Key-1>", sensor_on)
root.bind("<Key-2>", sensor_off)

# Start serial reading in thread
threading.Thread(target=read_serial, daemon=True).start()

# Start updating labels
update_labels()
root.focus_set()
root.mainloop()
