from model_mommy.recipe import Recipe
from news.models import Article, Comment

article = Recipe(
    Article,
    title='Test Title',
    author='joe jones',
    description='This is the article description.',
    is_published=True,
    article_text="This is the article text."
)

comment = Recipe(
    Comment,
    author="Author Test",
    text="Comment Test Text",
    approved_comment=True,
)
