import datetime
import json
from datetime import date, timedelta
from booking.models import Apartment, Reservation, ApartmentPrices
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.views.generic import  TemplateView
from django.http import HttpResponseRedirect
from booking.forms import ReservationForm



# 1. uzeti start i end iz forme
# 2. uzeti sve start i end iz cijena
# 3. usporediti start end forme sa start end cijenama
# 4. vratiti samo matcheve sa cijenama
#
#
#
#
#
#
#
#

def apartment_view(request, apartment_id):

    reservation = Reservation.objects.filter(apartment__pk=apartment_id)
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    context = {}
    context['apartment'] = apartment

    unavailable = []
    for start, end in apartment.reservations.values_list('start_date', 'end_date'):
        while start <= end:
            unavailable.append(start.strftime('%-d-%m-%Y'))
            start += datetime.timedelta(days=1)
    form = ReservationForm()
    context['unavailable_dates'] = json.dumps(unavailable)
    context['form'] = form

    if request.method == 'GET':
        form = ReservationForm()
        
    elif request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            context = {}
            reservation = form.save(commit=False)
            reservation.apartment = apartment
            reservation.save()        
            start_date = request.POST.get('start_date', None)
            end_date = request.POST.get('end_date', None)
            sdate = datetime.datetime.strptime(start_date, '%Y-%m-%d') #start
            edate = datetime.datetime.strptime(end_date ,'%Y-%m-%d') #end
            prices_by_date = apartment.price_by_date(sdate, edate)

            user_dates = [sdate + datetime.timedelta(days=x) for x in range((edate-sdate).days + 1)]
            user_date_list = []
            for day in user_dates:
                user_date_list.append(day.strftime('%d,%m,%Y'))
          
            context['price_per_day'] = prices_by_date.price
            context['total_price'] =  len(user_date_list) * prices_by_date.price    
            context['unavailable_dates'] = json.dumps(unavailable)
            context['form'] = form
            context['apartment'] = apartment           
            context['date_start'] = start_date
            context['date_end'] = end_date 
            form.save()
            return render(request, "booking/apartment.html", context)
            
    return render(request, 'booking/apartment.html', context)


class ApartmentsView(generic.ListView):
    context_object_name = 'apartment_list'
    template_name = 'booking/apartments.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ApartmentsView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        category_pk = self.request.GET.get('pk', None)
        if category_pk:
            return Apartment.objects.order_by("-list_date")
        return Apartment.objects.order_by("-list_date")


class IndexView(generic.ListView):

    template_name = 'booking/index.html'
    context_object_name = 'latest_apartment_list'

    def get_queryset(self):
        return Apartment.objects.all().order_by("-list_date")[:6]


class ContactView(TemplateView):
    template_name = "booking/contact.html"
