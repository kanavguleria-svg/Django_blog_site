from django.contrib import admin
from mediumeditor.admin import MediumEditorAdmin
from blog.models import Post,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
