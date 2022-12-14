from django.db import models
from django.utils import timezone
from django.conf import settings


class Article(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image_src = models.FileField(upload_to='article', null=True, blank=True, verbose_name='image')
    text = models.TextField()
    is_main = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
