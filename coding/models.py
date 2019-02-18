from django.db import models


class PostTag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Post(models.Model):
    post_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    content = models.TextField(max_length=255)
    tag = models.ManyToManyField(PostTag)

    def __str__(self):
        return f'{self.post_date} - {self.author}: {self.subject[:20]}'


class SongGenre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Song(models.Model):
    artist = models.CharField(max_length=150)
    album = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    genre = models.ManyToManyField(SongGenre)
    length = models.PositiveIntegerField()
    video_link = models.CharField(max_length=255)
    song_link = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.artist} - {self.title}'

