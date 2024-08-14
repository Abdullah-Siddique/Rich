from django.shortcuts import render
tasks = ["Abdullah", "Reza", "Siddique"]
# Create your views here.
def index(request):
    return render(request, "task/index.html", {"tasks": tasks})
