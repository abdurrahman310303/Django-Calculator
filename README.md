# Django-Calculator

# Django Calculator

A simple calculator web application built with Django that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and modulus.

## Features
- Input two numbers and select an operation
- Supports Addition (+), Subtraction (-), Multiplication (*), Division (/), and Modulus (%)
- Displays the result after submission
- Simple and clean UI with CSS styling

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/abdurrahman310303/django-calculator.git
   cd django-calculator
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**
   ```bash
   python manage.py runserver
   ```

6. **Open in Browser**
   Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- Enter the first number in the first input field
- Select an operation from the dropdown menu
- Enter the second number in the second input field
- Click the "Calculate" button to get the result

## Project Structure
```
calculator_project/
│── calculator/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── calculator.html
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│── calculator_project/
│   ├── settings.py
│   ├── urls.py
│── manage.py
```

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contribution
If you'd like to contribute, feel free to fork the repository and submit a pull request.

---
**Author:** Your Name  
**GitHub:** [abdurrahman310303](https://github.com/abdurrahman310303)

