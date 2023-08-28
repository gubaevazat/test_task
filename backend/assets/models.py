from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Asset(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='название'
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание актива'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'актив'
        verbose_name_plural = 'активы'
        default_related_name = 'assets'

    def __str__(self):
        return self.name


class AssetInWork(models.Model):
    worker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='работник',
    )
    asset = models.ForeignKey(
        Asset,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='актив'
    )
    TO_DO = 'TD'
    IN_PROGRESS = 'IP'
    COMPLETE = 'CO'
    STATUS_CHOICES = [
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In progress'),
        (COMPLETE, 'Complete')
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=TO_DO
    )
    todo_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата размещения задания'
    )
    begin_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='начало работы'
    )
    end_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='конец работы'
    )
    report = models.TextField(
        blank=True,
        verbose_name='отчёт'
    )

    class Meta:
        verbose_name = 'актив в работе'
        verbose_name_plural = 'активы в работе'

    def save(self, *args, **kwargs):
        if self.status == self.IN_PROGRESS:
            self.begin_date = timezone.now()
        elif self.status == self.COMPLETE:
            self.end_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.asset.name}, {self.worker.username}, {self.status}'
