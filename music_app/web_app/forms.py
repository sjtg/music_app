from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Artist Form
class NewArtistForm(forms.ModelForm):
    class Meta:
        model = ArtistType
        fields = ['Name', 'Born', 'Bio', 'DateJoined', 'ArtistPictures']

# Album Form
class NewAlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumType
        fields = ['ArtistName', 'AlbumName', 'AlbumCover', 'YearReleased']

# Song Form
class NewSongForm(forms.ModelForm):
    class Meta:
        model = SongType
        fields = ['AlbumNames', 'SongName', 'Song', 'ReleaseDate']

# Blog Form
class NewBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPosts
        fields = ['Titles', 'Description', 'BlogImage', 'PublishedDate']
