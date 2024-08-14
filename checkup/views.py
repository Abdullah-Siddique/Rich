# checkup/views.py
from django.shortcuts import render
from .forms import UserProfileForm

def checkup_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            bmi = user_profile.calculate_bmi()
            bmr = user_profile.calculate_bmr()
            health_status = user_profile.health_assessment()
            return render(request, 'checkup/result.html', {
                'bmi': bmi,
                'bmr': bmr,
                'health_status': health_status,
            })
    else:
        form = UserProfileForm()

    return render(request, 'checkup/checkup.html', {'form': form})
    


