from django.db import models


# we convert it to SQL ('DDL') using django ORM

class Post(models.Model):
    text = models.TextField()

    def __str__(self):  # toString()
        return self.text[:50]
