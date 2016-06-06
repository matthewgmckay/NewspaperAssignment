from django.db import models
from django.utils import timezone

class EventsTable(models.Model):
    ArticleOptions = (
        ('NZ', 'NZ'),
        ('International', 'International'),
        ('Tech', 'Tech'),
        ('Sports', 'Sports'),
    )

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    section = models.CharField("Section", max_length=15, choices=EventsTable.ArticleOptions)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title