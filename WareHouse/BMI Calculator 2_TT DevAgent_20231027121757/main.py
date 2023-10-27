'''
This is the main file of the BMI calculator application.
It imports the necessary modules and creates the GUI.
'''
import tkinter as tk
from tkinter import messagebox
from bmi_calculator import BMICalculator
class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.height_label = tk.Label(root, text="Height (cm):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()
        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_bmi)
        self.calculate_button.pack()
        self.bmi_label = tk.Label(root, text="BMI:")
        self.bmi_label.pack()
        self.bmi_value = tk.Label(root, text="")
        self.bmi_value.pack()
        self.bmi_level_label = tk.Label(root, text="BMI Level:")
        self.bmi_level_label.pack()
        self.bmi_level_value = tk.Label(root, text="")
        self.bmi_level_value.pack()
        self.weight_status_label = tk.Label(root, text="Weight Status:")
        self.weight_status_label.pack()
        self.weight_status_value = tk.Label(root, text="")
        self.weight_status_value.pack()
        self.normal_bmi_label = tk.Label(root, text="Normal BMI:")
        self.normal_bmi_label.pack()
        self.normal_bmi_value = tk.Label(root, text="")
        self.normal_bmi_value.pack()
        self.normal_weight_label = tk.Label(root, text="Normal Weight:")
        self.normal_weight_label.pack()
        self.normal_weight_value = tk.Label(root, text="")
        self.normal_weight_value.pack()
    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            if not height or not weight:
                messagebox.showerror("Error", "Please enter valid height and weight.")
                return
            if height == 0:
                messagebox.showerror("Error", "Height cannot be zero.")
                return
            bmi_calculator = BMICalculator()
            bmi = bmi_calculator.calculate_bmi(height, weight)
            bmi_level = bmi_calculator.get_bmi_level(bmi)
            weight_status = bmi_calculator.get_weight_status(bmi)
            normal_bmi = bmi_calculator.get_normal_bmi()
            normal_weight = bmi_calculator.get_normal_weight(height)
            self.bmi_value.config(text=str(bmi))
            self.bmi_level_value.config(text=bmi_level)
            self.weight_status_value.config(text=weight_status)
            self.normal_bmi_value.config(text=str(normal_bmi))
            self.normal_weight_value.config(text=str(normal_weight))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid height and weight.")
if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()