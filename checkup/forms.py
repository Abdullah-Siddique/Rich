# checkup/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'age', 'gender', 'activity_level']

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height <= 0:
            raise forms.ValidationError("Height must be greater than 0.")
        return height

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight <= 0:
            raise forms.ValidationError("Weight must be greater than 0.")
        return weight

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age <= 0:
            raise forms.ValidationError("Age must be greater than 0.")
        return age

