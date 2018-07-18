from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User



def home(request):

    numbers = [1,2,3,4,5]
    name = 'Kartik'

    args = {'myname': name, 'numbers': numbers}
    return render(request, 'account/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'account/reg_form.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'account/profile.html', args)


def dashboard(request):
    args = {'user': request.user}
    return render(request, 'account/dashboard.html', args)

def addemployee(request):
    args = {'user':request.user}
    return render(request, 'account/addemployee.html', args)

def enquirytype(request):
    args = {'user':request.user}
    return render(request, 'account/enquirytype.html', args)

def citymaster(request):
    args = {'user':request.user}
    return render(request, 'account/citymaster.html', args)

def department(request):
    args = {'user':request.user}
    return render(request, 'account/department.html', args)

def productmaster(request):
    args = {'user':request.user}
    return render(request, 'account/productmaster.html', args)

def customermaster(request):
    args = {'user':request.user}
    return render(request, 'account/customermaster.html', args)

def itemmaster(request):
    args = {'user':request.user}
    return render(request, 'account/itemmaster.html', args)

def addenquiry(request):
    args = {'user':request.user}
    return render(request, 'account/addenquiry.html', args)

def employeelist(request):
    args = {'user':request.user}
    return render(request, 'account/employeelist.html', args)

def enquirytypelist(request):
    args = {'user':request.user}
    return render(request, 'account/enquirytypelist.html', args)

def citylist(request):
    args = {'user':request.user}
    return render(request, 'account/citylist.html', args)

def departmentlist(request):
    args = {'user':request.user}
    return render(request, 'account/departmentlist.html', args)

def productlist(request):
    args = {'user':request.user}
    return render(request, 'account/productlist.html', args)

def customerlist(request):
    args = {'user':request.user}
    return render(request, 'account/customerlist.html', args)

def itemlist(request):
    args = {'user':request.user}
    return render(request, 'account/itemlist.html', args)

def enquirylist(request):
    args = {'user':request.user}
    return render(request, 'account/enquirylist.html', args)

