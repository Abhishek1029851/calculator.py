import tkinter as tk

def click(event):
    if entry.get() == "Error":
        entry.delete(0, tk.END)
    entry.insert(tk.END, event.widget["text"])

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#2c3e50")

entry = tk.Entry(root, font=("Consolas", 24), bd=8, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, pady=20, padx=10, ipady=10)

buttons = [
    ['C', '←', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', ]
]

colors = {
    'ops': '#f39c12',
    'num': '#34495e',
    'spec': '#c0392b',
    'bg': '#2c3e50',
    'text': 'white'
}

for row_values in buttons:
    row = tk.Frame(root, bg=colors['bg'])
    row.pack(expand=True, fill='both')
    for char in row_values:
        if char in ['+', '-', '*', '/', '%', '=']:
            bg_color = colors['ops']
        elif char in ['C', '←']:
            bg_color = colors['spec']
        else:
            bg_color = colors['num']

        btn = tk.Button(row, text=char, font=("Arial", 18), fg=colors['text'],
                        bg=bg_color, relief=tk.FLAT, activebackground="#1abc9c",
                        activeforeground="white")

        btn.pack(side=tk.LEFT, expand=True, fill='both')

        if char == '=':
            btn.bind('<Button-1>', lambda event: calculate())
        elif char == 'C':
            btn.config(command=clear)
        elif char == '←':
            btn.config(command=backspace)
        else:
            btn.bind('<Button-1>', click)

root.mainloop()

