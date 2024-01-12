from django.contrib import admin

from blogs.models import BlogTopic, Blog

# Register your models here.
admin.site.register(BlogTopic)
admin.site.register(Blog)
