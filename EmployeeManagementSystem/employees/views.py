from django.shortcuts import render, redirect, get_object_or_404
from employees.models import Employee
from .forms import EmployeeForm
import pandas as pd
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

def export_employees_csv(request):
    employees = Employee.objects.all()
    data = [{
        'Name': emp.name,
        'Email': emp.email,
        'Department': emp.department,
        'Date of Joining': emp.date_of_joining,
        'Salary': emp.salary
    } for emp in employees]
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    df.to_csv(path_or_buf=response, index=False)
    return response


# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Employee Management System!")

# def employee_list(request):
#     return HttpResponse("This is the Employee List page!")

# def employee_create(request):
#     return HttpResponse("This is the Employee Create page!")

# def employee_update(request, pk):
#     return HttpResponse(f"Update Employee with ID {pk}!")

# def employee_delete(request, pk):
#     return HttpResponse(f"Delete Employee with ID {pk}!")
