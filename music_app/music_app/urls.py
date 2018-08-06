"""music_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from web_app import views as web_views
# from blog import views as blog_views
from accounts import views as accounts_views
from web_app import views
# from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePages, name='HomePages'),
    url(r'^genres/$', views.Genres, name='Genres'),

    url(r'^artistlist/$', views.ArtistLists, name='ArtistLists'),
    url(r'^artistdetails/(?P<pk>\d+)/$', views.ArtistDetails, name='ArtistDetails'),

    url(r'^albumlist/$', views.AlbumLists, name='AlbumLists'),
    url(r'^albumdetails/(?P<pk>\d+)/$', views.AlbumDetails, name='AlbumDetails'),

    url(r'^songlist/$', views.SongLists, name='SongLists'),
    url(r'^songdetails/(?P<pk>\d+)/$', views.SongDetails, name='SongDetails'),
    url(r'^artist/new/$', views.NewArtists, name='NewArtists'),
    url(r'^artist/(?P<pk>\d+)/edit/$', views.EditArtists, name='EditArtists'),
    url(r'^albums/new/$', views.NewAlbums, name='NewAlbums'),
    url(r'^albums/(?P<pk>\d+)/edit/$', views.EditAlbums, name='EditAlbums'),
    url(r'^songs/new/$', views.NewSong, name='NewSong'),
    url(r'^songs/(?P<pk>\d+)/edit/$', views.EditSong, name='EditSong'),

    url(r'^blog/$', views.BlogList, name='BlogList'),
    url(r'^blog/new/$', views.NewBlog, name='NewBlog'),
    url(r'^blog/(?P<pk>\d+)/edit/$', views.EditBlog, name='EditBlog'),
    url(r'^blog/(?P<pk>\d+)/$', views.BlogDetails, name='BlogDetails'),

    url(r'^signup/$', accounts_views.signup, name='signup' ),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
