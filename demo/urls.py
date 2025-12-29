
from django.contrib import admin
from django.urls import path, include
from . import views

# http://127.0.0.1:8000/demo/employeedetails/
# http://127.0.0.1:8000/demo/employeedetails/api/101/

urlpatterns = [

    path('', views.demo_employee_details, name='home'),

    path('employeedetails/', views.demo_employee_details, name = 'demo_employee_details'),
    path('employeedetails/api/<int:emp_id>/', views.employee_detail_api),
]
