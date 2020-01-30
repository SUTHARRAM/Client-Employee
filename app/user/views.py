from django.shortcuts import render
from .forms import *
from . import models
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import View
import qrcode

from .utils import render_to_pdf

# Create your views here.


def employee(request):
    """Employee view"""
    context={}
    if request.method == 'POST':
        employee_form = Employee(request.POST or None, request.FILES or None)
        if employee_form.is_valid():
            #employee_form.save()
            pass
        else:
            return HttpResponse(str(employee_form.errors))
    else:
        employee_form = Employee()

    context['employee_form'] = employee_form

    return render(request, 'user/employee.html', context)

def client(request):
    """Client view"""
    context={}
    if request.method == 'POST':
        client_form = Client(request.POST or None, request.FILES or None)
        if client_form.is_valid():
            #client_form.save()
            pass
        else:
            return HttpResponse(str(client_form.errors))
    else: 
        client_form = Client()
    context['client_form'] = client_form

    return render(request, 'user/client.html',context)

def client_pdf(request):
    context = {}
    if request.method == 'POST':
        client_form = Client(request.POST or None, request.FILES or None)
        if client_form.is_valid():
            cid = request.POST.get('client_id')
            client_name = request.POST.get('client_name')
            client_form.save()

            dictionary = {
                'client_name': client_name,
            }

            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )

            qr.add_data(dictionary)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(f"media/qrcode/client_{cid}.jpg")
            context['dict'] = dictionary
        else:
            return HttpResponse(str(client_form.errors))

    else:
        client_form = Client()
    context['client_form'] = client_form
    return redirect('client_pdf', cid = cid)



def employee_pdf(request):
    context = {}
    if request.method == 'POST':
        employee_form = Employee(request.POST or None, request.FILES or None)
        if employee_form.is_valid():
            eid = request.POST.get('employee_id')
            employee_name = request.POST.get('employee_name')
            employee_form.save()

            dictionary = {
                'employee_name': employee_name,
            }

            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(dictionary)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(f"media/qrcode/employee_{eid}.jpg")
            context['dict'] = dictionary

           # qr_data = employee.objects.filter(employee_id = eid)
        else:
            return HttpResponse(str(employee_form.errors))
    else:
        employee_form = Employee()
    context['employee_form'] = employee_form

    return redirect('generate_pdf', eid = eid)

class GeneratePdf(View):
    def get(self, request, eid, *args, **kwargs):
        #qr_data = employee.objects.filter(employee_id = 111)
        qr_data = models.employee.objects.filter(employee_id = eid)

        data = {
            'employee_name':qr_data[0].employee_name,
            'employee_id':qr_data[0].employee_id,
        }

        pdf = render_to_pdf('user/generate_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ClientPdf(View):
    def get(self, request, cid, *args, **kwargs):

        qr_data = models.client.objects.filter(client_id = cid)

        data = {
            'client_name': qr_data[0].client_name,
            'client_id': qr_data[0].client_id,
        }

        pdf = render_to_pdf('user/client_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')