from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Categoriya"
        verbose_name_plural = "Categoriyalar"


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Nomi")
    img = models.ImageField(upload_to="post_images", null=True, blank=True, verbose_name="Rasm")
    desc = models.TextField(verbose_name="matn")
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=False, verbose_name="tanlav")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="voqti")
    views = models.IntegerField(default=0)

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

class Contact(models.Model):
    name = models.TextField(max_length=50)
    subject = models.TextField(max_length=100)
    message = models.CharField(max_length=400)
    email = models.EmailField()
    is_solved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class About(models.Model):
    header1 = models.CharField(max_length=200)
    disc1 = models.TextField()
    header2 = models.CharField(max_length=200)
    disc2 = models.TextField()
    image = models.ImageField(upload_to='about_image', null=True, blank=True)
    auther = models.CharField(max_length=50)
    about_auther = models.TextField()
    twitter_urls = models.URLField()
    facebook_urls = models.URLField()
    instagram_urls = models.URLField()
    is_visible = models.BooleanField(default=False)

    def str(self):
        return self.header1

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(max_length=50, blank=True)

class Comment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(max_length=50, blank=True)
    message = models.TextField(max_length=50, blank=True)
    

    post_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.email








