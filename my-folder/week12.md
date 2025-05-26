import tkinter as tk

counter_value = 0

def update_label():
    label.config(text=str(counter_value))

def increment():
    global counter_value
    counter_value += 1
    update_label()

def decrement():
    global counter_value
    counter_value -= 1
    update_label()

def reset():
    global counter_value
    counter_value = 0
    update_label()

root = tk.Tk()
root.title("Simple Counter")

heading = tk.Label(root, text="Counter")
heading.pack(pady=10)

label = tk.Label(root, text=str(counter_value))
label.pack(pady=10)

btn_minus = tk.Button(text="-", width=5, command=decrement)
btn_minus.pack(side="left", padx=20, pady=20)
btn_reset = tk.Button(text="Reset", width=7, command=reset)
btn_reset.pack(side="left", padx=20, pady=20)
btn_plus = tk.Button(text="+", width=5, command=increment)
btn_plus.pack(side="left", padx=20, pady=20)
root.mainloop()
