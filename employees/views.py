import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Employee
from .forms import EmployeeForm


def health_check(request):
    return JsonResponse({
        "status": "success",
        "message": "Employee Management Backend is running"
    })


@csrf_exempt
@require_http_methods(["GET", "POST"])
def employee_list(request):

    # READ - Get all employees
    if request.method == "GET":
        employees = Employee.objects.all()

        data = [
            model_to_dict(employee)
            for employee in employees
        ]

        return JsonResponse({
            "status": "success",
            "employees": data
        })

    # CREATE - Create employee
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            "status": "error",
            "message": "Invalid JSON data"
        }, status=400)

    form = EmployeeForm(data)

    if form.is_valid():
        employee = form.save()

        return JsonResponse({
            "status": "success",
            "message": "Employee created successfully",
            "employee": model_to_dict(employee)
        }, status=201)

    return JsonResponse({
        "status": "error",
        "errors": form.errors
    }, status=400)


@csrf_exempt
@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def employee_detail(request, id):

    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Employee not found"
        }, status=404)

    # READ - Get single employee
    if request.method == "GET":
        return JsonResponse({
            "status": "success",
            "employee": model_to_dict(employee)
        })

    # UPDATE
    if request.method in ["PUT", "PATCH"]:
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON data"
            }, status=400)

        form = EmployeeForm(
            data,
            instance=employee
        )

        if form.is_valid():
            employee = form.save()

            return JsonResponse({
                "status": "success",
                "message": "Employee updated successfully",
                "employee": model_to_dict(employee)
            })

        return JsonResponse({
            "status": "error",
            "errors": form.errors
        }, status=400)

    # DELETE
    if request.method == "DELETE":
        employee.delete()

        return JsonResponse({
            "status": "success",
            "message": "Employee deleted successfully"
        })