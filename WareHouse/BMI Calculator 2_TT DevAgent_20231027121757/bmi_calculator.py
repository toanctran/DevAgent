'''
This file contains the BMICalculator class which performs the BMI calculations.
'''
class BMICalculator:
    def calculate_bmi(self, height, weight):
        '''
        Calculates the BMI using the given height and weight.
        '''
        if height == 0:
            raise ValueError("Height cannot be zero.")
        bmi = weight / ((height / 100) ** 2)
        return round(bmi, 2)
    def get_bmi_level(self, bmi):
        '''
        Returns the BMI level based on the calculated BMI.
        '''
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    def get_weight_status(self, bmi):
        '''
        Returns the weight status based on the calculated BMI.
        '''
        if bmi < 18.5:
            return "You are underweight."
        elif bmi < 25:
            return "You have a normal weight."
        elif bmi < 30:
            return "You are overweight."
        else:
            return "You are obese."
    def get_normal_bmi(self):
        '''
        Returns the normal BMI range.
        '''
        return "18.5 - 24.9"
    def get_normal_weight(self, height):
        '''
        Returns the normal weight range based on the given height.
        '''
        normal_weight_min = 18.5 * ((height / 100) ** 2)
        normal_weight_max = 24.9 * ((height / 100) ** 2)
        return f"{round(normal_weight_min, 2)} - {round(normal_weight_max, 2)}"