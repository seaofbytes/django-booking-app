from django import template
from news.models import Article

register = template.Library()


@register.inclusion_tag("news/categories.html")
def show_results(category=None):
    article = Article.objects.all()
    if category:
        article = article.filter(article_category__category_title=category)
    return {'article': article[:3]}


@register.inclusion_tag("news/sport_tag.html")
def tech(category=None):
    article = Article.objects.all().filter(article_category=5)
    return {'article': article[:3]}


@register.inclusion_tag("news/sport_tag.html")
def sports(category=None):
    article = Article.objects.all().filter(article_category=3)
    return {'article': article[:3]}


@register.inclusion_tag("news/sport_tag.html")
def politics(category=None):
    article = Article.objects.all().filter(article_category=2)
    return {'article': article[:3]}
