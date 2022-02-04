from django.db import models
from autoslug  import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User=get_user_model()

class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to="")

    def __str__(self):
        return self.user.username
class Category(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
#
# class Post(models.Model):
#     title=models.CharField(max_length=200)
#     slug=AutoSlugField(populate_from='title')
#     overview=models.TextField()
#     date=models.DateTimeField(auto_now_add=True)
#     content=models.ForeignKey(Author,on_delete=models.CASCADE)
#     categories=models.ManyToManyField(Category)
#     published=models.BooleanField()
#
#     def __str__(self):
#         return self.title
# Create your models here.
#
class Post(models.Model):
    '''
      Database Table for Blogs
    '''
    blog_title=models.CharField(max_length=150,verbose_name='Blog Title')
    slug = AutoSlugField(populate_from='blog_title')
    # blog_description = models.CharField(max_length=2000, verbose_name='Description')
    blog_description=RichTextField(max_length=2000,verbose_name='Description')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()

    created_on=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.blog_title
