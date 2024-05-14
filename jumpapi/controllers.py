from django.http import JsonResponse
import json
from .jumpserver_api import jumpserver_api
import requests


def get_user_from_jumpserver(request):
    # 初始化JumpserverAPI对象
    data = json.loads(request.body)
    # 调用get_user_exist方法并获取用户数据
    user_data = jumpserver_api.get_user_exist(data)
    # 返回Django的JsonResponse
    return JsonResponse(user_data, safe=False)


def create_user_to_jumpserver(request):
    data = json.loads(request.body)
    user_data = jumpserver_api.user_create(data)
    return JsonResponse(user_data)


def get_node_list_to_jumpserver(request):
    node_data = jumpserver_api.get_node_list()
    return JsonResponse(node_data, safe=False)


def get_node_exists_to_jumpserver(request):
    data = json.loads(request.body)
    node_data = jumpserver_api.get_node_exist(data)
    return JsonResponse(node_data)


def create_node_to_jumpserver(request):
    data = json.loads(request.body)
    node_data = jumpserver_api.create_assets_nodes(data)
    return JsonResponse(node_data)


def create_host_to_jumpserver(request):
    data = json.loads(request.body)
    host_data = jumpserver_api.create_assets_hosts(data)
    return JsonResponse(host_data)


def update_host_to_jumpserver(request):
    host_id = "063c698b-6ce5-4bea-8ce1-f46c56e365ae"
    data = json.loads(request.body)
    # print(data)
    host_data = jumpserver_api.update_assets_hosts(data, host_id)
    return JsonResponse(host_data)


def delete_host_to_jumpserver(request):
    host_id = "b16b63cd-14d8-4007-bc11-15b2da0cb180"
    # data = json.loads(request.body)
    host_data = jumpserver_api.delete_assets_hosts(host_id)
    return JsonResponse(host_data)


def get_accounts_list_to_jumpserver(request):
    account_data = jumpserver_api.get_accounts_accounts_list()
    return JsonResponse(account_data, safe=False)


def get_accounts_exists_to_jumpserver(request):
    data = json.loads(request.body)
    account_data = jumpserver_api.get_accounts_accounts_exists(data)
    return JsonResponse(account_data, safe=False)


def get_assets_hosts_to_jumpserver(request):
    asset_host_data = jumpserver_api.get_assets_hosts()
    return JsonResponse(asset_host_data, safe=False)


def get_assets_hosts_exists_to_jumpserver(request):
    data = json.loads(request.body)
    asset_host_data = jumpserver_api.get_asset_exists(data)
    return JsonResponse(asset_host_data, safe=False)


def create_account_to_jumpserver(request):
    data = json.loads(request.body)
    account_create_data = jumpserver_api.account_create(data)
    return JsonResponse(account_create_data, safe=False)


def perms_asset_permissions_exists(request):
    data = json.loads(request.body)
    perms_asset_host_data = jumpserver_api.get_perms_asset_permissions(data)
    return JsonResponse(perms_asset_host_data, safe=False)


def create_asset_permissions(request):
    data = json.loads(request.body)
    # print(data)
    perms_asset_host_data = jumpserver_api.creat_perms_asset_permissions(data)
    return JsonResponse(perms_asset_host_data)


def update_asset_permissions(request):
    perms_id = "d0c4ecb5-2c3b-40d8-b874-3f5812edc6fe"
    data = json.loads(request.body)
    print(data)
    perms_asset_host_data = jumpserver_api.update_perms_asset_permissions(data, perms_id)
    return JsonResponse(perms_asset_host_data)


def delete_asset_permissions(request):
    permissions_id = "d0c4ecb5-2c3b-40d8-b874-3f5812edc6fe"
    # data = json.loads(request.body)
    host_data = jumpserver_api.delete_asset_permissions(permissions_id)
    return JsonResponse(host_data)


def get_perms_asset_permissions_users_relations(request):
    data = json.loads(request.body)
    perms_asset_host_data = jumpserver_api.perms_asset_permissions_users_relations(data)
    return JsonResponse(perms_asset_host_data, safe=False)


