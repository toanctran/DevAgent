'''
BMI Calculator Application
'''
import tkinter as tk
from tkinter import messagebox
class BMIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BMI Calculator")
        self.geometry("300x200")
        self.weight_label = tk.Label(self, text="Weight (kg):")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()
        self.height_label = tk.Label(self, text="Height (cm):")
        self.height_label.pack()
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_bmi)
        self.calculate_button.pack()
        self.bmi_label = tk.Label(self, text="BMI:")
        self.bmi_label.pack()
        self.bmi_value_label = tk.Label(self, text="")
        self.bmi_value_label.pack()
        self.bmi_level_label = tk.Label(self, text="BMI Level:")
        self.bmi_level_label.pack()
        self.bmi_level_value_label = tk.Label(self, text="")
        self.bmi_level_value_label.pack()
        self.weight_status_label = tk.Label(self, text="Weight Status:")
        self.weight_status_label.pack()
        self.weight_status_value_label = tk.Label(self, text="")
        self.weight_status_value_label.pack()
        self.min_weight_label = tk.Label(self, text="Minimum Weight to Lose:")
        self.min_weight_label.pack()
        self.min_weight_value_label = tk.Label(self, text="")
        self.min_weight_value_label.pack()
        self.normal_bmi_label = tk.Label(self, text="Normal BMI:")
        self.normal_bmi_label.pack()
        self.normal_bmi_value_label = tk.Label(self, text="18.5 - 24.9")
        self.normal_bmi_value_label.pack()
        self.normal_weight_label = tk.Label(self, text="Normal Weight:")
        self.normal_weight_label.pack()
        self.normal_weight_value_label = tk.Label(self, text="")
        self.normal_weight_value_label.pack()
    def calculate_bmi(self):
        """
        Calculate the BMI based on the weight and height inputs.
        Update the BMI value label, BMI level label, weight status label, minimum weight label, and normal weight label.
        """
        weight_input = self.weight_entry.get()
        height_input = self.height_entry.get()
        if not weight_input.isdigit() or not height_input.isdigit():
            messagebox.showerror("Invalid Input", "Please enter valid weight and height.")
            return
        weight = float(weight_input)
        height = float(height_input) / 100
        bmi = weight / (height ** 2)
        self.bmi_value_label.config(text=str(round(bmi, 2)))
        if bmi < 18.5:
            bmi_level = "Underweight"
        elif bmi < 25:
            bmi_level = "Normal"
        elif bmi < 30:
            bmi_level = "Overweight"
        else:
            bmi_level = "Obese"
        self.bmi_level_value_label.config(text=bmi_level)
        if bmi < 18.5:
            weight_status = "Underweight"
            min_weight = round((18.5 - bmi) * (height ** 2), 2)
        elif bmi < 25:
            weight_status = "Normal"
            min_weight = 0
        elif bmi < 30:
            weight_status = "Overweight"
            min_weight = round((bmi - 24.9) * (height ** 2), 2)
        else:
            weight_status = "Obese"
            min_weight = round((bmi - 24.9) * (height ** 2), 2)
        self.weight_status_value_label.config(text=weight_status)
        self.min_weight_value_label.config(text=str(min_weight))
        normal_weight = round(22.5 * (height ** 2), 2)
        self.normal_weight_value_label.config(text=str(normal_weight))
if __name__ == "__main__":
    app = BMIApp()
    app.mainloop()