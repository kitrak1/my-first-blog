from django.shortcuts import render
from .models import About , Services
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import AboutSerializer





class aboutlist(APIView):
    def get(self,request):
        emp1 = About.objects.all()
        serializer = AboutSerializer(emp1, many=True)
        return Response(serializer.data)


    def post(self):
        pass


def index(request):
    args = {'user': request.user}
    return render(request, 'new/index.html', args)

# def about(request):
#     args = {'user':request.user}
#     return render(request, 'new/about.html', args)

def about(request):
    about = About.objects.all()
    return render(request, 'new/about.html', {'about': about})

def services(request):
    services = Services.objects.all()
    return render(request, 'new/nxt-wine-tours.html',{'services' : services})

def faq(request):
    args = {'user':request.user}
    return render(request, 'new/faq.html', args)

def contact(request):
    args = {'user':request.user}
    return render(request, 'new/contact.html', args)

def data(request):
    args = {'user':request.user}
    return render(request, 'new/tours.html', args)
