from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse

def home(request):
    return render(request, 'websites/index.html')

def about(request):
    return render(request, 'websites/about.html')

def contact(request):
    return render(request, 'websites/contact.html')

def simple_api(request):
    if request.method == "GET":
        return JsonResponse({"message": "GET request successful"})
    return JsonResponse({"error": "Only GET allowed"}, status=405)



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def employee_api(request, emp_id):
    # GET request
    if request.method == "GET":
        return JsonResponse({
            "employee_id": emp_id,
            "role": "Data Engineer"
        })

    # POST request
    elif request.method == "POST":
        try:
            body = json.loads(request.body)

            name = body.get("name")
            role = body.get("role", "Data Engineer")

            return JsonResponse({
                "message": "Employee data received",
                "employee_id": emp_id,
                "name": name,
                "role": role
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON"},
                status=400
            )

    # Other methods not allowed
    return JsonResponse(
        {"error": "Method not allowed"},
        status=405
    )
