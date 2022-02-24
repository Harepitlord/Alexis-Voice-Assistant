import json
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View

from . import forms
from . import models
from . import voiceAssitant

backend = 'visionDetection.models.EmailBackend'


# Create your views here.

class Signup(CreateView):
    model = get_user_model()
    form_class = forms.NewUser
    template_name = 'visionDetection/regis.html'
    success_url = reverse_lazy("visionDetection:Dashboard")

    def form_valid(self, form):
        form.save(commit=True)
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data.get('password'))
        print(user)
        login(request=self.request, user=user)
        return redirect(to=self.success_url)


class Login(LoginView):
    template_name = 'visionDetection/login.html'


class Homepage(LoginRequiredMixin, View):
    login_url = reverse_lazy('visionDetection:Login')

    def get(self, request):
        return render(request=request, template_name='visionDetection/mainPage.html')


class Chat(LoginRequiredMixin, View):
    JSONPath = 'E:\\LabWork\\SEM-V\\Alexis-Voice-Assistant\\Alexis\\visionDetection\\static\\json'

    def get(self, request):
        with open(f'{self.JSONPath}\\{request.user.name}.json', 'w') as JSONData:
            data = [[f'Hi {request.user.name},How can I help you?', 0], ]
            json.dump({'data': data}, JSONData)
        return render(request=request, template_name='visionDetection/chatPage.html', context={'data': data})

    def post(self, request):
        with open(f'{self.JSONPath}\\{request.user.name}.json', 'r') as JSONData:
            prev_data = json.load(JSONData)
        new_data = prev_data['data']
        res = request.POST.get('msg', None)
        new_data.append([res, 1])
        if res is not None:
            resp = voiceAssitant.server_respond(res)
            if resp is None:
                resp = ["Check your question"]

            for r in resp:
                new_data.append([r, 0])

            with open(f'{self.JSONPath}\\{request.user.name}.json', 'w') as JSONData:
                json.dump({'data': new_data}, JSONData)
        return render(request=request, template_name='visionDetection/chatPage.html', context={'data': new_data})


class Capture(LoginRequiredMixin, View):
    def get(self, request):
        return render(request=request, template_name='')


class Profile(SuccessMessageMixin, UpdateView):
    model = 'visionDetection.User'
    form_class = forms.UserUpdateForm
    success_message = 'User data Updated'
    success_url = reverse_lazy('visionDetection:Profile')


class Logout(LogoutView):
    next_page = reverse_lazy('visionDetection:Home')


class ChangePassword(PasswordChangeView):
    template_name = 'visionDetection/regis.html'
    success_url = reverse_lazy('visionDetection:Dashboard')


class Login_old(View):
    def get(self, request):
        return render(request=request, template_name='visionDetection/login.html')

    def post(self, request):
        username = request.POST['uname']
        password = request.POST['password']
        if username is not None or password is not None:
            user = models.authenticate(email=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect(to=reverse('visionDetection:Dashboard'))
            else:
                ctx = {'error': 'Username or Password is incorrect', 'uname': username}
        else:
            ctx = {'error': 'Enter Username and Password'}
        return render(request=request, template_name='visionDetection/login.html', context=ctx)


class Signup_old(View):
    def get(self, request):
        form = forms.NewUser()
        ctx = {'form': form}
        return render(request=request, template_name='visionDetection/regis.html', context=ctx)

    def post(self, request):
        form = forms.NewUser(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request=request, template_name='visionDetection/regis.html', context=ctx)
        else:
            user = form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data.get('password'))

            if user is not None:
                login(request=request, user=user)
                print(reverse('visionDetection:Dashboard'))
            return redirect(to=reverse("visionDetection:Dashboard"))


class Profile_old(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.UserUpdateForm(request.user)
        return render(request=request, template_name='visionDetection/Profile.html', context={'form': form})

    def post(self, request):
        form = forms.UserUpdateForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
