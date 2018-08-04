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
def NewArtists(request):
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            newartist = form.save()
            newartist.user = request.user
            newartist.DateJoined = timezone.now()
            newartist.save()
            return redirect('ArtistDetails', pk=newartist.pk)
    else:
        form = ArtistForm()
    return render(request, 'website/newartist.html', {'form':form})



#Edit Artist
def EditArtists(request, pk):
    newartist = get_object_or_404(ArtistType, pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES, instance=newartist)
        if form.is_valid():
            newartist = form.save()
            newartist.user = request.user
            newartist.DateJoined = timezone.now()
            newartist.save()
            return redirect('ArtistDetails', pk=newartist.pk)
    else:
        form = ArtistForm(instance=newartist)
    return render(request, 'website/editartists.html', {'form':form})

#  Uploading New Album
def NewAlbums(request):
    if request.method == "POST":
        form = NewAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            newalbums = form.save()
            newalbums.user = request.user
            newalbums.YearReleased  = timezone.now()
            newalbums.save()
            return redirect('AlbumType', pk=newalbums.pk)
    else:
        form = NewAlbumForm()
    return render(request, 'website/newalbums.html', {'form' : form})



#  Edit Album
def EditAlbums(request, pk):
    newalbums = get_object_or_404(AlbumType, pk=pk)
    if request.method == "POST":
        form = NewAlbumForm(request.POST, request.FILES, instance=newalbums)
        if form.is_valid():
            newalbums = form.save()
            newalbums.user = request.user
            newalbums.YearReleased  = timezone.now()
            newalbums.save()
            return redirect('AlbumDetails', pk=newalbums.pk)
    else:
        form = NewAlbumForm(instance=newalbums)
    return render(request, 'website/editalbums.html', {'form' : form})


# Uploading New Song
def NewSong(request):
    if request.method == "POST":
        form = NewSongForm(request.POST, request.FILES)
        if form.is_valid():
            newsongs = form.save()
            newsongs.user = request.user
            newsongs.ReleaseDate = timezone.now()
            newsongs.save()
            return redirect('SongType', pk=newsongs.pk)
    else:
        form = NewSongForm()
    return render(request, 'website/newsongs.html', {'form' : form})

# Edit Song
def EditSong(request, pk):
    newsongs = get_object_or_404(SongType, pk=pk)
    if request.method == "POST":
        form = NewSongForm(request.POST, request.FILES, instance=newsongs)
        if form.is_valid():
            newsongs = form.save()
            newsongs.user = request.user
            newsongs.ReleaseDate = timezone.now()
            newsongs.save()
            return redirect('SongDetails', pk=newsongs.pk)
    else:
        form = NewSongForm(instance=newsongs)
    return render(request, 'website/editnewsongs.html', {'form' : form})
