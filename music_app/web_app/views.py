from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import *
from .forms import *
from django.utils import timezone
from .filters import SearchFilter
import time


# Home HomePage
def HomePages(request):
    SongHome = SongType.objects.all().order_by('-ReleaseDate')
    BlogHome = BlogPosts.objects.all().order_by('-PublishedDate')
    query = request.GET.get("searchs")
    if query:
        SongHome = SongHome.filter(
            Q(AlbumNames__icontains=query)|
            Q(SongName__icontains=query)
        ).distinct()

    return render(request, 'website/index.html', {'NewSong' :  SongHome, 'NewBlog' : BlogHome })

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
def AlbumLists(request):
    Albumlists = get_object_or_404(AlbumType)
    return render(request, 'website/albumlists.html', { 'newalbums': Albumlists})

# Album Details
def AlbumDetails(request, pk):
    Albumdetails = get_object_or_404(AlbumType, pk=pk)
    return render(request, 'website/albumdetails.html', {'newalbums' : Albumdetails})


# Song List
def SongLists(request):
    Songlists = SongType.objects.all().order_by('-ReleaseDate')
    return render(request, 'website/songlists.html', { 'NewSong' : Songlists})

# Song Details
def SongDetails(request, pk):
    Songdetails = get_object_or_404(SongType, pk=pk)
    return render(request, 'website/songdetails.html', { 'newsongs' : Songdetails})



#  Add New Artist
@login_required
def NewArtists(request):
    if request.method == "POST":
        form = NewNewArtistForm(request.POST, request.FILES)
        if form.is_valid():
            newartist = form.save()
            newartist.user = request.user
            newartist.DateJoined = timezone.now()
            newartist.save()
            return redirect('ArtistDetails', pk=newartist.pk)
    else:
        form = NewArtistForm()
    return render(request, 'website/newartists.html', {'form':form})



#Edit Artist
@login_required
def EditArtists(request, pk):
    newartist = get_object_or_404(ArtistType, pk=pk)
    if request.method == "POST":
        form = NewArtistForm(request.POST, request.FILES, instance=newartist)
        if form.is_valid():
            newartist = form.save()
            newartist.user = request.user
            newartist.DateJoined = timezone.now()
            newartist.save()
            return redirect('ArtistDetails', pk=newartist.pk)
    else:
        form = NewArtistForm(instance=newartist)
    return render(request, 'website/editartists.html', {'form':form})




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
def BlogLists(request):
    Bloglist = BlogPosts.objects.all().order_by('PublishedDate')
    return render(request, 'website/bloglists.html', {'NewBlog' : Bloglist })

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


# Delete Blog
@login_required
def RemoveBlog(request, pk):
    blogs = get_object_or_404(BlogPosts, pk=pk)
    if oldblogs.is_valid():
        oldblogs = oldblogs.delete()
        oldblogs.user = oldblogs.user
        oldblogs.delete()
        return redirect('BlogLists')


# Delete Artist
@login_required
def RemoveArtist(request, pk):
    artists = get_object_or_404(ArtistType, pk=pk)
    if artists.is_valid():
        oldartists = oldartists.delete()
        oldartists.user = request.user
        oldartists.delete()
        return redirect('ArtistLists')

#  Delete Album
@login_required
def RemoveAlbum(request, pk):
    albums = get_object_or_404(AlbumType, pk=pk)
    if albums.is_valid():
        oldalbums = oldalbums.delete()
        oldalbums.user = request.user
        oldalbums.delete()
        return redirect('AlbumLists')


# Delete song
@login_required
def RemoveSong(request, pk):
    songs = get_object_or_404(SongType, pk=pk)
    if songs.is_valid():
        oldsongs = oldsongs.delete()
        oldsongs.user = request.user
        oldsongs.delete()
        return redirect('SongLists')


# def RemoveSong(request, pk):
#     newsongs = get_object_or_404(SongType, pk=pk)
#     newsongs.delete()
#     return redirect('post_list')



#search function
def search(request):
    SearchList = SongType.objects.all().order_by('-ReleaseDate')
    query = request.GET.get("search")
    if query:
        SearchList = SearchList.filter(
            Q(AlbumNames__icontains=query)|
            Q(SongName__icontains=query)
        ).distinct()
    return render(request, 'website/searchlist.html', {'NewSong' : SearchList})
