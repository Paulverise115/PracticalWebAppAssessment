import datetime
from django.db import models
from django.utils import timezone

class Story(models.Model):
    story_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    story_body_text = models.CharField(max_length=200)

    def __str__(self):
        return self.story_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

