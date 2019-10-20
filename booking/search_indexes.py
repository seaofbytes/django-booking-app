import datetime
from haystack import indexes
from booking.models import Apartment

class ApartmentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,template_name='search/indexes/booking/apartment_text.txt')
    title = indexes.CharField(model_attr='title')
    
    def get_model(self):
        return Apartment
    
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(list_date__lte=datetime.datetime.now())
    