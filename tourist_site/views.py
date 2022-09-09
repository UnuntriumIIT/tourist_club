from django.shortcuts import render
from django.utils import timezone

from tourist_site.models import Article


def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, './tourist/article_list.html', {'articles': articles})
