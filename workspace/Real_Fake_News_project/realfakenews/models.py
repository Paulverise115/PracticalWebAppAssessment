from django.db import models


class Story(models.Model):
    story_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    story_body_text = models.CharField(max_length=200)

