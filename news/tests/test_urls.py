from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import article_view, IndexView, ArticlesView


class TestUrls():

    # Test Articles Url's
    def test_articles_url(self):
        path = reverse('news:articles')
        assert resolve(path).view_name == 'news:articles'

    # Test Index Url's

    def test_index_url(self):
        path = reverse('news:index')
        assert resolve(path).view_name == 'news:index'

    # Test Article Url's

    def test_article_url(self):
        path = reverse('news:article', kwargs={"article_id": 8})
        assert resolve(path).view_name == 'news:article'

    # Test Add Comment Url's

    def test_add_comment_to_article_url(self):
        path = reverse('news:add_comment_to_article', kwargs={"pk": 1})
        assert resolve(path).view_name == 'news:add_comment_to_article'
