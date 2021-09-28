from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'actionplan'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('home-about', views.HomeAboutView, name='home-about'),
    path('home-contact-us', views.HomeContactView, name='home-contact-us'),
    path('register/', views.MentorRegisterView, name='mentor-register'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('signup/', views.TeamRegisterView, name='team-register'),
    path('login/', views.LoginView, name='team-login'),
    path('logout/', views.LogoutView, name='logout'),
    path('success/', views.SuccessView, name='success'),
    path('team-edit/', views.TeamEditView, name='team-edit'),
    path('mentor/', views.MentorView, name='mentor-view'),
    path('incentives/', views.Incentives, name='incentives'),
    path('partners/', views.Partners, name='partners'),
    path('sectors/', views.Sectors, name='sectors'),
    path('structure/', views.Structure, name='structure'),
    path('faq/', views.FAQView, name='faq'),
]
