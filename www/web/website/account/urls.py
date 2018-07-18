from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$',auth_views.logout, {'template_name': 'account/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^addemployee/$', views.addemployee, name='addemployee'),
    url(r'^enquirytype/$', views.enquirytype, name='enquirytype'),
    url(r'^citymaster/$', views.citymaster, name='citymaster'),
    url(r'^department/$', views.department, name='department'),
    url(r'^productmaster/$', views.productmaster, name='productmaster'),
    url(r'^customermaster/$', views.customermaster, name='customermaster'),
    url(r'^itemmaster/$', views.itemmaster, name='itemmaster'),
    url(r'^addenquiry/$', views.addenquiry, name='addenquiry'),
    url(r'^employeelist/$', views.employeelist, name='employeelist'),
    url(r'^enquirytypelist/$', views.enquirytypelist, name='enquirytypelist'),
    url(r'^citylist/$', views.citylist, name='citylist'),
    url(r'^departmentlist/$', views.departmentlist, name='departmentlist'),
    url(r'^productlist/$', views.productlist, name='productlist'),
    url(r'^customerlist/$', views.customerlist, name='customerlist'),
    url(r'^itemlist/$', views.itemlist, name='itemlist'),
    url(r'^enquirylist/$', views.enquirylist, name='enquirylist'),
]
