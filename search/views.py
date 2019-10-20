from django.shortcuts import render
from booking.models import Apartment
from search.documents import ApartmentDocument


# def search(request):
#     articles = Article.objects.all()
#     q = request.GET.get('q')

#     if q:
#         articles = ArticleDocument.search().query("match", title=q)
#     else:
#         articles = ''

#     return render(request, 'search/search_elastic.html', {'articles': articles, "q": q, })


def search(request):
    apartments = Apartment.objects.all()
    q = request.GET.get('q')

    if q:
        apartments = ApartmentDocument.search().query("match", title=q)
    else:
        apartments = ''

    return render(request, 'search/search_elastic.html', {'apartments': apartments, "q": q, })
