import tkinter as tk

# Create the main window (root)
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Create an entry widget to display the numbers and result
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Define button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))  # Evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create the buttons and place them on the grid
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=button_clear)
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: button_click(t))

    button.grid(row=row, column=col)

# Run the application
root.mainloop()
