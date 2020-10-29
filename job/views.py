
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Candidate,Job,Cand_details,ApplyJob
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages



def index(request):
    p = Job.objects.all()
    q=Job.objects.all().count()
    q=str(q)
    return render(request, 'job/index.html', {'jobs': p,'jobsc':q})

def about(request):
    if request.session.has_key('uid'):
        s = Candidate.objects.all()
        return render(request, 'job/about2.html', {'res': s, 'udata': request.session['uid']})
    else:
        return render(request,'job/about.html')
def blog(request):
    if request.session.has_key('uid'):
        s = Candidate.objects.all()
        return render(request, 'job/blog2.html', {'res': s, 'udata': request.session['uid']})
    else:
        return render(request, 'job/blog.html')
def contact(request):
    if request.session.has_key('uid'):
        s = Candidate.objects.all()
        return render(request, 'job/contact2.html', {'res': s, 'udata': request.session['uid']})
    else:
        return render(request,'job/contact2.html')

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
                    return HttpResponseRedirect('loggedin/')
                return redirect('loggedin/')

            else:
                messages.info(request, 'invalid username or password')
                return redirect("login2")

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

        return render(request,'job/adminsignup2.html')
'''def jobpage(request):
    if request.session.has_key('uid'):
        if request.method == 'POST':
            ApplyJob.objects.get(pk=request.get['l'])
            return render(request, 'loggedin/jobapply.html')
        else:
            s = Job.objects.get(pk=request.GET['z'])
            return render(request, 'loggedin/viewjobpage.html', {'details': s})
    else:
        return HttpResponse("login krle")
def jobapply(request):
    if request.method == 'POST':
        q=Cand_details(firstname=request.POST['firstname'],lastname = request.POST['lastname'],email = request.POST['email'],contact = request.POST['contact'],gender = request.POST['gender'],age = request.POST['age'],state = request.POST['state'],district = request.POST['district'],skills = request.POST['skills'],experience = request.POST['experience'],qualification = request.POST['qualification'],pincode = request.POST['pincode'],passyear = request.POST['passyear'],cgpa = request.POST['cgpa'],extraskills = request.POST['extraskills'],collegename = request.POST['collegename'],course = request.POST['course'],branch = request.POST['branch'])
        q.save()
        return redirect("userdash")
    else:
        return HttpResponse("invalid")'''