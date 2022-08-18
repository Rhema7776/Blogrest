from django.db import models

CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('N', "Node")
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default=0)
    custom_id = models.IntegerField(default=0)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=0)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


