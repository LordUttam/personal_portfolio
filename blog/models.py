from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, default=None)
    date = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title


