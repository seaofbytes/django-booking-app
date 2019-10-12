from django.urls import path, include

from . import views


# NEWS URLS


app_name = "news"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('<int:article_id>/', views.ArticleView.as_view(), name='article'),
    path('<int:article_id>/', views.article_view, name='article'),
    path('articles/', views.ArticlesView.as_view(), name='articles'),
    path('search/', include('haystack.urls',)),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='add_comment_to_article'),
    #path('<int:pk>/comment/', views.add_comment_to_article, name='add_comment_to_article'),
]
