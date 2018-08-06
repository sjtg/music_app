# from django.shortcuts import render, redirect, get_object_or_404
# from django.db.models import Q
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.views.generic import View
# from django.views.generic.edit import DeleteView
# from django.urls import reverse_lazy
# from .models import *
# from .forms import *
# from django.utils import timezone
# from .filters import PhotoFilter
# import time


# Blog list function
# def BlogList(request):
#     Bloglist = BlogPosts.objects.all().order_by('PublishedDate')
#     return render(request, 'website/bloglist.html', {'NewBlog' : Bloglist })

# Blog details
# def BlogDetails(request, pk):
#     Blogdetails = get_object_or_404(BlogPost, pk=pk)
#     return render(request, 'website/blogdetails.html', {'NewBlog' : Blogdetails})


# Blog delete
# def Delete(request, pk):
#      = BlogPosts.objects.get(pk=pk)
#     member.delete()
#     return redirect('/crud/')

# New Blog POST
# def NewBlog(request):
#     if request.method == "POST":
#         form = NewBlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             newblogs = form.save()
#             newblogs.user = request.user
#             newblogs.PublishedDate = timezone.now()
#             newblogs.save()
#             return redirect('BlogList', pk=newblogs.pk)
#     else:
#         form = NewBlogForm()
#     return render(request, 'website/newblogs.html', {'form' : form})
#
# def EditBlog(request, pk):
#     newblogs = get_object_or_404(BlogPosts, pk=pk)
#     if request.method =="POST":
#         form = NewBlogForm(request.POST, request.FILES, instance=newblogs)
#         if form.is_valid():
#             newblogs = form.save()
#             newblogs.user = request.user
#             newblogs.PublishedDate = timezone.now()
#             newblogs.save()
#             return redirect('BlogList', pk=newblogs)
#     else:
#         form = NewBlogForm(instance=newblogs)
#     return render(request, 'website/editblogs.html', {'form' : form})
