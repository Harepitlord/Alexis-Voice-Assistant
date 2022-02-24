from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'visionDetection'

urlpatterns = [
    path('', TemplateView.as_view(template_name='visionDetection/homePage.html'), name='Home'),
    path('Signup', views.Signup.as_view(), name='Signup'),
    path('Login', views.Login.as_view(), name='Login'),
    path('Dashboard', views.Homepage.as_view(), name='Dashboard'),
    path('Chat', views.Chat.as_view(), name='Chat'),
    path('Capture', views.Capture.as_view(), name='Capture'),
    path('Profile',views.Profile.as_view(),name='Profile'),
    path('ChangePassword',views.ChangePassword.as_view(),name='ChangePassword'),
    path('Logout', views.Logout.as_view(), name='Logout'),
]
