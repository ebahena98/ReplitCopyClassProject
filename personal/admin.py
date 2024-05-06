from django.contrib import admin
from personal.models import Question

# Registering the Question model with the Django admin interface
admin.site.register(Question)