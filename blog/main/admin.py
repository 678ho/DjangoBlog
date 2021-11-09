from django.contrib import admin
from .models import Write
from .models import Comment


admin.site.register(Write)
admin.site.register(Comment)