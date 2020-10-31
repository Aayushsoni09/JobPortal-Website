from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from job.models import Candidate,Job
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

def viewjob(request):
    j = Job.objects.all()
    return render(request, 'adminpanel/viewjob.html', {'jobs': j})

def postjob(request):
    if request.method=='POST':
       obj2=Job(jtitle=request.POST['jtitle'],jcname=request.POST['jcompany'],jobtype=request.POST['job-type'],jstate=request.POST['jstate'],jdistrict=request.POST['jdistrict'],jdesc=request.POST['jdesc'])
       obj2.save()
    return render(request,'adminpanel/postjob.html')

def home(request):
    if request.method == 'POST':
        obj=Candidate(ausername=request.POST['ausername'],apassword=request.POST['apassword'])
        obj.save()
        return render(request,'adminpanel/adminlogin.html',{'msg':'registration successful'})
    if request.COOKIES.get('cid'):
        return render(request, 'adminpanel/adminlogin.html',{'cookie1':request.COOKIES['cid'],'cookie2':request.COOKIES['cid2']})
    else:
        return render(request, 'adminpanel/adminlogin.html')
def signup(request):
    if request.method == 'POST':
        try:
            firstname=request.POST['afirstname']
            lastname=request.POST['alastname']
            mail=request.POST['amail']
            password1=request.POST['apassword1']
            password2=request.POST['apassword2']
            username=request.POST['ausername']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('signup')
                elif User.objects.filter(email=mail).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('signup')
                else:

                    r = User.objects.create_user(first_name=firstname,username=username,last_name=lastname,email=mail,password=password1)
                    r.save()
                    print("User created")
                    return redirect('login')
        except :

            return HttpResponse("invalid")
        else:
            messages.info(request,"password doesn't match")
            return redirect('signup')
        return redirect('/')
    else:

        return render(request,'adminpanel/adminsignup.html')

def login(request):
    if request.method == 'POST':
        try:
            ausername=request.POST['ausername']
            apassword=request.POST['apassword']

            user = auth.authenticate(username=ausername,password=apassword)
            if user is not None:
                auth.login(request, user)
                request.session['uid']=request.POST['ausername']
                if request.POST.get("chk"):
                    response=HttpResponse('cookie')
                    response.set_cookie('cid' , request.POST['ausername'])
                    response.set_cookie('cid2', request.POST['apassword'])
                    return HttpResponseRedirect('admin_index')
                return redirect('admin_index')

            else:
                messages.info(request, 'invalid username or password')
                return redirect("login")

        except :
            return HttpResponse("invalid")
    else:
        return render(request,'adminpanel/adminlogin.html')

def index(request):
    if request.session.has_key('uid'):
        s=Candidate.objects.all()

        return render(request,'adminpanel/index.html',{'res':s,'udata':request.session['uid']})
    else:
        return redirect('login')

def iconmaterial(request):
    return render(request,'adminpanel/icon-material.html')


def find(request):
    s=Candidate.objects.get(pk=request.GET['q'])
    return render(request,'adminpanel/find.html',{'r':s})
def update(request):
    s = Candidate.objects.get(pk=request.POST['nid'])
    s.cand_name=request.POST['cand_name']
    s.cand_mail=request.POST['cand_mail']
    s.cand_password=request.POST['cand_password']
    s.save()
    return redirect('admin_index')
def delete(request):
    s = Candidate.objects.get(pk=request.GET['q'])
    s.delete()
    return redirect('admin_index')
def logout(request):
    del request.session['uid']
    return redirect('login')
def deletejob(request):
    z = Job.objects.get(pk=request.GET['z'])
    z.delete()
    return redirect('viewjob')
