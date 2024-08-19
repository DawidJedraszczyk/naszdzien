from django.views.generic import TemplateView
from blog.models import Post

class LandingPageView(TemplateView):
    template_name = 'landingpageview.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['blog_posts'] = Post.objects.filter(status='published').all()

        return context