
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Candidate,Job
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

def userdash(request):
    cand=Candidate.objects.all()
    return render(request,'job/userdash.html',{'res':cand})
def index(request):

    p = Job.objects.all()
    return render(request, 'job/index.html', {'jobs': p})

def about(request):
    return render(request,'job/about.html')
def blog(request):
    return render(request,'job/blog.html')
def contact(request):
    return render(request,'job/contact.html')

def search(request):

    title = request.GET['title']
    type = request.GET['type']
    location = request.GET['location']
    jobs=Job.objects.filter(jtitle__icontains=title,jobtype__icontains=type,jstate__icontains=location)

    return render(request,'job/result.html',{'jobs':jobs})
def login(request):
    if request.method == 'POST':
        try:
            cand_mail=request.POST['cand_mail']
            cand_password=request.POST['cand_password']

            user = Candidate.objects.filter(cand_mail=cand_mail,cand_password=cand_password)

            if (user.count()==1):

                request.session['uid']=cand_mail
                if request.POST.get("chk2"):
                    response=HttpResponse('cookie')
                    response.set_cookie('cid3', request.POST['cand_mail'])
                    response.set_cookie('cid4', request.POST['cand_password'])
                    return HttpResponseRedirect('userdash')
                return redirect('userdash')

            else:
                messages.info(request, 'invalid username or password')
                return redirect("login")

        except :
            return HttpResponse("invalid")
    else:
        return render(request,'job/adminlogin2.html')

def signup(request):
    if request.method == 'POST':
        try:
            cand_name=request.POST['cand_name']
            cand_mail=request.POST['cand_mail']
            cand_password=request.POST['cand_password']

            if Candidate.objects.filter(cand_mail=cand_mail).exists():
                messages.info(request,'you are already registered with us')
                return redirect('signup2')

            else:

                r = Candidate(cand_name=cand_name,cand_mail=cand_mail,cand_password=cand_password)
                r.save()
                print("User created")
                return redirect('login2')
        except :

            return HttpResponse("invalid")
        else:
            messages.info(request,"password doesn't match")
            return redirect('signup2')
        return redirect('/')
    else:

        return render(request,'job/adminsignup2.html')

def jobpage(request):
    if 'apply' in request.POST:
        jtitle = request.POST.get('jtitle','hello')
        jstate = request.POST.get('jstate', 'hello')
        jdistrict = request.POST.get('jdistrict', 'hello')
        jobtype = request.POST.get('jobtype', 'hello')
        jcname = request.POST.get('jcname', 'hello')
        jdesc = request.POST.get('jdesc', 'hello')


        a=Job.objects.all()


        return render(request,'job/viewjobpage.html',{'details':a})
    else:
         return HttpResponse('invalid')
