from django.views.generic import TemplateView
from blog.models import Post
from products.models import Package, Product


class LandingPageView(TemplateView):
    template_name = 'landingpage/landingpageview.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['blog_posts'] = Post.objects.filter(status='published').all()[:3]
        context['products'] = Product.objects.filter(show_on_landing_page=True).filter(active=True).all()
        context['packages'] = Package.objects.filter(active=True).order_by('price').all()

        return context