from django.shortcuts import render

from tourist_site.models import Article


def main_page(request):
    articles_mini = Article.objects.filter(is_main=False)
    main_article = Article.objects.filter(is_main=True)
    return render(request, './tourist/main_page.html', {'articles_mini': articles_mini, 'article_big': main_article})
