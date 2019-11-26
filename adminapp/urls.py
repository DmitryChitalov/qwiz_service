from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.GameListView.as_view(), name='games'),
    re_path(r'^games/create/$', adminapp.GameCreateView.as_view(), name='game_create'),
    re_path(r'^games/edit/(?P<pk>\d+)$', adminapp.GameUpdateView.as_view(), name='game_update'),
    re_path(r'^games/del/(?P<pk>\d+)$', adminapp.GameDeleteView.as_view(), name='game_delete'),

    re_path(r'commands$', adminapp.CommandsListView.as_view(), name='commands'),
    re_path(r'^commands/create/$', adminapp.CommandCreateView.as_view(), name='command_create'),
    re_path(r'^commands/edit/(?P<pk>\d+)$', adminapp.CommandUpdateView.as_view(), name='command_update'),
    re_path(r'^commands/del/(?P<pk>\d+)$', adminapp.CommandDeleteView.as_view(), name='command_delete'),

    re_path(r'^requests$', adminapp.RequestsListView.as_view(), name='requests'),
    re_path(r'^requests/create/$', adminapp.RequestCreateView.as_view(), name='request_create'),
    re_path(r'^requests/del/(?P<pk>\d+)$', adminapp.RequestDeleteView.as_view(), name='request_delete'),

    re_path(r'^qwiz/$', adminapp.QwizListView.as_view(), name='qwiz'),
    re_path(r'^qwiz/create/$', adminapp.QwizCreateView.as_view(), name='qwiz_create'),
    re_path(r'^qwiz/edit/(?P<pk>\d+)$', adminapp.qwiz_update, name='qwiz_update'),
    re_path(r'^qwiz/del/(?P<pk>\d+)$', adminapp.QwizDeleteView.as_view(), name='qwiz_delete'),

    re_path(r'^qwestion/create/(?P<pk>\d+)$', adminapp.qwestion_create, name='qwestion_create'),
    re_path(r'^qwestion/update/(?P<pk>\d+)$', adminapp.qwestion_update, name='qwestion_update'),

    re_path('^login/$', adminapp.user_login, name='login'),
    re_path('^logout/$', adminapp.user_logout, name='logout'),
]