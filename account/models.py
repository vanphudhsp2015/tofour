from django.db import models

# Create your models here.

class InfoAccount(models.Model):
    ACCOUNT_CHOICES = (
        ('admin','admin'),
        ('account','account'),
    )
    avatar = models.FileField(upload_to = 'tourer/',default='/default/avatar.jpg')
    question = models.CharField(max_length=250,default='question')
    name = models.CharField(max_length=250)
    info = models.CharField(max_length=250)
    author = models.CharField(max_length=250,choices=ACCOUNT_CHOICES,null=True,blank=True,default='account')

    class Meta:
        abstract = True

class Account(InfoAccount):
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' - ' + self.email