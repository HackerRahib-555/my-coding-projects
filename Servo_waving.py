import tkinter as tk
import threading
import serial
import time

# Serial setup
ser = serial.Serial("/dev/ttyACM0", 9600)

# Global variables
Distance = "Unknown"
ServoWaving = False
AlertBlink = False

def read_serial():
    global Distance, ServoWaving
    while True:
        line = ser.readline().decode("utf-8").strip()
        if line.startswith("Distance:"):
            Distance = line.split(":")[1].strip()
        elif line.startswith("Servo:"):
            ServoWaving = True

def send(cmd):
    if ser:
        ser.write(f"{cmd}\n".encode("utf-8"))

def sensor_on():
    send("ON")

def sensor_off():
    send("OFF")

def wave_servo():
    send("WAVE")

def update_labels():
    global ServoWaving, AlertBlink

    # Update distance label
    distance_label.config(text=f"Distance: {Distance}")

    root.after(500, update_labels)

# Tkinter GUI setup
root = tk.Tk()
root.title("Ultrasonic & Servo Monitor")
root.config(bg='orange')
root.geometry("500x500")

distance_label = tk.Label(root, text=f"Distance: {Distance}", font=("Arial", 14), bg='orange')
distance_label.pack(pady=5)

servo_label = tk.Label(root, text="Servo is Waving!", font=("Arial", 14), bg='orange')
servo_label.pack(pady=5)

on_btn = tk.Button(root, text="Turn Sensor ON", command=sensor_on, width=20, font=("Arial", 12))
on_btn.pack(pady=5)

off_btn = tk.Button(root, text="Turn Sensor OFF", command=sensor_off, width=20, font=("Arial", 12))
off_btn.pack(pady=5)

wave_btn = tk.Button(root, text="Wave Servo", command=wave_servo, width=20, font=("Arial", 12))
wave_btn.pack(pady=5)

# Start serial reading in a daemon thread
threading.Thread(target=read_serial, daemon=True).start()

# Start updating labels
update_labels()

root.mainloop()
