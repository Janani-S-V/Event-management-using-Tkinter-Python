import tkinter
from tkinter import *
root = Tk()
root.configure(bg="purple")
root.title("To do list")
root.geometry("200x300")
events = []
def update_listbox():
    clear_listbox()
    for event in events:
        ltasks.insert("end", event)
        
def clear_listbox():
    ltasks.delete(0, "end")
    
def add():
    event_name = input.get()
    if event_name != "":
        events.append(event_name)
        update_listbox()
    else:
        display["text"] = "Please enter any event"
    input.delete(0, "end")

def dele():
    display["text"] = "Please enter any event"
    event = ltasks.get("active")
    if event in events:
        events.remove(event)
    update_listbox()
    
def total():
    total_event = len(events)
    msg = "Number of events:%s" % total_event
    display["text"] = msg

display = Label(root, text="Event Management", bg="skyblue")
display.pack()
input = Entry(root, width=15)
input.pack()
add_event = Button(root, text="Event name ", width=12, bg="pink",height=1, command=add)
add_event.pack()
add_date = Button(root, text="Date ", width=12, bg="pink",height=1)
add_date.pack()
total_event = Button(root, text="Total", width=12,bg="pink", height=1, command=total)
total_event.pack()
del_event = Button(root, text="Remove", width=12, bg="pink",height=1, command=dele)
del_event.pack()
quit_event = Button(root, text="Exit", width=12,bg="pink", height=1, command=exit)
quit_event.pack()
ltasks = Listbox(root)
ltasks.pack()
root.mainloop()
