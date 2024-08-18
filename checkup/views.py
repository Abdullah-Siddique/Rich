# checkup/views.py
from django.shortcuts import render
from .forms import UserProfileForm

def checkup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            bmi = profile.calculate_bmi()
            bmr = profile.calculate_bmr()
            calorie_demand = profile.calculate_calorie_demand()
            health_status = profile.health_assessment()
            return render(request, 'checkup/result.html', {
                'bmi': bmi,
                'bmr': bmr,
                'calorie_demand': calorie_demand,
                'health_status': health_status
            })
    else:
        form = UserProfileForm()

    return render(request, 'checkup/checkup.html', {'form': form})

    


