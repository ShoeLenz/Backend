from django.db import models

# Create your models here.

class PageModel(models.Model):
    objects = models.Manager()
    postId = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        )
    brand = models.CharField(max_length=30)
    modelNumber = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    minSize = models.SmallIntegerField(null=True)
    maxSize = models.SmallIntegerField(null=True)
    price = models.IntegerField()


class PageImageModel(models.Model):
    imageId = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        )
    postId = models.ForeignKey(PageModel, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField()