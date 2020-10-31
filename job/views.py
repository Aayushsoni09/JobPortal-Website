
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Candidate,Job,Cand_details,ApplyJob
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages



def index(request):
    p = Job.objects.all()
    q=Job.objects.all().count()
    q=str(q)
    return render(request, 'job/index.html', {'jobs': p,'jobsc':q})

def contact(request):

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail(
            subject,message,email,['soniaayush24400@gmail.com']
        )


        return render(request, 'job/contact2.html', {'name':name})
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
            user_id=None
            user = Candidate.objects.filter(cand_mail=cand_mail,cand_password=cand_password)
            for uid in Candidate.objects.filter(cand_mail=cand_mail,cand_password=cand_password):
                user_id = uid.id
            #user_id=Candidate.objects.filter(cand_mail=cand_mail,cand_password=cand_password).values_list('id', flat=True)
            #print(user_id)
            if (user.count()==1):

                #request.session['uid']=cand_mail
                request.session['uid'] = user_id
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
