from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=False)
    descricao = models.TextField(max_length=600, blank=False, null=False)
    url = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
