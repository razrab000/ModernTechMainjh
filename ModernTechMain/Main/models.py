from django.db import models

# Create your models here.
class Messages(models.Model):
    message = models.CharField('Текст сообщения', max_length=1000)
    contact = models.CharField('Контактная информация', max_length=50)
    def __str__(self):
        return self.message
    class Meta:
        verbose_name='Сообщение'
        verbose_name_plural = "Сообщения"
