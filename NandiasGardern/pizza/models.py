from django.db import models


class Size(models.Model):
    title = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.title[:20]

class Pizza(models.Model):
    topping1 = models.CharField(blank=False, max_length=200)
    topping2 = models.CharField(blank=False, max_length=200)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "hello write here"

    def __str__(self):
        return self.topping1[:30]

    class Meta:
        verbose_name_plural = 'Pizza'
