from django.contrib import admin
from .models import *

myModels = Student
admin.site.register(myModels)