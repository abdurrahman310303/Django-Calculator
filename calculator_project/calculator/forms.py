from django import forms

class CalculatorForm(forms.Form):
    first_number = forms.FloatField(label="First Number")
    second_number = forms.FloatField(label="Second Number")
    OPERATION_CHOICES = [
        ('add', 'Addition (+)'),
        ('subtract', 'Subtraction (-)'),
        ('multiply', 'Multiplication (×)'),
        ('divide', 'Division (÷)'),
        ('modulus', 'Modulus (%)'),
    ]
    operation = forms.ChoiceField(choices=OPERATION_CHOICES, label="Operation")
