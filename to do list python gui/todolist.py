import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('todo app')
root.geometry('500x500')
root.resizable(False,False)
root.iconbitmap('1486504314-check-list-item-item-list-to-do-ui-shopping_81331.ico')

tasklist = []

def open_tasks():
    try:
        with open('tasklist.txt', 'r') as file:
            tasks = file.readlines()

        for task in tasks:
            if task != '\n':
                tasklist.append(task)
                listbox.insert(tk.END, task)
    except:
        with open('tasklist.txt', 'w') as file:
            pass

def add_task(event):
    task = task_enrty.get()
    task_enrty.delete(0,tk.END)
    if task:
        with open('tasklist.txt', 'a') as file:
            file.write(f'\n{task}')
        listbox.insert(tk.END,task)
        tasklist.append(task)

def delet_task():
    global tasklist
    task = str(listbox.get(tk.ANCHOR))
    if task in tasklist:
        tasklist.remove(task)
        with open('tasklist.txt', 'w') as file:
            for task in tasklist:
                file.write(f'{task}\n')
        listbox.delete(tk.ANCHOR)

heading = ttk.Label(root,text='Tasks',font='arial 25 bold')
heading.pack()

frame = ttk.Frame(root,width='500',height='50')
frame.pack(pady='20')

task = tk.StringVar()

task_enrty = ttk.Entry(frame,font='12',width='25')
task_enrty.pack()
task_enrty.focus()
 
task_enrty.bind("<Return>", add_task)

frame1 = ttk.Frame(root,width='500',height='300')
frame1.pack()

listbox = tk.Listbox(frame1,font='arial 15',width='40',height='12')
listbox.pack()

open_tasks()

s = ttk.Style()
s.configure('TButton', font=('arial', 12))

complete = ttk.Button(root,text='complete',command=delet_task)
complete.pack(side='bottom',pady='25',ipady='10',ipadx='15')

root.mainloop()