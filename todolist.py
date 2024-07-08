from tkinter import *
# a Graphical User Interface (GUI) for our Python To-Do List project.
# We will use Tkinter, Python’s standard GUI library, which is 
# included in the standard Python installation.

class ToDoList:
    def __init__(self,root):
        self.root=root
        self.task=[]
        self.listbox=Listbox(self.root)
        self.entry=Entry(self.root)
        self.addButton=Button(self.root,text="Add Task",command=self.add_task)
        self.delButton=Button(self.root,text="Delete Task",command=self.delete_task)
        
        #gui layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()
    def add_task(self):
        task=self.entry.get()
        if task !="":
            self.listbox.insert(END,task)
            self.entry.delete(0,END)
    def delete_task(self):
        try:
            task_index=self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            pass
root=Tk()
root.title("Python To Do List")
root.geometry("300x400")
to_do_list=ToDoList(root)
root.mainloop()