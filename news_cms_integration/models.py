from django.db import models
from cms.models import CMSPlugin
from news.models import Article


class ArticlePluginModel(CMSPlugin):
    article = models.ForeignKey(Article, on_delete="models.CASCADE")

    def __str__(self):
        return self.article.title
