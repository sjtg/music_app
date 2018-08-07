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
def HomePages(request):
    Home = SongType.objects.all().order_by('PublishedDate')
    return render(request, 'website/index.html', {'NewSong' :  Home})

#  List of Genres
def Genres(request):
    Genrelist = GenreType.objects.all().order_by('Genre')
    return render(request, 'website/', {'newartist' : Genrelist})

# List of Artist
def ArtistLists(request):
    Artistlist = SongType.objects.all().order_by('PublishedDate')
    return render(request, 'website/artistlist.html', {'newartist' : Artistlist })


# Artist Details
def ArtistDetails(request, pk):
    Artistdetail = get_object_or_404(ArtistType, pk=pk)
    return render(request, 'website/artistdetails.html', {'newartist' : Artistdetail})


# Album Details
def AlbumLists(request, pk):
    Albumlists = get_object_or_404(AlbumType, pk=pk)
    return render(request, 'website/albumdetails.html', { 'newalbums': Albumlists})

# Album Details
def AlbumDetails(request, pk):
    Albumdetails = get_object_or_404(AlbumType, pk=pk)
    return render(request, 'website/albumdetails.html', {'newalbums' : Albumdetails})

# Delete Album


# Details about song
def SongLists(request, pk):
    Songlists = get_object_or_404(SongType, pk)
    return render(request, 'website/songdetails.html', { 'newsongs' : Songlists})

# Details about song
def SongDetails(request, pk):
    Songdetails = get_object_or_404(SongType, pk)
    return render(request, 'website/songdetails.html', { 'newsongs' : Songdetails})






# Delete song
@login_required
def RemoveSong(request, pk):
    songs = get_object_or_404(SongType, pk=pk)
    if songs.is_valid():
        newsongs = newsongs.delete()
        newsongs.user = request.user
        newsongs.delete()
        return redirect('SongLists')


# def RemoveSong(request, pk):
#     newsongs = get_object_or_404(SongType, pk=pk)
#     newsongs.delete()
#     return redirect('post_list')

#  Add New Artist
@login_required
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
@login_required
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


# Delete Artist


#  Uploading New Album
@login_required
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
@login_required
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


# Delete Artist


# Uploading New Song
@login_required
def NewSong(request):
    if request.method == "POST":
        form = NewSongForm(request.POST, request.FILES)
        if form.is_valid():
            newsongs = form.save()
            newsongs.user = request.user
            newsongs.ReleaseDate = timezone.now()
            newsongs.save()
            return redirect('SongDetails', pk=newsongs.pk)
    else:
        form = NewSongForm()
    return render(request, 'website/newsongs.html', {'form' : form})

# Edit Song
@login_required
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



# Blog list function
def BlogList(request):
    Bloglist = BlogPosts.objects.all().order_by('PublishedDate')
    return render(request, 'website/bloglist.html', {'NewBlog' : Bloglist })

# Blog details
def BlogDetails(request, pk):
    Blogdetails = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'website/blogdetails.html', {'NewBlog' : Blogdetails})


# Blog delete
# def Delete(request, pk):
#      = BlogPosts.objects.get(pk=pk)
#     member.delete()
#     return redirect('/crud/')

# New Blog POST
@login_required
def NewBlog(request):
    if request.method == "POST":
        form = NewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            newblogs = form.save()
            newblogs.user = request.user
            newblogs.PublishedDate = timezone.now()
            newblogs.save()
            return redirect('BlogList', pk=newblogs.pk)
    else:
        form = NewBlogForm()
    return render(request, 'website/newblogs.html', {'form' : form})

# Edit Blog
@login_required
def EditBlog(request, pk):
    newblogs = get_object_or_404(BlogPosts, pk=pk)
    if request.method =="POST":
        form = NewBlogForm(request.POST, request.FILES, instance=newblogs)
        if form.is_valid():
            newblogs = form.save()
            newblogs.user = request.user
            newblogs.PublishedDate = timezone.now()
            newblogs.save()
            return redirect('BlogList', pk=newblogs)
    else:
        form = NewBlogForm(instance=newblogs)
    return render(request, 'website/editblogs.html', {'form' : form})
