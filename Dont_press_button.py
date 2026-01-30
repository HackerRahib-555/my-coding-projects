import tkinter as tk
window = tk.Tk()
window.title("DO NOT CLICK THE BUTTON")
window.geometry("500x500")
window.configure(bg="green")

def close():
    Label.config(text="I TOLD YOU NOT TO PRESS THE BUTTON. NOW YOU WILL SEE THE CONSEQUENCES")
    window.destroy()

Label = tk.Label(window, text="Whatever you do, do NOT click the button IDC about your snoopiness")
Label.pack(pady=30)

Button = tk.Button(window, text="Button to not press", command=close)
Button.pack(pady=90)

window.mainloop()