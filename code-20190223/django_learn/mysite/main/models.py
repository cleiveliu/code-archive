from django.db import models

# Create your models here.


class Tutorial(models.Model):
    tutorial = "tem"
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(
        'date published', defualt=datetime.now())

    def __str__(self):
        return self.tutorial_title


class Person(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.name
