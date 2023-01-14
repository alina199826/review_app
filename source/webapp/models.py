from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


CATEGORY = [('other', 'other'), ('pharmacy', 'pharmacy'), ('food', 'food')]
PRODUCT_QUANTITY = [(i, str(i)) for i in range(1, 5)]


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False,  verbose_name="title")
    category = models.TextField(max_length=50, null=False, blank=False, choices=CATEGORY, verbose_name="category")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="description")
    img = models.ImageField(null=True, blank=True, upload_to='user_avatar', verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('webapp:view', kwargs={'pk': self.pk})


class Review(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Товар')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="text review")
    rating = models.FloatField(choices=PRODUCT_QUANTITY, default=0)
    modern = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def averagereview(self):
        review = Review.objects.filter(product=self).aggregate(avarage=Avg('rating'))
        avg = 0
        if review["avarage"] is not None:
            avg = float(review["avarage"])
        return avg

    def countreview(self):
        reviews = Review.objects.filter(product=self).aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse('webapp:view', kwargs={'pk': self.pk})
