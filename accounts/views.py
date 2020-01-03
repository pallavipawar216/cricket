from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from accounts.models import Accounts
from myapp.views import home
from django.core.mail import send_mail
from cricket.settings import EMAIL_HOST_USER

# Create your views here.
def login_page(request):
    if(request.method=="GET"):
        return render(request,'login.html',{})
    else:
        email_id = request.POST['email_id']
        password = request.POST['password']
        a = Accounts.objects.filter(email_id = email_id, password = password)
        if bool(a):
            request.session['email_id'] = a[0].email_id
            request.session['logged_in'] = True
            messages.success(request,f"You have successfully logged in as : {email_id}")
        else:
            messages.error(request, f"Authentication Failed !")
        return redirect(home)
def sign_up(request):
    if(request.method=="GET"):
        return render(request,'signup.html',{})
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_id = request.POST['email_id']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        users = Accounts.objects.filter(email_id=email_id)
        if len(users)==0:
            a = Accounts()
            a.first_name = first_name
            a.last_name = last_name
            a.email_id = email_id
            a.mobile_number = mobile_number
            a.password = password
            a.save()
        else:
            messages.warning(request, f"Email-id already registered with us")
            return redirect(home)
        messages.success(request, f"Successfully Registered as : {email_id}")
        return redirect(home)
def forget_passwd(request):
    if(request.method=="GET"):
        return render(request,'forget_passwd.html',{})
    else:
        send = request.POST['send']
        email_id = request.POST['email_id']
        password = Accounts.objects.filter(email_id=email_id)
        subject = 'Password Authentication'
        message = f'Your password is {password[0].password}. You can use the password to login into your account.\nThanks and Regards from CricTrend'
        recepient = []
        recepient.append(email_id)
        res = send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently=False)
        messages.info(request, f"Your password is successfully sent to your email-id : {email_id}")
        return redirect(home)     
def logout(request):
    try:
        del request.session['email_id']
        request.session['logged_in'] = False
        messages.success(request, f"You are logged out Successfully")
    except KeyError:
        pass
    return redirect(home)