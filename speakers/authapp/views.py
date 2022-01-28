from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

import authapp
from speakers import settings
from speakers.local_settings import EMAIL_HOST_USER
from .forms import UserRegisterForm, UserLoginForm
from .models import User
from .serializers import (
    UserProfileCreateSerializer,
    UserProfileLoginSerializer
)
from .docs import docs


class UserProfileCreationView(APIView):  # Возможно в будущем переделается на дженерик
    @swagger_auto_schema(**docs.UserProfileCreationView)
    def post(self, request):
        serializer = UserProfileCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={"user_profile": serializer.data['email'],
                  "status": "created"},
            status=201)


class UserProfileLoginView(APIView):
    @swagger_auto_schema(**docs.UserProfileLoginView)
    def post(self, request):
        serializer = UserProfileLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, new_token = serializer.login_user()

        response = Response(
            data={
                "auth_token": new_token.key,
                "status": "logged_in"
            },
            status=201
        )
        response.set_cookie('auth_token', new_token.key)

        return response


class UserProfileLogoutView(APIView):
    def post(self, request):
        user = request.user.logout()
        user.auth_token.delete()

        return Response(
            data={"status": "logged_out"},
            status=201
        )

# --------------------Временные представления для разработки-----------------------


class UserProfileDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        request.user.auth_token.delete()
        request.user.delete()

        return Response(
            data={"status": "deleted"},
            status=201
        )


# Тестовая вьюшка для проверки аутентификации-----------------------
class TestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return Response(data={"response": "success"})

# --------------------Временные представления для разработки-----------------------


def login(request):
    title = 'вход'
    login_form = UserLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        email = request.POST['email']
        password = request.POST['password']

        user = authapp.authenticate(email=email, password=password)
        if user and user.is_active:
            authapp.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('login'))

    content = {
        'title': title,
        'login_form': login_form,
        'next': next
    }
    return render(request, 'authapp/login.html', content)


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            # register_form.save()
            user = register_form.save()
            if send_verify_email(user):
                print('success')
            else:
                print('failed')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()

    content = {
        'title': title,
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', content)

def send_verify_email(user):
    verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
    subject = f'Подтверждение учетной записи {user.activation_key}'
    message = f'Ссылка для активации: {settings.BASE_URL}{verify_link}'

    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=True)


def veryfy(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = ''
            user.save()
            authapp.login(request, backend=user)
        return render(request, 'authapp/verification.html')

    except Exception as err:
        print(f'error activation user: {err.args}')

    return HttpResponseRedirect(reverse('main'))

def test(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                      EMAIL_HOST_USER, [User.email], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('register')
            else:
                messages.error(request, 'Ошибка отправки.')
        else:
            messages.error(request, 'Ошибка регистрации.')
    else:
        form = UserRegisterForm()
    return render(request, 'authapp/test.html', {"form": form})
