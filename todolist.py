import tkinter
import random

root = tkinter.Tk()
root.title("To Do List")
root.geometry("400x800")
root.resizable(False, False)
root.configure(bg="lightblue")

# Create a list to store tasks
tasks = []

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task) 

def add_task():
    update_listbox()
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        txt_input.delete(0, "end")
        clear_listbox()
        update_listbox()
    else:
        lb_tasks.delete(0, "end")
        lb_tasks.insert("end", "Please enter a task")

def clear_listbox():
    lb_tasks.delete(0, "end")

def delete_all():
    global tasks
    tasks = []
    clear_listbox()

def delete_one():
    try:
        selected_task_index = lb_tasks.curselection()[0]
        tasks.pop(selected_task_index)
        clear_listbox()
        update_listbox()
    except IndexError:
        pass  
def sort_asc():
    global tasks
    tasks.sort()
    clear_listbox()
    update_listbox()

def sort_desc():
    global tasks
    tasks.sort(reverse=True)
    clear_listbox()
    update_listbox()

def choose_random():
    if tasks:
        random_task = random.choice(tasks)
        lb_tasks.delete(0, "end")
        lb_tasks.insert("end", random_task)
    else:
        lb_tasks.delete(0, "end")
        lb_tasks.insert("end", "No tasks available")
        
def show_number_of_tasks():
    task_count = len(tasks)
    lb_tasks.delete(0, "end")
    lb_tasks.insert("end", f"Number of tasks: {task_count}")

lbl_display = tkinter.Label(root, text="Simple To-Do-List", font=("Times New Roman", 8), bg="lightblue")
lbl_display.pack(pady=10)

txt_input = tkinter.Entry(root, font=("Times New Roman", 8), bg="lightblue")
txt_input.insert(0, "Enter Task Here")
txt_input.pack(pady=10)

btn_add_task = tkinter.Button(root, text="Add Task", font=("Times New Roman", 8), bg="lightblue", command=add_task)
btn_add_task.pack(pady=10)

btn_delete_all = tkinter.Button(root, text="Delete All", font=("Times New Roman", 8), bg="lightblue", command=delete_all)
btn_delete_all.pack(pady=10)

btn_delete_one = tkinter.Button(root, text="Delete", font=("Times New Roman", 8), bg="lightblue", command=delete_one)
btn_delete_one.pack(pady=10)

btn_sort_asc = tkinter.Button(root, text="Sort Ascending", font=("Times New Roman", 8), bg="lightblue", command=sort_asc)
btn_sort_asc.pack(pady=10)

btn_sort_desc = tkinter.Button(root, text="Sort Descending", font=("Times New Roman", 8), bg="lightblue", command=sort_desc)
btn_sort_desc.pack(pady=10)

btn_choose_random = tkinter.Button(root, text="Choose Random", font=("Times New Roman", 8), bg="lightblue", command=choose_random)
btn_choose_random.pack(pady=10)

btn_show_number_of_tasks = tkinter.Button(root, text="Show Number of Tasks", font=("Times New Roman", 8), bg="lightblue", command=show_number_of_tasks)
btn_show_number_of_tasks.pack(pady=10)

btn_exit = tkinter.Button(root, text="Quit", font=("Times New Roman", 8), bg="lightblue", command=exit)
btn_exit.pack(pady=10)

lbl_tasks = tkinter.Label(root, text="Tasks", font=("Times New Roman", 8), bg="lightblue")
lbl_tasks.pack(pady=10)

lb_tasks = tkinter.Listbox(root, font=("Times New Roman", 8), bg="lightblue", selectmode=tkinter.SINGLE, height=10, width=25)
lb_tasks.pack(pady=10)

root.mainloop()