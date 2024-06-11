import tkinter as tk 
from tkinter import messagebox
import pickle

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def view_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_text = task_list.get(selected_task[0])
        messagebox.showinfo("Task Details", f"Task: {task_text}")
    else:
        messagebox.showwarning("Warning", "Select a task to view details.")

def mark_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task[0], {'bg': 'White'})
    else:
        messagebox.showwarning("Warning", "Select a task to mark as done.")

def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)
    messagebox.showinfo("Saved", "Tasks loading completed.")

def load_tasks():
    try:
        with open("tasks.pkl", "rb") as file:
            tasks = pickle.load(file)
            task_list.delete(0, tk.END)
            for task in tasks:
                task_list.insert(tk.END, task)
        messagebox.showinfo("Loaded", "Tasks loading completed.")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No Saved tasks are found.")

root = tk.Tk()
root.title("To-Do List App")

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

view_button = tk.Button(root, text="View Task", command=view_task)
view_button.pack()

mark_button = tk.Button(root, text="Mark Task", command=mark_task)
mark_button.pack()

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack()

task_list = tk.Listbox(root)
task_list.pack()

root.mainloop()
