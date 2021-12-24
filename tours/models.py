from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class TourModel(models.Model):
    title = models.CharField(max_length=64)
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='tours')
    image = models.ImageField(upload_to='tours')
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tour'
        verbose_name_plural = 'tours'
