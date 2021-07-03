from django.contrib import admin
from features import views

# Register your models here.
from features.models import (
    Info
    )
admin.site.register([Info])