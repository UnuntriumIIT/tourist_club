import django.contrib.auth as auth
import django.http as http
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from tourist_site.models import Article


def main_page(request):
    articles_mini = Article.objects.filter(is_main=False)
    main_article = Article.objects.filter(is_main=True)
    return render(request, './tourist/main_page.html', {'articles_mini': articles_mini, 'article_big': main_article})


def login_view(request):
    if not request.user.is_authenticated:
        if request.POST:
            username = request.POST.get('loginUsername', '')
            password = request.POST.get('inputPassword', '')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(profile_view)
            else:
                return http.HttpResponseBadRequest('Неправильный логин или пароль')
        else:
            return render(request, './accounts/login.html')
    else:
        return redirect(main_page)


def logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return render(request, './accounts/logout.html')
    else:
        return redirect(login_view)


def profile_view(request):
    if request.user.is_authenticated:
        return render(request, './accounts/profile.html')
    else:
        return http.HttpResponseForbidden('Доступ запрещен.')


def register_view(request):
    if request.POST:
        username = request.POST.get('userName', '')
        password = request.POST.get('inputPassword', '')
        first_name = request.POST.get('firstName', '')
        email = request.POST.get('email', '')
        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email)
            user.is_active = False
            user.save()
        except Exception:
            return http.HttpResponseServerError('Ошибка при создании пользователя')
        return redirect(login_view)
    return render(request, './accounts/registration.html')
