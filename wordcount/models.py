from django.db import models

class DataStore(models.Model):
    url = models.URLField()
    word_count = models.IntegerField(blank=True, null=True)
    favourite = models.BooleanField(default=False)
    web_links = models.TextField(blank=True, null=True)
    media_links = models.TextField(blank=True, null=True)
