from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

class contact(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    e_mail = models.EmailField(max_length = 200)
    first_name = models.CharField(max_length = 200)
    phone_number = models.IntegerField()
    contact_meassage = models.TextField()
    timestamp = models.DateField(auto_now_add = True,blank = True)

    def __str__(self) -> str:
        return str(self.first_name)
