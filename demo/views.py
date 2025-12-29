

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import EmployeeDetails


def demo_employee_details(request):
    demo_employee = EmployeeDetails.objects.all()
    return render(request, 'demo/index1.html', {'demo_employee':demo_employee})

def employee_detail_api(request, emp_id):
    try:
        emp = EmployeeDetails.objects.get(employee_id=emp_id)
        return JsonResponse({
            "id": emp.employee_id,
            "name": emp.name,
            "company": emp.company,
            "field": emp.field,
            "field_display": emp.get_field_display(),
            "image": emp.image.url if emp.image else None
        })
    except EmployeeDetails.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)