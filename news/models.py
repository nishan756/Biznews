from django.db import models

from django.core.exceptions import ValidationError

from django.utils.text import slugify

from django_summernote.fields import SummernoteTextField

from django.conf import settings

import uuid


class NewsCategory(models.Model):

    slug = models.SlugField(blank = True, null = True, unique = True)

    title = models.CharField(max_length = 60, unique = True)

    def __str__(self):
        return self.title

    def clean(self):

        queryset = NewsCategory.objects.filter(title__iexact = self.title)

        if self.pk:

            queryset = queryset.exclude(pk = self.pk)

        if queryset:

            raise ValidationError("Category with this title already exists.")

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:

        verbose_name_plural = "News Categories"


class News(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)

    image = models.ImageField(upload_to = "news_images/",blank = True, null = True)

    title = models.CharField(max_length = 100, blank = True, null = True)

    category = models.ForeignKey(NewsCategory, on_delete = models.SET_NULL, blank = True, null = True, related_name = "news")

    short_description = models.CharField(max_length = 200)

    description = SummernoteTextField()

    created_at = models.DateTimeField(auto_now_add = True)

    updated_at = models.DateTimeField(blank = True, null = True)

    is_active = models.BooleanField(default = True)

    def __str__(self):
        return f"{self.title} - {self.created_at.date}"

    class Meta:

        ordering = ["-created_at", "-updated_at"]

        verbose_name_plural = "Newses"


class NewsImage(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    news = models.ForeignKey(News, on_delete = models.CASCADE, related_name = "news_images")

    image = models.ImageField(upload_to = "news_images/")

    def __str__(self):

        return f"Image of {self.news.title}"