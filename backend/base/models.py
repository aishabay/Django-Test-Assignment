from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class News(models.Model):
    POPULARITY_LEVEL_1 = 1
    POPULARITY_LEVEL_2 = 2
    # POPULARITY_LEVEL_3 = 3

    POPULARITY_LEVEL_CHOICES = [
        (POPULARITY_LEVEL_1, 1),
        (POPULARITY_LEVEL_2, 2),
        # (POPULARITY_LEVEL_3, 3),
    ]

    headline = models.CharField(max_length=200, blank=False)
    image = models.ImageField(blank=False, upload_to='news')
    image_source = models.CharField(max_length=30, blank=False)
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)
    short_content = models.TextField(blank=False)
    content = models.TextField(blank=False)
    popularity_level = models.IntegerField(blank=False, choices=POPULARITY_LEVEL_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
