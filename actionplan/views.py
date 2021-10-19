from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import MentorRegistrationForm, TeamSignUpForm, TeamEditForm, Stage1SubmissionForm
from django.contrib.auth import  logout, login
from email.message import EmailMessage
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
import string
import random
import smtplib
from .credentials import EMAIL_ADDRESS, EMAIL_PASSWORD
from .models import Team

# Create your views here.

def MentorRegisterView(request):
    if request.method == 'POST':
        form = MentorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actionplan:home')
    else:
        form = MentorRegistrationForm()
    return render(request, 'access/mentor_register.html', {'form':form})


def TeamRegisterView(request):
    if request.method == 'POST':
        form = TeamSignUpForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            #create login credentials for team
            username = 'AP' + ''.join(random.choices(string.digits, k = 4))
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))
            email = form.cleaned_data['team_leader_emailID']
            name = form.cleaned_data['team_leader_name']
            #save user to database
            instance.username = username
            instance.password = make_password(password)
            instance.email = email
            instance.save()

            #send login credentials to email
            msg = EmailMessage()
            msg['Subject'] = "Registration Successful"
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = email
            msg.set_content('Hello {}, \nGreetings from Abhyuday, IIT Bombay!\nCongratulations on registering to Action plan competition 2021-22 \n\nACTION PLAN ID: {} \nPASSWORD: {} \n\n* To proceed further, login using your ACTION PLAN ID and Password and fill in the further details. \n* You’ll get access to a questionnaire soon regarding which you will be notified over mail. This needs to be filled compulsorily to proceed further in the competition. \n* Kindly note your ACTION PLAN ID and Password with you for future reference. \n\nAll the rules regarding registration and questionnaire are mentioned on the website. The other details of the competition will be conveyed further. \n\nThanks & Regards, \nAction plan 2021-22'.format(name, username, password))
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            return redirect('actionplan:success')
    else:
        form = TeamSignUpForm()
    return render(request, "access/signup.html", {'form': form})


def LoginView(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('actionplan:dashboard')
        form = AuthenticationForm()
    return render(request, 'access/login.html', {'form':form})


@login_required(login_url='/login/')
def DashboardView(request):
    instance = Team.objects.get(username=request.user)
    if request.POST:
        form1 = Stage1SubmissionForm(request.POST, request.FILES)
        if form1.is_valid():
            instance = form1.save(commit=False)
            instance.team = request.user
            instance.save()
            return redirect('actionplan:dashboard')
    else:
        form1 = Stage1SubmissionForm(instance=instance)
    return render(request, 'dashboard.html', {'form': form1})


@login_required(login_url='/login/')
def TeamEditView(request):
    instance = Team.objects.get(username=request.user)
    if request.method == 'POST':
        form = TeamEditForm(request.POST, instance=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('actionplan:dashboard')
    else:
        form = TeamEditForm(instance=instance)
    return render(request, "team_edit.html", {'form': form})


def LogoutView(request):
    logout(request)
    return redirect('actionplan:home')


def SuccessView(request):
    return render(request, 'success.html')

def MentorView(request):
    return render(request, 'mentorship.html')

def Incentives(request):
    return render(request, 'incentives.html')

def Partners(request):
    return render(request, 'partners.html')

def Sectors(request):
    return render(request, 'sectors.html')

def Structure(request):
    return render(request, 'structure.html')

def HomeAboutView(request):
    return redirect(reverse('actionplan:home') + '#about')

def HomeContactView(request):
    return redirect(reverse('actionplan:home') + '#contact-us')

def FAQView(request):
    return render(request, 'rulesfaq.html')

