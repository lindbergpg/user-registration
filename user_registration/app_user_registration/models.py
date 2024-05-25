from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(max_length=255)
    user_age = models.IntegerField()
