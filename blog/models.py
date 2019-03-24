from django.db import models

from django.utils import timezone



class Post(models.Model):
    AUTHOR = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    TITLE = models.CharField(max_length=200)
    TEXT = models.TextField()
    CREATED_DATE = models.DateTimeField(
            default=timezone.now)
    PUBLISHED_DATE = models.DateTimeField(
            blank=True, null=True)
    
    
    def publish(self):
        self.PUBLISHED_DATE = timezone.now()
        self.save()
        
    def __str__(self):
        return self.TITLE
    