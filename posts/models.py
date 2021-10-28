from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

User = get_user_model()


class Posts(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(
        upload_to='posts_images/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    text = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class Comments(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children_comments',
        on_delete=models.CASCADE,
        verbose_name='Родительский коментарий'
    )
    post = models.ForeignKey(
        Posts,
        blank=True,
        null=True,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    image = models.ImageField(
        upload_to='comments_images/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    text = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']
        constraints = [
            models.CheckConstraint(
                check=(
                    (Q(post=None) & ~Q(parent=None))
                    | (~Q(post=None) & Q(parent=None))
                ),
                name='check_pair_post_parent'
            ),
        ]

    def __str__(self):
        return self.text[:50]
