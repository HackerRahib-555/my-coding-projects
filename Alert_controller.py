import tkinter as tk
import serial
import threading

# === CONFIG ===
PORT = "/dev/ttyACM1"  
BAUD = 9600

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
except Exception as e:
    print("Could not open serial:", e)
    ser = None


distance = "N/A"
alert = ""
sensor_on = False

def read_serial():
    global distance, alert, sensor_on
    while ser:
        try:
            line = ser.readline().decode("utf-8").strip()
            if not line:
                continue

            
            if line.startswith("Distance:"):
               
                distance = line.split(":")[1].strip()
                alert = ""  

            elif line.startswith("ALERT"):
                alert = line  

            elif "Sensor Enabled" in line:
                sensor_on = True

            elif "Sensor Disabled" in line:
                sensor_on = False

            update_labels()

        except Exception as e:
            print("Serial read error:", e)

def send_command(cmd):
    if ser:
        ser.write(cmd.encode("utf-8"))

def toggle_sensor(event=None):
    if sensor_on:
        send_command("0")  
    else:
        send_command("1")  
    
def update_labels():
    global distance_label
    distance_label.config(text=f"Distance: {distance}")
    alert_label.config(text=alert)
    sensor_status.config(text="Sensor: ON" if sensor_on else "Sensor: OFF")


root = tk.Tk()
root.title("Ultrasonic Sensor security system controller/monitor")
root.geometry("500x500")
root.configure(bg="blue")


toggle_button = tk.Button(root, text="Turn Sensor on/off(press enter/return)", command=toggle_sensor, font=("Arial", 16), bg="orange")
toggle_button.place(x=90, y= 180)

sensor_status = tk.Label(root, text="Sensor: OFF", font=("Arial", 14), bg="orange")
sensor_status.place(x=180, y=220)

distance_label = tk.Label(root, text=f"Distance: {distance}", font=("Arial", 14), bg="orange")
distance_label.place(x=180, y=260)

alert_label = tk.Label(root, text="", fg="black", font=("Arial", 14), bg="red")
alert_label.place(x=80, y=300)

# Start serial thread
thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

root.bind("<Return>", toggle_sensor)
root.focus_set()

root.mainloop()