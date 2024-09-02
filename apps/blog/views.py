from django.shortcuts import render
from .models import Post, Tag
from django.views import generic
from products.models import Package, Product

class BlogMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = self.get_latest_post()

        tag = self.kwargs.get('tag')
        most_popular_posts = self.get_most_popular_posts(tag)

        context.update({
            'products': self.get_products(),
            'latest_post': latest_post,
            'the_most_popular_posts': most_popular_posts,
            'tags': Tag.objects.all(),
            'current_tag': Tag.objects.get(name=tag) if tag else None,
        })


        return context

    def get_queryset(self):
        queryset = Post.objects.filter(status='published').order_by('-created')

        tag = self.kwargs.get('tag')
        if tag:
            queryset = queryset.filter(tag_posts__tag__name=tag)

        return queryset

    def get_latest_post(self):
        return Post.objects.filter(status='published').order_by('-created').first()

    def get_most_popular_posts(self, tag=None):
        if tag:
            return Post.objects.filter(status='published').filter(tag_posts__tag__name=tag).order_by('-view_count')[:3]

        return Post.objects.filter(status='published').order_by('-view_count')[:3]

    def get_products(self):
        return Product.objects.filter(show_on_landing_page=True, active=True)


# Create your views here.
class PostDetail(BlogMixin, generic.DetailView):
    model = Post
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        post = self.get_object()

        post.view_count += 1
        post.save()

        return super().get(request, *args, **kwargs)

    def get_most_popular_posts(self, tag=None):
        if self.get_object().tag_posts.exists():
            post = self.get_object()
            tags = post.tag_posts.all().values_list('tag', flat=True).distinct()
            posts_with_same_tags = Post.objects.filter(status='published').exclude(id=post.id).filter(tag_posts__tag__in=tags).distinct().order_by('-view_count')[:3]

            if posts_with_same_tags.count() > 0:
                return posts_with_same_tags


        return Post.objects.filter(status='published').order_by('-view_count')[:3]


class PostList(BlogMixin, generic.ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created']
    paginate_by = 5

