import tkinter as tk
from tkinter import ttk

def insert_symbol(symbol):
    """Insert symbols into the currently active input field."""
    widget = root.focus_get()
    if isinstance(widget, tk.Entry):
        widget.insert(tk.INSERT, symbol)

def dms_to_dd(d, m, s, direction):
    """Convert DMS (Degrees, Minutes, Seconds) to Decimal Degrees"""
    decimal = d + m / 60 + s / 3600
    if direction in ["S", "W"]:
        decimal *= -1
    return round(decimal, 6)

def dd_to_dms(decimal):
    """Convert Decimal Degrees to DMS (Degrees, Minutes, Seconds)"""
    direction = "N" if decimal >= 0 else "S"
    if decimal < 0:
        decimal = abs(decimal)
        direction = "S" if "N" in direction else "W"
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round((decimal - degrees - minutes / 60) * 3600, 2)
    return f"{degrees}°{minutes}′{seconds}″ {direction}"

def dd_to_dm(decimal):
    """Convert Decimal Degrees to Degrees & Minutes"""
    direction = "N" if decimal >= 0 else "S"
    if decimal < 0:
        decimal = abs(decimal)
        direction = "S" if "N" in direction else "W"
    degrees = int(decimal)
    minutes = round((decimal - degrees) * 60, 3)  # Rounded to 3 decimal places
    return f"{degrees}°{minutes}′ {direction}"

def process_input(text):
    """Process user input and handle both single and paired coordinates."""
    parts = [coord.strip() for coord in text.split(",")]
    results = []
    
    for part in parts:
        try:
            if "°" in part and "′" in part:  # DMS Input
                d, m, s, direction = part.replace("°", " ").replace("′", " ").replace("″", " ").split()
                d, m, s = int(d), int(m), float(s)
                converted = dms_to_dd(d, m, s, direction)
            elif "°" in part:  # DM Input
                d, m, direction = part.replace("°", " ").replace("′", " ").split()
                d, m = int(d), float(m)
                converted = dms_to_dd(d, m, 0, direction)
            else:  # Decimal Degrees Input
                converted = float(part)

            # Apply output format selection
            if output_format.get() == "DMS":
                results.append(dd_to_dms(converted))
            elif output_format.get() == "DM":
                results.append(dd_to_dm(converted))
            else:  # Default is Decimal Degrees
                results.append(str(converted))

        except ValueError:
            results.append("Invalid Input")

    result.set(", ".join(results))

def copy_to_clipboard():
    """Copy the result to clipboard."""
    root.clipboard_clear()
    root.clipboard_append(result.get())
    root.update()

# GUI Setup
root = tk.Tk()
VERSION = "1.0.0"
root.title(f"Coordinate Converter v{VERSION}")
root.geometry("500x400")

# Input Fields
ttk.Label(root, text="Enter Coordinates (Single or Pair):").pack()
entry = ttk.Entry(root, width=40)
entry.pack()

# Symbol Buttons
symbols_frame = ttk.Frame(root)
symbols_frame.pack()

for sym in ["°", "′", "″", "N", "S", "E", "W"]:
    ttk.Button(symbols_frame, text=sym, width=3, command=lambda s=sym: insert_symbol(s)).pack(side=tk.LEFT, padx=2)

# Dropdown for Output Format
ttk.Label(root, text="Select Output Format:").pack()
output_format = tk.StringVar(value="DD")
format_dropdown = ttk.Combobox(root, textvariable=output_format, values=["DD", "DM", "DMS"])
format_dropdown.pack()

# Convert Button
ttk.Button(root, text="Convert", command=lambda: process_input(entry.get())).pack()

# Result Display (Copyable)
result = tk.StringVar()
output_frame = ttk.Frame(root)
output_frame.pack(pady=5)

result_entry = ttk.Entry(output_frame, textvariable=result, width=40, state="readonly")
result_entry.pack(side=tk.LEFT)

ttk.Button(output_frame, text="Copy", command=copy_to_clipboard).pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
