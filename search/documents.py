from django_elasticsearch_dsl import Document, Index
from booking.models import Apartment



apartments = Index('apartments')


@apartments.document
class ApartmentDocument(Document):
    class Django:
        model = Apartment

        fields = [
            'title',
            'id',
            'bedrooms',
            'list_date',
        ]
