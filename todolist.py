# Removed unused import to avoid conflict with tkinter root
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

root.mainloop()
