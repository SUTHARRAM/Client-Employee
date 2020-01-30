from django.contrib import admin
from django.urls import path
from . import  views


urlpatterns = [
    
    path('employee/', views.employee, name="employee"),
    path('client/', views.client, name="client"),
    path('employee/employee_pdf/',views.employee_pdf, name="employee_pdf"),
    path('client/client_pdf/',views.client_pdf, name="client_pdf"),
    path('generate_pdf/<eid>/',views.GeneratePdf.as_view(), name="generate_pdf"),
    path('client_pdf/<cid>/',views.ClientPdf.as_view(), name="client_pdf"),
]