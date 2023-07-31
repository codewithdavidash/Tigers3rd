from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class HTML(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='core/static/media', default='core/static/media/html_css.jpg')
    notes = models.FileField(
        upload_to='core/static/notes', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'HTML'

    def __str__(self):
        return self.title


class JS(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='core/static/media', default='core/static/media/js.png')
    notes = models.FileField(
        upload_to='core/static/notes', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'JS'

    def __str__(self):
        return self.title


class PYTHON(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='core/static/media', default='core/static/media/images.png')
    notes = models.FileField(
        upload_to='core/static/notes', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Python'

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=100)
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-created_at',)


class Assignments(models.Model):
    COURSE_CHOICES = (
        ('html/css', 'HTML|CSS'),
        ('js', 'Js'),
        ('python', 'Python')
    )
    username = models.CharField(max_length=100)
    courses = models.CharField(
        choices=COURSE_CHOICES, max_length=8, blank=True, null=True)
    assignments = models.FileField(
        upload_to='core/static/students_assigments', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Assignments'
        ordering = ('-posted_at',)


class Profile(models.Model):
    user = models.ForeignKey(
        User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='core/static/media', default='core/static/media/user.png')
