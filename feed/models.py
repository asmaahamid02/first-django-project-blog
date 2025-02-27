from django.db import models
from sorl.thumbnail import ImageField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140,null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = ImageField()
    created_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self) -> str:
        return self.title
