import inspect

from apps.webapp import models
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


for name, _class in inspect.getmembers(models, inspect.isclass):
    try:
        admin.site.register(_class)
    except AlreadyRegistered:
        pass
