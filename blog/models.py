from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField('Artical title', max_length=100, unique=True)
    text = models.TextField('Main text')
    date = models.DateTimeField('Publication date', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    views = models.IntegerField('Views', default=1)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X Large'),
    )

    shop_sizes = models.CharField(choices=sizes, max_length=2, default='S')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"pk": self.pk})
    

    class Meta:
        verbose_name = 'News',
        verbose_name_plural = 'News'