import tkinter as tk
from datetime import datetime
import serial
import threading

ser = serial.Serial("/dev/ttyACM0", 9600)

Button_state = "Unknown"
Light = "Unknown"
Temprature = "Unknown"
Humidity = "Unknown"
Distance = "Unknown"


def read_serial():
    global Button_state, Light, Temprature, Humidity, Distance
    while True:
        try:
            line = ser.readline().decode("utf-8", errors="ignore").strip()
            if line.startswith("Button: "):
                Button_state = line.split(":")[1].strip()
            elif line.startswith("Light: "):
                Light = line.split(":")[1].strip()
            elif line.startswith("Temperature:"):
                Temprature = line.split(":")[1].strip()
            elif line.startswith("Humidity: "):
                Humidity = line.split(":")[1].strip()
            elif line.startswith("Distance: "):
                Distance = line.split(":")[1].strip()
        except Exception as e:
            print("Serial read error:", e)


def save_file():
    while True:
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("Button_Save.txt", "a") as f:
            f.write(f"At {time_stamp}, Button state was {Button_state}\n")
        with open("Light_record.txt", "a") as f:
            f.write(f"At {time_stamp}, Light brightness was {Light}\n")
        with open("Temprature_record.txt", "a") as f:
            f.write(f"At {time_stamp}, Temprature was {Temprature}\n")
        with open("Humidity_record.txt", "a") as f:
            f.write(f"At {time_stamp}, Humidity was {Humidity}\n")
        with open("Distance_record.txt", "a") as f:
            f.write(f"At {time_stamp}, Distance was {Distance}\n")
        # Save every second
        import time
        time.sleep(15)

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


def update_labels():
    button_label.config(text=f"Button: {Button_state}")
    light_label.config(text=f"Light: {Light}")
    temp_label.config(text=f"Temprature: {Temprature}")
    hum_label.config(text=f"Humidity: {Humidity}")
    distance_label.config(text=f"Distance: {Distance}")
    root.after(500, update_labels)


root = tk.Tk()
root.title("4 sensor monitor")
root.config(bg="green")
root.geometry("600x400")

button_label = tk.Label(root, text=f"Button: {Button_state}", font=("Arial", 14), bg="orange")
button_label.pack(pady=5)

light_label = tk.Label(root, text=f"Light: {Light}", font=("Arial", 14), bg="orange")
light_label.pack(pady=5)

temp_label = tk.Label(root, text=f"Temprature: {Temprature}", font=("Arial", 14), bg="orange")
temp_label.pack(pady=5)

hum_label = tk.Label(root, text=f"Humidity: {Humidity}", font=("Arial", 14), bg="orange")
hum_label.pack(pady=5)

distance_label = tk.Label(root, text=f"Distance: {Distance}", font=("Arial", 14), bg="orange")
distance_label.pack(pady=5)

history_btns = [
    ("Button History", "Button_Save.txt"),
    ("Light History", "Light_record.txt"),
    ("Temprature History", "Temprature_record.txt"),
    ("Humidity History", "Humidity_record.txt"),
    ("Distance History", "Distance_record.txt")
]

for label, file in history_btns:
    b = tk.Button(root, text=label, font=("Arial", 12),
                  command=lambda f=file, l=label: open_history(f, l))
    b.pack(pady=2)

# --- Start threads ---
threading.Thread(target=read_serial, daemon=True).start()
threading.Thread(target=save_file, daemon=True).start()

update_labels()
root.mainloop()
