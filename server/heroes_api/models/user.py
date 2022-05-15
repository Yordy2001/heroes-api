from xml.parsers.expat import model
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=70, null=False)
    email = models.CharField(max_length=70, null=False)
    password = models.CharField(max_length=100 ,null=False)
    permission = models.CharField(max_length=70, null=False)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.user_name, self.email, self.permission)
