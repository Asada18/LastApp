from django.db import models

from account.models import MyUser


class Stories(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='stories')
    image = models.ImageField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=225)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')


