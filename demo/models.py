from django.db import models


class Course:
    def __init__(self, title, duration, fee, topics):
        self.title = title
        self.duration = duration
        self.fee = fee
        self.topics = topics


class Title(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100, null=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.title} - {self.author}  - {self.price}"
