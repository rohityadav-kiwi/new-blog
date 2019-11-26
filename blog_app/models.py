""" models.py"""

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(default=0, max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    """blogpost model"""
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE,
                               null=True, default=None)
    title = models.CharField(max_length=100)
    post_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']
