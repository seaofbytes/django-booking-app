from django.shortcuts import render
from news.models import Article
from search.documents import ArticleDocument


def search(request):
    articles = Article.objects.all()
    q = request.GET.get('q')

    if q:
        articles = ArticleDocument.search().query("match", title=q)
    else:
        articles = ''

    return render(request, 'search/search_elastic.html', {'articles': articles, "q": q, })
