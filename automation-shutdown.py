import os
from datetime import datetime
import time

notified = False

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time >= "21:00":
        os.system('notify-send "Shutting down in 1 Hour"')
        notified = True

    if current_time >= "21:30":
        os.system('notify-send "Shutting down in 30 min"')
        notified = True


    if current_time >= "21:55":
        os.system('notify-send "Shutting down in 5 min"')
        notified = True

    if current_time >= "22:00":
        os.system("shutdown now")
        break

    time.sleep(300)