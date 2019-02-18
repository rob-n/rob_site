from django.contrib import admin

from .models import PostTag, Post, SongGenre, Song

# Register your models here.

admin.site.register(PostTag)
admin.site.register(Post)
admin.site.register(SongGenre)
admin.site.register(Song)

