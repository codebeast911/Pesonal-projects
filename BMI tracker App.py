import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        name = name_entry.get()
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        bmi = weight / (height ** 2)
        result_text = f"Hello {name}, Age: {age}\nYour BMI is: {bmi:.2f}\n"
        
        if bmi < 18.5:
            result_text += "You are underweight. Consider a balanced diet with more nutritious food."
        elif bmi > 29:
            result_text += "You are obese. It's advisable to consult a healthcare provider for a healthy lifestyle plan."
        elif bmi > 24.5:
            result_text += "You are overweight. Regular exercise and a balanced diet can help maintain a healthy BMI."
        else:
            result_text += "Your BMI is normal. Keep up the healthy lifestyle!"
        
        messagebox.showinfo("BMI Result", result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for age, weight, and height.")

# Creating main window
root = tk.Tk()
root.title("BMI Tracker")
root.geometry("400x400")
root.configure(bg="#ADD8E6")  # Light Blue Background

# Styling
frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20, relief=tk.RIDGE, borderwidth=5)
frame.pack(pady=20)

title_label = tk.Label(frame, text="BMI Tracker", font=("Inter", 16, "bold"), bg="#FFFFFF")
title_label.pack()

tk.Label(frame, text="Name:", bg="#FFFFFF").pack()
name_entry = tk.Entry(frame)
name_entry.pack()

tk.Label(frame, text="Age:", bg="#FFFFFF").pack()
age_entry = tk.Entry(frame)
age_entry.pack()

tk.Label(frame, text="Weight (kg):", bg="#FFFFFF").pack()
weight_entry = tk.Entry(frame)
weight_entry.pack()

tk.Label(frame, text="Height (m):", bg="#FFFFFF").pack()
height_entry = tk.Entry(frame)
height_entry.pack()

# Calculate button
calc_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi, bg="#87CEEB", font=("Arial", 12, "bold"), relief=tk.GROOVE)
calc_button.pack(pady=10)

# Run the app
root.mainloop()
