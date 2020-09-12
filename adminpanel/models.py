from django.db import models


class Admin(models.Model):
    aname = models.CharField(max_length=50)
    amail=models.EmailField(max_length=254)

    ausername=models.CharField(max_length=50)
    apassword=models.CharField(max_length=50)

