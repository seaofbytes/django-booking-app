from django.urls import path, include
from . import views


# BOOKING APP URLS


app_name = "booking"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:apartment_id>/', views.apartment_view, name='apartment'),
    path('apartments/', views.ApartmentsView.as_view(), name='apartments'),
    #path('ajax_requests/', views.ajaxrequests_view, name='ajax_requests'),
    # path('reservation/', views.CreateReservationView.as_view(), name='reservation'),
    path('search/', include('haystack.urls',)),

]
