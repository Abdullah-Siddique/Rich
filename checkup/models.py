# checkup/models.py
from django.db import models

class UserProfile(models.Model):
    ACTIVITY_LEVEL_CHOICES = [
        ('little', 'Little/no exercise'),
        ('light', 'Light exercise'),
        ('moderate', 'Moderate exercise (3-5 days/wk)'),
        ('active', 'Very active (6-7 days/wk)'),
        ('extra', 'Extra active (very active & physical job)'),
    ]

    height = models.FloatField(help_text="Height in centimeters")
    weight = models.FloatField(help_text="Weight in kilograms")
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_LEVEL_CHOICES, default='little')

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        return self.weight / (height_in_meters ** 2)

    def calculate_bmr(self):
        if self.gender == 'male':
            return 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        elif self.gender == 'female':
            return 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

    def calculate_calorie_demand(self):
        bmr = self.calculate_bmr()
        activity_multipliers = {
            'little': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'extra': 1.9
        }
        return bmr * activity_multipliers.get(self.activity_level, 1.2)

    def health_assessment(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"







        



        

