from elasticsearch_dsl.connections import create_connection
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date

create_connection()


class ArticleIndex(DocType):
    title = Text()
    pub_date = Date()
    description = Text()
    article_text = Text()

    class Meta:
        index = 'article-index'


def bulk_indexing():

    ArticleIndex.init()
    es = Elasticsearch()
    bulk(client=es,
         actions=(b.indexing() for b in models.Article.objects.all().iterator()))
