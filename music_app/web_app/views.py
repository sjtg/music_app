from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import *
from .forms import *
from django.utils import timezone
# from .filters import PhotoFilter
import time


# Home HomePage
def HomePage(request):
    Home = SongType.objects.all().order_by('PublishedDate')
    return render(request, 'website/index.html', {'NewSong' :  Home})

#  List of Genres
def Genres(request):
    Genrelist = GenreType.objects.all().order_by('Genre')
    return render(request, 'website/', {'' : Genrelist})

# List of Artist
def ArtistLists(request):
    Artistlist = SongType.objects.all().order_by('PublishedDate')
    return render(request, 'website/artistlist.html', {'NewSong' : Artistlist })


# Artist Details
def ArtistDetails(request, pk):
    Artistdetail = get_object_or_404(ArtistType, pk=pk)
    return render('website/artistdetails.html', { : })

# Album Details
def AlbumDetails(request, pk):
    Albumdetails = get_object_or_404(AlbumType, pk=pk)
    return render('website/albumdetails.html', { : })

# Details about song
def SongDetails(request, pk):
    Songdetails = get_object_or_404(SongType, pk)
    return render('website/songdetails.html', { : })


#  Add New Artist
def NewArtist(request):



#Edit Artist
def EditArtist(request, pk):


#  Uploading New Album
def NewAlbum(request):

#  Edit Album
def NewAlbum(request):


# Uploading New Song
def UploadSong(request):


# Edit Song
def EditSong(request):
