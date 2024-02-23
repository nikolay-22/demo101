from django.shortcuts import render, redirect

from demo101.formsbasics.forms import EmployeeForm, EmployeeModelForm
from demo101.formsbasics.models import Employee


def index_forms(request):
    ### Simpler version:
    form = EmployeeForm(request.POST or None) # if method is get, we'll receive an empty form object
    if request.method == "POST":
        if form.is_valid():  # it will return and populate cleaned_data, which means validated data
            print(form.cleaned_data)
            return redirect('index_forms')
    context = {"employee_form": form}
    return render(request, "formsbasics/index_forms.html", context=context)

    ### full code
    # if request.method == "GET":
    #     context={
    #         "employee_form": EmployeeForm(),
    #     }
    #     # print(request.POST['last_name'])
    #     return render(request, "formsbasics/index_forms.html", context=context)
    # else: #request.method == "GET"
    #     form = EmployeeForm(request.POST)
    #     if form.is_valid(): # it will return and populate cleaned_data, which means validated data
    #         print(form.cleaned_data['last_name'])
    #         return redirect('index_forms')
    #     else: # data is invalid populates errors
    #         context = {
    #             "employee_form": form,
    #         }
    #         return render(request, "formsbasics/index_forms.html", context=context)


def index_mforms(request):
    employee_model_form = EmployeeModelForm(request.POST or None)
    if request.method == "POST":
        if employee_model_form.is_valid():
            print(employee_model_form.cleaned_data['department']) # the field does not exist in the DB
            employee_model_form.save()
            return redirect('index_mforms')

    employees_list = Employee.objects.all()

    context = {
        # "employee_normal_form": EmployeeForm(),
        # "employee_model_form": EmployeeModelForm(),
        "employee_model_form":  employee_model_form,
        "employees_list": employees_list,
    }
    return render(request, "formsbasics/index_mforms.html", context=context)
    # ### Simpler version:
    # form = EmployeeForm(request.POST or None) # if method is get, we'll receive an empty form object
    # if request.method == "POST":
    #     if form.is_valid():  # it will return and populate cleaned_data, which means validated data
    #         print(form.cleaned_data)
    #         return redirect('index_forms')
    # context = {"employee_form": form}
    # return render(request, "formsbasics/index_forms.html", context=context)


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == "GET":
        employee_model_form = EmployeeModelForm(instance=employee)
    else:
        employee_model_form = EmployeeModelForm(request.POST, instance=employee)
        if employee_model_form.is_valid():
            employee_model_form.save()
            return redirect('index_mforms')

    employees_list = Employee.objects.all()

    context = {
        "employee_model_form": employee_model_form,
        "employee": employee,
    }

    return render(request, "formsbasics/employee_details.html", context=context)