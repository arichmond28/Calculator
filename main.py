import tkinter as tk

# Function to handle button clicks
def on_button_click(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + char)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression in the entry widget
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Add an entry widget for displaying the input and results
entry = tk.Entry(root, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons in a grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=10, height=3, command=evaluate_expression).grid(row=row_val, column=col_val, columnspan=2)
    else:
        tk.Button(root, text=button, width=10, height=3, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Add a clear button
tk.Button(root, text='C', width=10, height=3, command=clear_entry).grid(row=row_val, column=2, columnspan=2)

# Run the application
root.mainloop()
