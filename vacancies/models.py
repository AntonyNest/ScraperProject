from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    link = models.URLField()
    source = models.CharField(max_length=50)

    def __str__(self):
        return self.title