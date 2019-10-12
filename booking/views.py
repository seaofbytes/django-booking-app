from django.shortcuts import render
from booking.models import Apartment, Reservation
from django.shortcuts import render, reverse, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views import generic, View
from django.views.generic import CreateView, DetailView, ListView
from django.http import HttpResponseRedirect
from booking.forms import ReservationForm
import json
from django.core.serializers.json import DjangoJSONEncoder
import itertools


def apartment_view(request, apartment_id):

    reservation = Reservation.objects.filter(apartment__pk=apartment_id)
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    context = {'apartment': apartment, }
    unavailable_dates = apartment.reservations.values_list('start_date', 'end_date')

    form = ReservationForm()
    if request.method == 'GET':
        form = ReservationForm()

    elif request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.apartment = apartment
            reservation.save()
            form.save()
            return HttpResponseRedirect('/booking/')
    args = {}
    args['form'] = form
    args['apartment'] = context
    args['reservation'] = reservation
    args['unavailable_dates'] = list(itertools.chain(*unavailable_dates))
    print(unavailable_dates)
    return render(request, 'booking/apartment.html', args)


def ajaxrequests_view(request):
    item_id = request.POST.get('item_id', None)
    get_data = MyModel.objects.select_related('item_owner').filter(item_id=item_id)
    ser_data = serializers.serialize("json", get_data)

    return HttpResponse(ser_data, content_type="application/json")

# ALL APARTMENTS PAGE VIEW


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
            return Apartment.objects.order_by("-pub_date")
        return Apartment.objects.order_by("-pub_date")


class IndexView(CreateView):

    def get(self, request, *args, **kwargs):
        context = {'form': ReservationForm()}
        return render(request, 'booking/index.html', context)

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            apartment = get_object_or_404(Apartment, pk=kwargs.get('pk'))
            comment = form.save(commit=False)
            comment.post = apartment
            comment.save()
            return HttpResponseRedirect(reverse('booking:index'))
        else:
            form = ReservationForm()
            return render(request, 'booking/index.html', {'form': form})
