
from django.shortcuts import render,redirect

from job.models import Candidate,Job,Cand_details,ApplyJob

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages



def index(request):
    pe = Job.objects.all()
    q = Job.objects.all().count()
    q = str(q)
    if request.session.has_key('uid'):
        s = Candidate.objects.all()
        return render(request, 'loggedin/index.html', {'res': s, 'udata': request.session['uid'], 'jobs': pe, 'jobsc': q})
    else:
        return redirect('login')



def search(request):

    title = request.GET['title']
    type = request.GET['type']
    location = request.GET['location']
    jobs=Job.objects.filter(jtitle__icontains=title,jobtype__icontains=type,jstate__icontains=location)
    return render(request, 'loggedin/result.html', {'jobs': jobs})

def jobpage(request):
    if request.session.has_key('uid'):
        if request.method =='POST':
            return render(request,'loggedin/jobapply.html',{'udata': request.session['uid']})
        else:
            s = Job.objects.get(pk=request.GET['z'])
            return render(request,'loggedin/viewjobpage.html',{'details':s,'udata': request.session['uid']})

    else:
        return HttpResponse("login to continue")

def userdash(request):

    '''if request.session.has_key('uid'):
        a=request.session(id)
        m=Job.objects.filter(a=a)

        return render(request, 'loggedin/userdash.html', {'dashdetail': m})
    else:
        return HttpResponse("login to continue")'''
    #s = ApplyJob.objects.get(pk=request.GET['jobinfo'])
    #return render(request, 'loggedin/userdash.html', {'details': s, 'udata': request.session['uid']})
    return HttpResponse("save ho gya")

def jobapply(request):
    if request.session.has_key('uid'):
        if request.method == 'POST':
            q=Cand_details(firstname=request.POST['firstname'],lastname = request.POST['lastname'],email = request.POST['email'],contact = request.POST['contact'],gender = request.POST['gender'],age = request.POST['age'],state = request.POST['state'],district = request.POST['district'],skills = request.POST['skills'],experience = request.POST['experience'],qualification = request.POST['qualification'],pincode = request.POST['pincode'],passyear = request.POST['passyear'],cgpa = request.POST['cgpa'],extraskills = request.POST['extraskills'],collegename = request.POST['collegename'],course = request.POST['course'],branch = request.POST['branch'])
            q.save()
    appliedjob=ApplyJob.objects.get(id=pk_apply)
            #applyjobdetail=ApplyJob.objects.get(pk=request.GET['jobinfo'],userid=request.session.get('uid'))
            #applyjobdetail.save()





        #return render(request, 'loggedin/userdash.html', {'details': s, 'udata': request.session['uid']})
        return redirect("userdash")

    else:
        return HttpResponse("invalid")


def logout(request):
    del request.session['uid']
    return redirect('/')

def contact(request):
    if request.session.has_key('uid'):
        s = Candidate.objects.all()
        return render(request, 'loggedin/contact2.html', {'res': s, 'udata': request.session['uid']})
    else:
        return render(request, 'loggedin/contact2.html')