from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('',  views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/',  views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/',  views.vote, name='vote')
]
