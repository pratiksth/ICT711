import tkinter as tk
from tkinter import ttk

# Conversion functions for different units
def length_conversion(value, from_unit, to_unit):
    # Convert input value to centimeters first
    if from_unit == "Centimeters":
        cm_value = value
    elif from_unit == "Millimeters":
        cm_value = value / 10
    elif from_unit == "Inches":
        cm_value = value * 2.54
    elif from_unit == "Feet":
        cm_value = value * 30.48

    # Now convert from centimeters to the desired output unit
    if to_unit == "Centimeters":
        return cm_value
    elif to_unit == "Millimeters":
        return cm_value * 10
    elif to_unit == "Inches":
        return cm_value / 2.54
    elif to_unit == "Feet":
        return cm_value / 30.48

# Function to perform the conversion based on the selected input and output units
def convert_length():
    input_value = float(entry.get())
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    
    result = length_conversion(input_value, from_unit, to_unit)
    result_label.config(text=f"Result: {result:.2f} {to_unit.lower()}")

# Creating the main window
root = tk.Tk()
root.title("Length Unit Converter")

# Creating a label and entry field for input
tk.Label(root, text="Enter the length:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for input units (from)
from_unit_var = tk.StringVar()
from_unit_var.set("Centimeters")  # Default input unit
from_dropdown = ttk.Combobox(root, textvariable=from_unit_var)
from_dropdown['values'] = ("Centimeters", "Millimeters", "Inches", "Feet")
from_dropdown.grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="From").grid(row=1, column=1)

# Dropdown for output units (to)
to_unit_var = tk.StringVar()
to_unit_var.set("Millimeters")  # Default output unit
to_dropdown = ttk.Combobox(root, textvariable=to_unit_var)
to_dropdown['values'] = ("Centimeters", "Millimeters", "Inches", "Feet")
to_dropdown.grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="To").grid(row=2, column=1)

# Button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_length)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Running the main event loop
root.mainloop()
