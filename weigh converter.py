# Import tkinter module
import tkinter as tk
from tkinter import *

# Create the main window
app = Tk()
app.title("Weight Converter App")
app.geometry("500x500")

# Add a title label
Label(app, text="Weight Converter Tool", font=("Arial", 20), bg="darkblue", fg='white').pack()

# Define variable for input weight in kilograms
weight_kg = tk.IntVar()

def to_grams():
    kg_value = weight_kg.get()  # Get the input value in kg
    grams = float(kg_value) * 1000  # Convert to grams
    Label(app, text="Equivalent weight in grams:", font=("Arial", 12)).pack()
    Label(app, text=grams, bg="green", font=("Arial", 10)).pack()

def to_ounces():
    kg_value = weight_kg.get()  # Get the input value in kg
    ounces = float(kg_value) * 35.274  # Convert to ounces
    Label(app, text="Equivalent weight in ounces:", font=("Arial", 12)).pack()
    Label(app, text=ounces, bg="green", font=("Arial", 10)).pack()

def to_pounds():
    kg_value = weight_kg.get()  # Get the input value in kg
    pounds = float(kg_value) * 2.20462  # Convert to pounds
    Label(app, text="Equivalent weight in pounds:", font=("Arial", 12)).pack()
    Label(app, text=pounds, bg="green", font=("Arial", 10)).pack()

# Label and entry for weight input
Label(app, text="Enter weight in kilograms:", font=("Arial", 14)).pack()
Entry(app, textvariable=weight_kg).pack()

# Buttons for conversions
Button(app, text="Convert to Grams", bg="darkgreen", fg="white", command=to_grams).pack(pady=5)
Button(app, text="Convert to Ounces", bg="darkgreen", fg="white", command=to_ounces).pack(pady=5)
Button(app, text="Convert to Pounds", bg="darkgreen", fg="white", command=to_pounds).pack(pady=5)

app.mainloop()
