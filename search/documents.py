from django_elasticsearch_dsl import Document, Index
from news.models import Article

articles = Index('articles')


@articles.document
class ArticleDocument(Document):
    class Django:
        model = Article

        fields = [
            'title',
            'description',
        ]
