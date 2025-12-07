import tkinter as tk
from tkinter import ttk, messagebox


root = tk.Tk()
root.title("Binary Arithmetic Calculator")
root.geometry("550x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Binary Arithmetic Calculator",
                       font=("Arial", 16, "bold"))
title_label.pack(pady=10)


frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter first integer:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
first_entry = tk.Entry(frame, font=("Arial", 12))
first_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Enter second integer:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
second_entry = tk.Entry(frame, font=("Arial", 12))
second_entry.grid(row=1, column=1, padx=10, pady=5)


tk.Label(frame, text="Select Operation:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)

operation_var = tk.StringVar()
operation_combo = ttk.Combobox(frame, textvariable=operation_var,
                               values=["Addition", "Subtraction", "Multiplication", "Division"],
                               state="readonly", font=("Arial", 12), width=17)
operation_combo.grid(row=2, column=1, padx=10, pady=5)
operation_combo.current(0)


first_bin_label = tk.Label(root, text="First number in binary: ", font=("Arial", 12))
first_bin_label.pack(pady=5)

second_bin_label = tk.Label(root, text="Second number in binary: ", font=("Arial", 12))
second_bin_label.pack(pady=5)

result_label = tk.Label(root, text="Result in binary: | Result in integer:", font=("Arial", 12, "bold"))
result_label.pack(pady=10)


def calculate():
    try:
        a = int(first_entry.get())
        b = int(second_entry.get())
        op = operation_var.get()

        # Convert to binary
        a_bin = bin(a)[2:]
        b_bin = bin(b)[2:]

        # Perform operation
        if op == "Addition":
            result = a + b
        elif op == "Subtraction":
            result = a - b
        elif op == "Multiplication":
            result = a * b
        elif op == "Division":
            if b == 0:
                messagebox.showerror("Math Error", "Division by zero is not allowed.")
                return
            result = a // b  

        result_bin = bin(result)[2:] if result >= 0 else "-" + bin(abs(result))[2:]

        first_bin_label.config(text=f"First number in binary: {a_bin}")
        second_bin_label.config(text=f"Second number in binary: {b_bin}")
        result_label.config(text=f"Result in binary: {result_bin} | Result in integer: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers.")

def clear():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    first_bin_label.config(text="First number in binary: ")
    second_bin_label.config(text="Second number in binary: ")
    result_label.config(text="Result in binary: | Result in integer: ")


button_frame = tk.Frame(root)
button_frame.pack(pady=15)

calc_button = tk.Button(button_frame, text="Calculate", command=calculate,
                        width=12, font=("Arial", 12))
calc_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear,
                         width=12, font=("Arial", 12))
clear_button.grid(row=0, column=1, padx=10)

root.mainloop()
