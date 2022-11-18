from django.db import models

class Blog(models.Model):
    hl_link = models.CharField(max_length=100, default="Topic")
    post_date = models.DateField(auto_created=True)
    description = models.TextField()

    def __str__(self):
        return self.hl_link


