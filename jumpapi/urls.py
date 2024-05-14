from django.urls import path
from . import views

from .controllers import *

urlpatterns = [

    path('user_list/', get_user_from_jumpserver,name='get_user'),
    path('user_create/', create_user_to_jumpserver, name='user_create'),
    path('node_list/', get_node_list_to_jumpserver, name='get_node'),
    path('node_exists/', get_node_exists_to_jumpserver, name='get_node_exists'),
    path('node_create/', create_node_to_jumpserver, name='node_create'),
    path('account_list/', get_accounts_list_to_jumpserver, name='get_account'),
    path('account_exists/', get_accounts_exists_to_jumpserver, name='get_account_exists'),
    path('assets_hosts_list/', get_assets_hosts_to_jumpserver, name='get_assets_hosts'),
    path('assets_hosts_exists/', get_assets_hosts_exists_to_jumpserver, name='get_assets_hosts_exists'),
    path('account_create/', create_account_to_jumpserver, name='account_create'),
    path('assets_host_create/', create_host_to_jumpserver, name='host_create'),
    path('assets_host_update/', update_host_to_jumpserver, name='host_update'),
    path('assets_host_delete/', delete_host_to_jumpserver, name='host_delete'),
    path('perms_asset_permissions_list/', perms_asset_permissions_exists, name='perms_asset_permissions_list'),
    path('create_asset_permissions/', create_asset_permissions, name='create_asset_permissions'),
    path('update_asset_permissions/', update_asset_permissions, name='update_asset_permissions'),
    path('delete_asset_permissions/', delete_asset_permissions, name='update_asset_permissions'),
    path('perms_asset_permissions_users_relations_list/', get_perms_asset_permissions_users_relations, name='perms_asset_permissions_users_relations_list'),

    path('', views.index, name='index'),

]