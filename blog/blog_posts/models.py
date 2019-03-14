from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 30) #title of Article
    author_name = models.CharField(max_length = 30) #author of Article
    text = models.TextField() #actual article
    date_of_submission = models.DateField(default = datetime.date.today) #date of submission

    def __str__(self):
        return ('{title} by {author}'.format(title = self.title, author = self.author_name))
