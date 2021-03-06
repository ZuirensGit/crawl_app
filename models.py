from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Spider(models.Model):
    domain = models.CharField(max_length=63, unique=True)
    stype = models.CharField(max_length=63, default='single', verbose_name=u'type')
    status = models.CharField(max_length=63, default='debug')
    entry = models.CharField(max_length=1023)
    pages = models.IntegerField(blank=True, null=True)
    url_xpath = models.CharField(max_length=4095)
    title_xpath = models.CharField(max_length=4095)
    content_xpath = models.CharField(max_length=4095)
    author_xpath = models.CharField(max_length=4095, blank=True, null=True)
    date_xpath = models.CharField(max_length=4095, blank=True, null=True)
    author_pattern = models.CharField(max_length=63, blank=True, null=True)
    date_pattern = models.CharField(max_length=63, blank=True, null=True)
    release = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.domain)

    class Meta:
        verbose_name = _('SPIDER')
        verbose_name_plural = verbose_name


class Joblog(models.Model):
    name = models.CharField(max_length=255)
    event = models.TextField()
    start_time = models.DateTimeField(default=timezone.now)
    finish_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, default='running')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('JOB LOG')
        verbose_name_plural = verbose_name
