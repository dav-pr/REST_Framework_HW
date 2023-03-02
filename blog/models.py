
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils import timezone


# Create your models here.
GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Other"))
)

class Author(models.Model):
    name = models.CharField(max_length=256)
    pseudonym = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.pseudonym

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"
        ordering = ['name']

class Posts(models.Model):
    content = models.CharField(max_length=1024)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=1)

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"


class Comments(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=64)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

class LikePost(models.Model):
    like = models.BooleanField(null = True)
    post = models.ForeignKey('Posts', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='like_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Вподобання статей"
        verbose_name_plural = "Вподобання статей"


class LikeComments(models.Model):
    like = models.BooleanField(null=True)
    post = models.ForeignKey('Comments', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='like_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Вподобання коментарів"
        verbose_name_plural = "Вподобання коментарів"


