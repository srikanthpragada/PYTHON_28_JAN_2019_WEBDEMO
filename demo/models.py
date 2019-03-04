from django.db import models

# Create your models here.

class Course:
    def __init__(self, title, duration, fee, topics):
        self.title = title
        self.duration = duration
        self.fee = fee
        self.topics = topics

