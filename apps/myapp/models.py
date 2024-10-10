from django.db import models

# Create your models here.
CATEGORY_COLOR_CHOICES = [
    ('#ff3300', 'red'),
    ('#ffff00', 'Yellow'),
    ('#ff0066', 'pink'),
]

from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class ProductCategory(TimeStampedModel):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=16, null=True, blank=True,
                             choices=CATEGORY_COLOR_CHOICES,
                             verbose_name="Color category",
                             help_text="Select color category"
                             )

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
