from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Tovary(models.Model):
    photo = models.ImageField(verbose_name='Фотки', upload_to='photos/%Y/%m/%d')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category',related_name='category', default=False)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

class Coment(models.Model):
    title = models.TextField()
    name = models.CharField(max_length=50)
    kartinka = models.TextField()

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['name']