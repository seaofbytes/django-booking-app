
from . import models
from django.contrib import admin
from .models import Article, Comment, Category, ArticleImages
from news.forms import ArticleModelForm
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ArticleImages
    fields = ['image_tag']
    readonly_fields = ['image_tag']


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'category_title')


class ArticleAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = (
        'title',
        'id',
        'article_category',
        'slug',
        'author',
        'is_published',
        'pub_date',

    )

    inlines = (ImagesInline,)
    list_filter = ('is_published', 'pub_date', 'article_category')
    search_fields = ('slug',)


class ArticleImagesAdmin(admin.ModelAdmin):

    list_display = ('id', 'article', 'image', )
    list_filter = ('article',)


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'post',
        'author',
        'text',
        'created_date',
        'approved_comment',
    )
    list_filter = ('post', 'created_date', 'approved_comment')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Article, ArticleAdmin)
_register(models.ArticleImages, ArticleImagesAdmin)
_register(models.Comment, CommentAdmin)
