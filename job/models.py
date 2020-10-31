from django.db import models
from phone_field import PhoneField


class Candidate(models.Model):
    cand_name = models.CharField(max_length=50)
    cand_mail = models.EmailField(max_length=254)
    cand_password = models.CharField(max_length=50)

class Cand_details(models.Model):
    userid= models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    contact = PhoneField(blank=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    state = models.CharField(max_length=60)
    district = models.CharField(max_length=60)
    skills = models.CharField(max_length=500)
    experience = models.IntegerField()
    profile_heading = models.CharField(max_length=60)
    qualification = models.CharField(max_length=60)
    image = models.ImageField()
    pincode = models.IntegerField()
    passyear = models.IntegerField()
    cgpa = models.IntegerField()
    extraskills = models.CharField(max_length=500)
    collegename = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)

class Company(models.Model):
    cname = models.CharField(max_length=100)
    cmail = models.EmailField(max_length=250)
    cpassword = models.CharField(max_length=50)
    cregdate = models.DateTimeField(auto_now=True)
    cwebsite = models.URLField(max_length=200)

class Job(models.Model):

    jtitle = models.CharField(max_length=100)
    jskills = models.CharField(max_length=500)
    jdesc = models.CharField(max_length=1000)
    jdate = models.DateTimeField(null=True,auto_now=True)
    jstate = models.CharField(max_length=40)
    jdistrict = models.CharField(max_length=60)
    jcname = models.CharField(max_length=100,default="")
    jobtype = models.CharField(max_length=30)
    min_quali = models.CharField(max_length=30)
    lastapply = models.DateTimeField(null=True)
    maxage = models.IntegerField(default=40)
    no_of_openings = models.IntegerField(default=1)



class ApplyJob(models.Model):
    jobs = models.ForeignKey(Job,on_delete=models.CASCADE,null=True)
    userid= models.ForeignKey(Candidate,on_delete=models.CASCADE,null=True)
