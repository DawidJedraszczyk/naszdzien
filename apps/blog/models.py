from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from unidecode import unidecode


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    slug = models.SlugField(allow_unicode=True, max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class PostTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tag_posts')

    def __str__(self):
        return f'{self.tag} - {self.post}'


