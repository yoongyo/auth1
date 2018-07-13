from django.db import models
from django.utils import timezone
from django.shortcuts import reverse




class Category(models.Model):
    local_category = models.CharField(max_length=10)
    local_img = models.ImageField(default='null', upload_to='local_img')

    def __str__(self):
        return self.local_category


class Post(models.Model):
    title = models.CharField(max_length=60, default='')
    price = models.CharField(max_length=30, default='')
    time = models.CharField(max_length=10, default='')
    img = models.ImageField(upload_to='user_img', default='local_img/logo2.png')
    local = models.ForeignKey(Category)
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    visited_country = models.CharField(max_length=20)
    next_country = models.CharField(max_length=30, default='ch')
    interest = models.CharField(max_length=60)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    guide_at = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="jyg0172@naver.com")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('travel:local_detail_form', args=[self.local, self.name])

