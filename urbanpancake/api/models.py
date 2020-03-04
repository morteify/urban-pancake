from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        ordering = ['first_name']


class Picture(models.Model):
    description = models.TextField()
    publish_date = models.DateTimeField()
    author = models.ForeignKey(
        'User', related_name='pictures', on_delete=models.CASCADE)

    class Meta:
        ordering = ['author']
