from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        result = num1 + num2
        return render(request, 'result.html', {'result': result})  # You may want to create a result.html for displaying the result

    return render(request, 'home.html')  # Show the form again if it's not a

def dashboard(request):
    return render(request, 'dashboard.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    return render(request, 'pricing.html')

def action(request):
    return render(request, 'action.html')

def another_action(request):
    return render(request, 'another_action.html')

def something_else(request):
    return render(request, 'something_else.html')
