from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import CreateView, DetailView, ListView
from news.models import Article, Category, Comment

from django.http import HttpResponseRedirect

# HOME PAGE VIEW


class IndexView(generic.ListView):

    template_name = 'news/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        return Article.objects.all().order_by("-pub_date")[:6]


# SINGLE ARTICLE VIEW


def article_view(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article,
               'article_category': article.article_category.category_title}

    return render(request, 'news/article.html', context)


# ALL ARTICLES PAGE VIEW


class ArticlesView(generic.ListView):
    context_object_name = 'latest_article_list'
    template_name = 'news/articles.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ArticlesView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        category_pk = self.request.GET.get('pk', None)
        if category_pk:
            return Article.objects.filter(article_category__pk=category_pk).order_by("-pub_date")
        return Article.objects.order_by("-pub_date")


# ADD COMMENT VIEW


class CommentCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        context = {'form': CommentForm()}
        return render(request, 'news/add_comment_to_article.html', context)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            article = get_object_or_404(Article, pk=kwargs.get('pk'))

            comment = form.save(commit=False)
            comment.post = article
            comment.save()
            return HttpResponseRedirect(reverse('news:article', kwargs={'article_id': article.pk}))
        else:
            form = CommentForm()
            return render(request, 'news/add_comment_to_article.html', {'form': form})


# CATEGORY VIEW


class CategoryView(generic.ListView):

    template_name = 'news/categories.html'
    context_object_name = 'category'

    def get_queryset(self):
        return Article.objects.filter(article_category__category_title="Politics")
