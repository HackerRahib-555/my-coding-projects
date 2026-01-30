import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_display.config(state=tk.NORMAL)
            chat_display.insert(tk.END, message + '\n')
            chat_display.config(state=tk.DISABLED)
            chat_display.config(bg='lightgrey')
            chat_display.yview(tk.END)
        except:
            break

def send_message():
    message = message_entry.get()
    if message.lower() == 'exit':
        client_socket.send(message.encode())
        client_socket.close()
        root.quit()
    else:
        client_socket.send(message.encode())
        message_entry.delete(0, tk.END)

server_ip = '127.0.0.1'
server_port = 6549

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
except:
    print("Unable to connect to the server.")
    exit()

username_prompt = client_socket.recv(1024).decode('utf-8')
root = tk.Tk()
root.config(bg='grey')
root.withdraw()
username = simpledialog.askstring("Username", username_prompt)
if not username:
    exit()
client_socket.send(username.encode())

root.deiconify()
root.title(f"Chat for {username}")

chat_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20)
chat_display.pack(padx=10, pady=10)

message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5, padx=10, side=tk.LEFT)

send_button = tk.Button(root, text="Send", command=send_message, width='200')
send_button.pack(pady=5, padx=10, side=tk.RIGHT)

threading.Thread(target=receive_messages).start()

root.mainloop()
