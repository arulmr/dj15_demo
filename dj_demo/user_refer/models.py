from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model

class DummyModel(models.Model):
    user_key = models.ForeignKey(get_user_model())

admin.site.register(DummyModel)
