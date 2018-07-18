from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.

class USER(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


def create_pofile(sender, **kwargs):
    if kwargs['created']:
        user_profile = USER.objects.create(user=kwargs['instance'])

post_save.connect(create_pofile, sender= User)

class addemployee(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dob = models.IntegerField(default=50)

    # on submit click on the product entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('account:employeelist')





