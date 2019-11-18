from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(default=0, max_length=15)
    email = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.user


"""
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
"""


class BlogPost(models.Model):
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True, default=None)

    title = models.CharField(max_length=100)
    post_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def save(self):
        if self.is_published and not self.published_date:
            self.published_date = datetime.now()
        super(BlogPost, self).save()

    # def publish(self):
    #     self.published_date = models.DateTimeField(timezone.now)
    #     self.save()
    #     return self.published_date

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
