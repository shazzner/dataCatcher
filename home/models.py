from django.db import models

# Create your models here.
class Page(models.Model):
    page_title = models.CharField(max_length=50)
    page_content = models.CharField(max_length=300)

    def __unicode__(self):
        return self.page_title
