from django.db import models

class Submission():
    text = models.TextField(max_length=5000, blank=True)
