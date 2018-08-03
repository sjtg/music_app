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

# def HomePage(request):
