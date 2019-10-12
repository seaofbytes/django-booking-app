import pytest
from django.urls import reverse
from model_mommy import mommy
from model_mommy.recipe import Recipe
from news.forms import CommentForm
from django.test import TestCase
from news.models import Article
from news.models import Comment


class NewsViewsTestCase(TestCase):
    fixtures = ['news_views_testdata.json']

    # INDEX

    def test_index_response_code(self):

        # Test Index Status Code
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_index_context(self):

        # Test Index Context
        response = self.client.get('')
        self.assertTrue('latest_article_list' in response.context)
        self.assertEqual([article.pk for article in response.context['latest_article_list']], [10, 9, 8, 7, 6, 5, ])

    def test_index_template(self):

        # Test Index Template
        response = self.client.get('')
        self.assertTemplateUsed(response, 'news/index.html')

    # ARTICLES

    def test_articles_response_code(self):

        # Test Articles Status Code
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_articles_context(self):

        # Test Article Context
        response = self.client.get('/articles/')
        self.assertTrue('latest_article_list' in response.context)
        self.assertEqual([article.pk for article in response.context['latest_article_list']], [10, 9, 8, 7, 6, ])

    def test_articles_title(self):

        # Test Articles Title
        response = self.client.get('/articles/')
        article_1 = response.context['latest_article_list'][0]
        self.assertEqual(article_1.title, "Batman shooting victim's family 'horrified' by Joker film's violence")

    def test_article_is_published(self):

        # Test if article is published
        response = self.client.get('/articles/')
        article_1 = response.context['latest_article_list'][0]
        self.assertEqual(article_1.is_published, True)

    def test_articles_template(self):

        # Test Articles Template
        response = self.client.get('/articles/')
        self.assertTemplateUsed(response, 'news/articles.html')

    # CATEGORIES

    def test_categories(self):

        # Test Categories
        response = self.client.get('/articles/')
        category_1 = response.context['categories' in response.context]
        self.assertTrue('categories' in response.context)
        self.assertEqual([categories.pk for categories in response.context['categories']], [2, 3, 4, 5, 6, 7, ])

    # COMMENT FORM

    def test_valid_form(self):

        # Test Comment Form
        w = Comment.objects.create(author='Foo', text='Bar')
        data = {'author': w.author, 'text': w.text, }
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    # def test_article(self):
    #     response = self.client.get('/1/')
    #     self.assertEqual(response.self, 200)

    # def test_search(self):
    #     response = self.client.get('/search/')
    #     self.assertEqual(response.self, 200)


# def test_api_create_comment(db, admin_client):
#     article = mommy.make_recipe("news.article")
#     comment = mommy.make_recipe("news.comment")

#     assert response.status_code == 200

#     comments = Comment.objects.all()
#     assert comments.count() == 1
#     comment = comments.last()
#     assert comment.text == "This is the article text."


# class CreateCommentViewTestCase(TestCase):

#     # def setUp(self):
#     #     # maybe look into factory boy if you haven't already
#     #     article = mommy.make_recipe("news.article")

#     # def test_get(self):
#     #     article = mommy.make_recipe("news.article")
#     #     response = self.client.get(reverse('news:add_comment_to_article', kwargs={'article_id': article.pk}))
#     #     self.assertEqual(response.status_code, 200)

#     def test_post(self):
#         # populate with form data

#         article = mommy.make_recipe("news.comment")
#         original_comment_count = article.comment_set.all().count()
#         post_data = {'author': 'value'}

#         new_comment_count = article.article_set.all().count()
#         self.assertNotEqual(original_comment_count, new_comment_count)
