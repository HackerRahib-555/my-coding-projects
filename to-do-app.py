import json
import tkinter as tk
from tkinter import messagebox


class Task:
    def __init__(self, name, priority, due, completed=False):
        self.name = name
        self.priority = priority
        self.due = due
        self.completed = completed
    
    def __str__(self):
        status = 'Finished' if self.completed else 'Not finished'
        return f"Task: {self.name}, Priority: {self.priority}, Due: {self.due}, Status: {status}"

class Todo:
    def __init__(self):
        self.tasks = []
    
    def sorting(self):
        self.tasks.sort(key=lambda task: task.priority, reverse=True)
        
    def add_task(self, name, priority, due):
        new_task = Task(name, priority, due)
        self.tasks.append(new_task)
        self.sorting()
        self.display()
    
    def remove_task(self, task_name):
        for task in self.tasks:
            if task_name.lower() == task.name.lower():
                self.tasks.remove(task)
                self.display()
                return
        print("Task not found.")
        self.display()

    def mark_task(self, task_name):
        for task in self.tasks:
            if task_name.lower() == task.name.lower():
                task.completed = True
                self.display()
                return
        messagebox.showwarning("Task not found.")
        self.display()

    def display(self):
        task_list = ""
        if self.tasks:
            for task in self.tasks:
                task_list += str(task) + "\n"
        else:
            task_list = "No tasks available."
        return task_list
    
    def save(self):
        with open("to-do-list.json", "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)
            print("Tasks saved!")


    def load(self):
        try:
            with open("to-do-list.json", "r") as file:
                load = json.load(file)
                self.tasks = [Task(**task) for task in load]
        except FileNotFoundError:
            print("Could not find to-do list")


# GUI with Tkinter
class TodoApp(tk.Tk):
    def __init__(self, todo):
        super().__init__()
        self.todo = todo
        self.title("To-Do List yay")
        
        
        # Create UI elements
        self.task_list_box = tk.Listbox(self, height=10, width=50)
        self.task_list_box.grid(row=0, column=0, columnspan=8)
        
        self.task_name_entry = tk.Entry(self, width=20)
        self.task_name_entry.grid(row=1, column=0)
        Name_label = tk.Label(self, text='Name of task', font='Arial 10')
        Name_label.grid(row=2, column=0)
        
        self.priority_entry = tk.Entry(self, width=10)
        self.priority_entry.grid(row=1, column=1)
        Priority_label = tk.Label(self, text='Priority(number scale)', font='Arial 10')
        Priority_label.grid(row=2, column=1)
        
        self.due_entry = tk.Entry(self, width=15)
        self.due_entry.grid(row=1, column=2)
        Due_label = tk.Label(self, text='Due date', font='Arial 10')
        Due_label.grid(row=2, column=2)
        
        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.grid(row=5, column=0)
        
        self.remove_button = tk.Button(self, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=5, column=1)
        
        self.check_button = tk.Button(self, text="Check Task", command=self.check_task)
        self.check_button.grid(row=5, column=2)
        
        self.save_button = tk.Button(self, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=5, column=3)
        
        self.load_button = tk.Button(self, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=5, column=4)
        
        self.update_task_list()
    
    def add_task(self):
        name = self.task_name_entry.get()
        priority = self.priority_entry.get()
        due = self.due_entry.get()
        if name and priority and due:
            self.todo.add_task(name, priority, due)
            self.update_task_list()
        else:
            messagebox.showwarning("Not all fields filled.", "Please fill out all fields.")

    def remove_task(self):
        selected_task = self.task_list_box.get(tk.ACTIVE)
        if selected_task:
            task_name = selected_task.split(",")[0].split(":")[0].strip()
            self.todo.remove_task(task_name)
            self.update_task_list()
        else:
            messagebox.showwarning("No task selected.", "Please select a task to remove.")

    def check_task(self):
        selected_task = self.task_list_box.get(tk.ACTIVE)
        if selected_task:
            task_name = selected_task.split(",")[0].split(":")[0].strip()
            self.todo.mark_task(task_name)
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to check off.")
    
    def save_tasks(self):
        self.todo.save()
        messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            self.todo.load()
            self.update_task_list()
        except FileNotFoundError:
            messagebox.showwarning("File to-do list not found or doesn't exist")

    def update_task_list(self):
        self.task_list_box.delete(0, tk.END)
        task_list = self.todo.display().strip().split("\n")
        for task in task_list:
            self.task_list_box.insert(tk.END, task)


# Create a Todo instance and a TodoApp GUI
todo = Todo()
todo_app = TodoApp(todo)
todo_app.mainloop()
