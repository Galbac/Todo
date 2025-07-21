import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название заголовка")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Описание")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    due_date = models.DateField(blank=True, null=True, verbose_name="Крайний срок")
    photo = models.ImageField(
        upload_to="todo_photo", blank=True, verbose_name="Фото", null=True
    )

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            while TodoList.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"
            self.slug = slug
        super().save(*args, **kwargs)
