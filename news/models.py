from django.db import models
from datetime import datetime
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.utils.safestring import mark_safe
from news.search import ArticleIndex


class Category(models.Model):
    category_title = models.CharField(max_length=200, blank=True, null=True, default="")

    def __str__(self):
        return self.category_title


class Article(models.Model):
    title = models.CharField('title', max_length=200, blank=True)
    slug = AutoSlugField(populate_from='title', default="",
                         always_update=True, unique=True)
    author = models.CharField('Author', max_length=200, default="", blank=True, null=True)
    description = models.CharField('description', max_length=500, blank=True)
    is_published = models.BooleanField(default=False)
    article_text = HTMLField('Article text', default="", blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    article_category = models.ForeignKey(Category, on_delete="models.CASCADE", blank=True, null=True, default="")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return self.title

    def indexing(self):
        obj = ArticleIndex(meta={'id': self.id},
                           author=self.author.username,
                           title=self.title,)
        obj.save()
        return obj.to_dict(include_meta=True)


class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete="models.CASCADE", related_name="image")
    image = models.ImageField("image")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    post = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
