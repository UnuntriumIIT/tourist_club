from django.shortcuts import render
from django.utils import timezone

from tourist_site.models import Article


def main_page(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, './tourist/main_page.html', {'articles': articles})


def login(request):
    return render(request, './tourist/../templates/registration/login.html')
