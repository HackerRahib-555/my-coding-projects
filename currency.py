import requests
import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, Text

File = 'convert.txt'

root = tk.Tk()
root.title('Currency converter')
root.geometry('500x500')
root.config(bg='dark blue')

# Function to handle the currency conversion
def lol():
    # Get values from entries
    Currency = currency_entry.get().strip().upper()
    amount = amount_entry.get()
    converted = converted_entry.get().strip().upper()
    
    if not Currency or not amount or not converted:
        messagebox.showerror(text='Invalid input. Please fill in all fields')
    URL = f'https://v6.exchangerate-api.com/v6/9579f578c568b8c7a059d3b2/latest/{Currency}'
    request = requests.get(URL)

    if request.status_code == 200:
        data = request.json()
        if converted in data["conversion_rates"]:
            rate = data["conversion_rates"][converted]
            try:
                final = float(rate) * float(amount)
                result_label.config(text=f"{amount} {Currency} = {final} {converted}")
                with open('convert.txt', 'a') as file:
                    file.write(f"{amount} {Currency} = {final} {converted}\n")

            except ValueError:
                messagebox.showerror(text='Invalid number')
            
        else:
            messagebox.showwarning(text="Invalid currency code please enter a valid currency code(e.g: USD).")
    else:
        messagebox.showerror("Error: Unable to fetch data. Please try again later.")

def history():
    try:
        with open('convert.txt', 'r') as file:
           show = file.read()
           show_window = tk.Toplevel(root)
           show_window.title('Conversions history')
           show_window.geometry('400x300')
           text = Text(show_window, height=300, width=300)
           text.pack()
           text.insert(END, show)
           text.config(state='disabled')
    except FileNotFoundError:
       messagebox.showerror(text='File not found')


# Creating Entry widgets
currency_label = Label(root, text="From Currency (3-letter code):")
currency_label.pack(pady=5)

currency_entry = Entry(root)
currency_entry.pack(pady=5)

amount_label = Label(root, text="Amount to Convert:")
amount_label.pack(pady=5)

amount_entry = Entry(root)
amount_entry.pack(pady=5)

converted_label = Label(root, text="To Currency (3-letter code):")
converted_label.pack(pady=5)

converted_entry = Entry(root)
converted_entry.pack(pady=5)

# Button to trigger the conversion
convert_button = Button(root, text='Convert', font='Arial 13', command=lol)
convert_button.pack(side='bottom', pady=20)

history_button = Button(root, text='History', font='Arial 13', command=history)
history_button.pack(side='bottom', pady=40)
# Label to display the result
result_label = Label(root, text="", font='Arial 14')
result_label.pack(pady=20)

root.mainloop()
