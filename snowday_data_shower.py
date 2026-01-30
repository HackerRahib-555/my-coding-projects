import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.geometry("600x600")
window.title("It should be a snow day these conditions are bad")

tk.Label(
    window,
    text="You think it should be a snowday based on these extreme conditions but..."
).pack(pady=10)

tk.Label(
    window,
    text="NO MATTER THE CONDITIONS SCHOOLS ALWAYS STAY OPEN",
    fg="red"
).pack(pady=10)

tk.Label(
    window,
    text="SCHOOLS NEVER CARE ABOUT SAFETY OF STUDENTS ONLY SCHOOL",
    fg="red"
).pack(pady=10)


data = pd.read_csv("snow.csv")


fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(data["Day"], data["Snow"], marker="*", color="blue", label="Snow")
ax.plot(data["Day"], data["Cold"], marker="*", color="green", label="Cold")
ax.legend()
ax.set_xlabel("Day")
ax.set_ylabel("Scale 1/5")
ax.set_title("Snow and cold levels(they suck)")


canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(pady=10)

window.mainloop()

