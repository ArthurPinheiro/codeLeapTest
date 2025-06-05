from django.db import models

class Career(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    created_datetime = models.DateField(auto_now_add=False, blank=False, null=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.title