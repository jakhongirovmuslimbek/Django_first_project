from django.db import models

class UzbekistanNews(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class GlobalNews(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class SportNews(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()    

    def __str__(self):
        return self.title