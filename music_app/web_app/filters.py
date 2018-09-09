from .models import *
from django import forms
import django_filters

class SearchFilter(django_filters.FilterSet):
    # file_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model =  SongType
        fields = [ 'SongName','RelaseDate', ]

    class Meta:
    	model = AlbumType
    	fields =  ['AlbumName', 'YearReleased',]


    class Meta:
    	model = ArtistType
    	fiels = ['Name','Bio', 'Born', ]


    class Meta:
    	model = GenreType
    	fields = ['Genre',]

    class Meta:
    	model = BlogPosts
    	fields = ['Titles', 'Description', 'PublishedDate',]


    class Meta:
    	model = VoteSong
    	fields = ['VotedSong',]

