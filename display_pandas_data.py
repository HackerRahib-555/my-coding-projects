import tkinter as tk
import pandas as pd

data = pd.read_csv("cool_spreadsheet.csv")
window = tk.Tk()
window.title("Names")
window.geometry("1000x500")
Label = tk.Label(text=data)
Label.pack(pady=30)

window.mainloop()