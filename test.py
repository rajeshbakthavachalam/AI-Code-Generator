from tkinter import *

# Define functions FIRST
def add_task():
    task = task_entry.get()
    if task:  # Only add if the entry is not empty
        task_list.insert(END, task)
        task_entry.delete(0, END)  # Clear the entry box

def delete_task():
    try:
        selected_task = task_list.curselection()[0]  # Get selected task index
        task_list.delete(selected_task)
    except IndexError:
        pass  # Do nothing if no task is selected

def mark_task_completed():
    try:
        selected_task = task_list.curselection()[0]
        task_list.itemconfig(selected_task, {'fg': 'gray'})  # Gray out completed task
    except IndexError:
        pass  # Do nothing if no task is selected

# Create the main window
root = Tk()
root.title("To-Do List App")

# Create widgets
task_list = Listbox(root)
task_list.pack()

task_entry = Entry(root)
task_entry.pack()

# Buttons (now functions are defined above)
add_button = Button(root, text="Add Task", command=add_task)
delete_button = Button(root, text="Delete Task", command=delete_task)
mark_completed_button = Button(root, text="Mark Completed", command=mark_task_completed)

# Pack buttons
add_button.pack()
delete_button.pack()
mark_completed_button.pack()

# Run the app
root.mainloop()