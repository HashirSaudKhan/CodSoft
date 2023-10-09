import tkinter as tk
from tkinter import *
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title(" TO DO LIST")
root.geometry("400x300")
root.config(bg="#00BFFF")
root.resizable(0,0)

# EVENTS
# Cursor Entered
def cursor_ent_add_btn(event):
    btn_add_task.config(
        bg="#5CACEE",
        fg="White"

    )

def cursor_leav_add_btn(event):
    btn_add_task.config(
        bg="#1E90FF",
        fg="#000000"
    )

def cursor_ent_del_btn(event):
    btn_delete_task.config(
        bg="#5CACEE",
        fg="#FF0000"
    )


def cursor_leav_del_btn(event):
    btn_delete_task.config(
        bg="#1E90FF",
        fg="#000000"
    )

def cursor_ent_load_btn(event):
    btn_load_task.config(
        bg="#5CACEE",
        fg="White"
    )


def cursor_leav_load_btn(event):
    btn_load_task.config(
        bg="#1E90FF",
        fg="#000000"
    )

def cursor_ent_save_btn(event):
    btn_save_task.config(
        bg="#5CACEE",
        fg="White"
    )


def cursor_leav_save_btn(event):
    btn_save_task.config(
        bg="#1E90FF",
        fg="#000000"
    )

# ADD result function
def add_task():
    get_task = entry_task.get()  # getting text from entry
    if get_task != "":
        listbox_tasks.insert(tk.END, get_task)  # saving task in list_box
        entry_task.delete(0, tk.END)  # delete the value remaining in entry
    else:
        tk.messagebox.showwarning("Warning", "You must enter a task")

# Delete result function
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tk.messagebox.showwarning("Warning", "You have to must select a task")


# LOAD result function
def load_task():
    all_task = pickle.load(open('All_task_data', 'rb'))  # rb means read binary
    listbox_tasks.delete(0, tk.END)
    for task in all_task:
        listbox_tasks.insert(tk.END, task)

# SAVE result function


def save_task():
    all_tasks = listbox_tasks.get(0, listbox_tasks.size())
    # open a file, where you want to store the data
    file = open('All_task_data', 'wb')  # wb means writing binary
    # dump information to that file
    pickle.dump(all_tasks, file)
    # close the file
    file.close()
    tk.messagebox.showinfo("Info", "Your data has been saved")
    


# FRAMES
Listbox_scrollbar_frame = tk.Frame(root)
Listbox_scrollbar_frame.pack(expand=TRUE,fill="both")

entry_task_frame = tk.Frame(root)
entry_task_frame.pack(expand=TRUE,fill="both")

add_and_delete_btn_frame = tk.Frame(root)
add_and_delete_btn_frame.pack(expand=TRUE,fill="both")

load_and_save_btn_frame = tk.Frame(root)
load_and_save_btn_frame.pack(expand=TRUE,fill="both")

# GUI
# LISTBOX
listbox_tasks = tk.Listbox(
    Listbox_scrollbar_frame,
    height=10,
    width=63,
    bg="#F0F0F0"
)
listbox_tasks.pack(side=LEFT)


# SCROLLBAR
Scrollbar_task = tk.Scrollbar(Listbox_scrollbar_frame)
Scrollbar_task.pack(side=RIGHT, fill=tk.Y)

# For scrollbar working with listbox item
listbox_tasks.config(yscrollcommand=Scrollbar_task.set)
Scrollbar_task.config(command=listbox_tasks.yview)

# ENTRY
entry_task = tk.Entry(entry_task_frame,width=52)
entry_task.pack(fill="both")

# ADD BUTTON
btn_add_task = tk.Button(
    add_and_delete_btn_frame,
    text="Add Task",
    height=2,
    font="bold",
    bg="#1E90FF",
    command=add_task
)
btn_add_task.pack(expand=TRUE,side=LEFT,fill="both")
btn_add_task.bind("<Enter>", cursor_ent_add_btn)
btn_add_task.bind("<Leave>", cursor_leav_add_btn)

# Delete BUTTON
btn_delete_task = tk.Button(
    add_and_delete_btn_frame,
    text="Del  Task",
    height=2,
    font="bold",
    bg="#1E90FF",
    command=delete_task
)
btn_delete_task.pack(expand=TRUE,side=LEFT,fill="both")
btn_delete_task.bind("<Enter>", cursor_ent_del_btn)
btn_delete_task.bind("<Leave>", cursor_leav_del_btn)

# LOAD BUTTON
btn_load_task = tk.Button(
    load_and_save_btn_frame,
    text="View Task",
    height=2,
    font="bold",
    bg="#1E90FF",
    command=load_task
)
btn_load_task.pack(expand=TRUE,side=LEFT,fill="both")
btn_load_task.bind("<Enter>", cursor_ent_load_btn)
btn_load_task.bind("<Leave>", cursor_leav_load_btn)

# SAVE BUTTON
btn_save_task = tk.Button(
    load_and_save_btn_frame,
    text="Save Task",
    height=2,
    font="bold",
    bg="#1E90FF",
    command=save_task
)
btn_save_task.pack(expand=TRUE,side=LEFT,fill="both")
btn_save_task.bind("<Enter>", cursor_ent_save_btn)
btn_save_task.bind("<Leave>", cursor_leav_save_btn)


root.mainloop()
