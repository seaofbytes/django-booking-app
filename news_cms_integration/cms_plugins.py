from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from news_cms_integration.models import ArticlePluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class ArticlePluginPublisher(CMSPluginBase):
    model = ArticlePluginModel  # model where plugin data are saved
    module = _("Article")
    name = _("Article Plugin")  # name of the plugin in the interface
    render_template = "news_cms_integration/article_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
