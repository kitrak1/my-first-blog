from django.conf.urls import url
from . import views
app_name = 'new'

urlpatterns = [
    #define the url getdata that we have written inside form
    # url(r'^new/getdata/$', views.index),

    #defining the view for root URL
    url(r'^$', views.index, name='index'),
    url(r'^About/', views.aboutlist.as_view()),
    url(r'^new/about/$', views.about, name='about'),
    url(r'^new/services/$', views.services, name='services'),
    url(r'^new/faq/$', views.faq, name='faq'),
    url(r'^new/contact/$', views.contact, name='contact'),
    url(r'^new/data/$', views.data, name='data'),

]