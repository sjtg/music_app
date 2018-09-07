from .models import *
from django import forms
import django_filters

class SearchFilter(django_filters.FilterSet):
    # file_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model =  SongType
        fields = [ 'AlbumNames', 'SongName',]

