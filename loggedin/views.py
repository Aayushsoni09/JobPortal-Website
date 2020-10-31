from collections.abc import Iterable
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from job.models import Candidate, Job, Cand_details, ApplyJob

job_id=None
user_email=None

def index(request):
    pe = Job.objects.all()
    q = Job.objects.all().count()
    q = str(q)
    if request.session.has_key('uid'):
        global user_email
        s = Candidate.objects.all()
        for userid in s:
            if userid.id==request.session['uid']:
                user_email = userid.cand_mail
        return render(request, 'loggedin/index.html', {'res': s, 'udata': user_email, 'jobs': pe, 'jobsc': q})
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
            cand = None
            if Cand_details.objects.filter(userid_id=request.session['uid']):
                for data in Cand_details.objects.all():
                    if data.userid_id == request.session['uid']:
                        cand = data
                        print('andarwala')
                print('baharwala')
                return render(request, 'loggedin/jobapply2.html', {'udata': user_email, 'candidate': cand})
            else:
                for data in Candidate.objects.all():
                    if data.id == request.session['uid']:
                        cand=data
                        print('elseandarwala',cand)
                print('elsebaharwala',cand)
                return render(request,'loggedin/jobapply.html',{'udata': user_email,'candidate': cand})
        else:
            s = Job.objects.get(pk=request.GET['z'])
            global job_id
            job_id=s.id

            return render(request,'loggedin/viewjobpage.html',{'details':s,'udata': user_email})

    else:
        return HttpResponse("login to continue")

def userdash(request):

    if request.session.has_key('uid'):
        m=[]
        jobs=[]

        for userdata in ApplyJob.objects.all():
            if userdata.userid_id == request.session['uid']:
                jobs.append(userdata.jobs_id)

        for job in Job.objects.all():
            if job.id in jobs:
                m.append(job)

        udetail=Candidate.objects.filter(id=request.session['uid'])

        return render(request, 'loggedin/userdash.html', {'dashdetail': m,'udetail':udetail})
    else:
        return HttpResponse("login to continue")

def jobapply(request):
    if request.session.has_key('uid'):

        if request.method == 'POST':
            global job_id
            if Cand_details.objects.filter(userid_id=request.session['uid']):
                appliedjob = ApplyJob(jobs_id=job_id, userid_id=request.session['uid'])
                appliedjob.save()
                return redirect('userdash')

            else:
                q = Cand_details(fullname=request.POST['fullname'], email=request.POST['email'],
                                 contact=request.POST['contact'], gender=request.POST['gender'],
                                 age=request.POST['age'], state=request.POST['state'],
                                 district=request.POST['district'], skills=request.POST['skills'],
                                 experience=request.POST['experience'], qualification=request.POST['qualification'],
                                 pincode=request.POST['pincode'], passyear=request.POST['passyear'],
                                 cgpa=request.POST['cgpa'], extraskills=request.POST['extraskills'],
                                 collegename=request.POST['collegename'], course=request.POST['course'],
                                 branch=request.POST['branch'], userid_id=request.session['uid'])
                q.save()
                appliedjob = ApplyJob(jobs_id=job_id, userid_id=request.session['uid'])
                appliedjob.save()
                return redirect('userdash')
            return redirect('userdash')
        else: pass


    else:
        return HttpResponse("invalid")


def logout(request):
    del request.session['uid']
    return redirect('/')

def contact(request):
    if request.session.has_key('uid'):
        s = Candidate.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            send_mail(
                subject, message, email, ['soniaayush24400@gmail.com']
            )

            return render(request, 'loggedin/contact2.html', {'res': s, 'udata': request.session['uid'],'name':name})
        else:
            return render(request, 'loggedin/contact2.html')

    else:
        return render(request, 'loggedin/contact2.html')

def deletejob2(request):
    z = ApplyJob.objects.get(jobs_id=request.GET['q'])
    z.delete()
    return redirect('userdash')