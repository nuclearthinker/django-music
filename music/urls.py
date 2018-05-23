from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/
    url(r'^register$', views.UserFormView.as_view(), name='register'),

    # /music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/ID/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/ID/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/album_id/
    url(r'/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

    # /music/album_id/favorite
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='song-favorite'),
]
