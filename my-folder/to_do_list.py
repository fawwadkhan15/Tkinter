import tkinter as tk

def save_event():
    event = event_entry.get()
    priority = priority_var.get()
    event_listbox.insert(tk.END, "Event: " + event + " | Priority: " + priority)

root = tk.Tk()
root.title("To-Do List")

tk.Label(root, text="Event:").pack()
event_entry = tk.Entry(root)
event_entry.pack()

tk.Label(root, text="Priority:").pack()
priority_var = tk.StringVar(root)

priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
priority_menu.pack()

save_button = tk.Button(root, text="Save", width=10, command=save_event)
save_button.pack()

event_listbox = tk.Listbox(root, width=50)
event_listbox.pack()

root.mainloop()
