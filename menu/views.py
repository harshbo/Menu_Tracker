from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Lunch, Day, Snacks, BreakFast, Supper
from .forms import BreakfastForm, LunchForm, SnacksForm, SupperForm


def addData(request, type, day):
    if type == 'breakfast':
        dayObj = Day.objects.get(name=day.title())
        try:
            instance = get_object_or_404(BreakFast, day=dayObj)
        except Http404:
            instance = None
        if request.method == 'POST':
            form = BreakfastForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = BreakfastForm()

    elif type == 'lunch':
        dayObj = Day.objects.get(name=day.title())
        try:
          
          instance = get_object_or_404(Lunch, day=dayObj)
        except Http404:
            instance = None
        if request.method == 'POST':
            form = LunchForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = LunchForm()

    elif type == 'snacks':
        dayObj = Day.objects.get(name=day.title())
        try:
            instance = get_object_or_404(Snacks, day=dayObj)
        except Http404:
            instance = None
        if request.method == 'POST':
            form = SnacksForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = SnacksForm()

    elif type == 'supper':
        dayObj = Day.objects.get(name=day.title()) 
        try:
            instance = get_object_or_404(Supper, day=dayObj)
        except Http404:
            instance = None
        if request.method == 'POST':
            form = SupperForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = SupperForm()

    return render(request, 'menu/form.html', {'form': form})


def get(request):
    data = Lunch.objects.all()
    context = {"Menu": data}
    return render(request, 'menu/base.html', context)


def home(request):
    context = {}
    context['days'] = [
        'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday'
    ]
    context['sessions'] = ['Breakfast', 'Lunch', 'Snacks', 'Supper']

    if request.method == 'POST':
        day = request.POST['day']
        session = request.POST['session']

        if day not in context['days'] or session not in context['sessions']:
            context['error'] = 'Please select valid day and session'
            return render(request, 'menu/home.html', context)

        dayObj = Day.objects.get(name=day)

        if session == 'Lunch':
            data2 = Lunch.objects.get(day=dayObj)
            return render(request, 'menu/base.html', {"data2": data2})

        if session == 'Snacks':
            data3 = Snacks.objects.get(day=dayObj)
            return render(request, 'menu/base.html', {"data3": data3})

        if session == 'Breakfast':
            data1 = BreakFast.objects.get(day=dayObj)
            return render(request, 'menu/base.html', {"data1": data1})

        if session == 'Supper':
            data4 = Supper.objects.get(day=dayObj)
            return render(request, 'menu/base.html', {"data4": data4})

    return render(request, 'menu/home.html', context)
