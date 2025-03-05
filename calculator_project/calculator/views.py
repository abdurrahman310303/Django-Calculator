from django.shortcuts import render
from .forms import CalculatorForm

def calculator_view(request):
    result = None
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['first_number']
            num2 = form.cleaned_data['second_number']
            operation = form.cleaned_data['operation']
            
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            elif operation == "modulus":
                result = num1 % num2 if num2 != 0 else "Error: Modulus by zero"
    else:
        form = CalculatorForm()

    return render(request, "calculator/calculator.html", {"form": form, "result": result})
