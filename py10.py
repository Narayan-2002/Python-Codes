import tkinter as tk
from math import factorial

def calculate_factorial():
    try:
        # Get values from entries
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        
        # Find smallest number
        smallest = min(num1, num2, num3)
        
        # Calculate factorial
        result = factorial(smallest)
        
        # Display result
        result_label.config(text=f"Factorial of {smallest} is: {result}")
        
    except ValueError:
        result_label.config(text="Please enter valid integers!")

# Create main window
root = tk.Tk()
root.title("Smallest Number Factorial Calculator")

# Create input fields
tk.Label(root, text="Number 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Number 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Number 3:").pack()
entry3 = tk.Entry(root)
entry3.pack()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_factorial)
calculate_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
