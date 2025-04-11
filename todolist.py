from ast import Pass
import tkinter
import random
import time
import datetime
import os

root = tkinter.Tk()
root.title("To Do List")
root.geometry("300x500")
root.resizable(False, False)
root.configure(bg="lightblue")

def add_task():
    Pass
def delete_all():
    Pass
def delete_one():
    Pass
def sort_asc():
    Pass
def sort_desc():
    Pass
def choose_random():
    Pass
def show_number_of_tasks():
    Pass

lbl_display = tkinter.Label(root, text="Simple To-Do-List", font=("Times New Roman", 15), bg="lightblue")
lbl_display.pack(pady=10)

txt_input = tkinter.Entry(root, font=("Times New Roman", 15), bg="lightblue")
txt_input.insert(0, "Enter Task Here")
txt_input.pack(pady=10)

btn_add_task = tkinter.Button(root, text="Add Task", font=("Times New Roman", 15), bg="lightblue", command=add_task)
btn_add_task.pack(pady=10)

btn_delete_all = tkinter.Button(root, text="Delete All", font=("Times New Roman", 15), bg="lightblue", command=delete_all)
btn_delete_all.pack(pady=10)

btn_delete_one = tkinter.Button(root, text="Delete One", font=("Times New Roman", 15), bg="lightblue", command=delete_one)
btn_delete_one.pack(pady=10)

btn_sort_asc = tkinter.Button(root, text="Sort Ascending", font=("Times New Roman", 15), bg="lightblue", command=sort_asc)
btn_sort_asc.pack(pady=10)

btn_sort_desc = tkinter.Button(root, text="Sort Descending", font=("Times New Roman", 15), bg="lightblue", command=sort_desc)
btn_sort_desc.pack(pady=10)

btn_choose_random = tkinter.Button(root, text="Choose Random", font=("Times New Roman", 15), bg="lightblue", command=choose_random)
btn_choose_random.pack(pady=10)

btn_show_number_of_tasks = tkinter.Button(root, text="Show Number of Tasks", font=("Times New Roman", 15), bg="lightblue", command=show_number_of_tasks)
btn_show_number_of_tasks.pack(pady=10)

btn_exit = tkinter.Button(root, text="Quit", font=("Times New Roman", 15), bg="lightblue", command=exit)
btn_exit.pack(pady=10)

lbl_tasks = tkinter.Label(root, text="Tasks", font=("Times New Roman", 15), bg="lightblue")
lbl_tasks.pack(pady=10)

lb_tasks = tkinter.Listbox(root, font=("Times New Roman", 15), bg="lightblue")
lb_tasks.pack(pady=10)

for i in range(20):
    lb_tasks.insert(tkinter.END, "Task " + str(i+1))





root.mainloop()