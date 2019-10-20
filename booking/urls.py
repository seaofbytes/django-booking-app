from django.urls import path, include
from . import views


# BOOKING APP URLS


app_name = "booking"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:apartment_id>/', views.apartment_view, name='apartment'),
    path('apartments/', views.ApartmentsView.as_view(), name='apartments'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('search/', include('haystack.urls',)),

]
