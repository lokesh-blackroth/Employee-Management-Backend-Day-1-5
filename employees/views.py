from django.http import JsonResponse


employees = [
    {
        "id": 1,
        "name": "Divya",
        "department": "Backend",
        "designation": "Python Developer"
    },
    {
        "id": 2,
        "name": "Rahul",
        "department": "Frontend",
        "designation": "React Developer"
    }
]


def health_check(request):
    return JsonResponse({
        "status": "success",
        "message": "Employee Management Backend is running"
    })


def employee_list(request):
    return JsonResponse({
        "employees": employees
    })

def employee_detail(request, id):
    for employee in employees:
        if employee["id"] == id:
            return JsonResponse(employee)

    return JsonResponse({
        "error": "Employee not found"
    }, status=404)