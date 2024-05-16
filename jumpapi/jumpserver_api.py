from .base import JumpserverCli


class JumpserverApi(JumpserverCli):
    '''
    Jumpserver API
    '''

    def user_create(self, data):
        url = '/api/v1/users/users/'
        res_data = self._post(url, json=data)
        if 'name' in res_data.keys():
            data = {
                'name': res_data['name'],
                'username': res_data['username'],
                'email': res_data['email']
            }
        else:
            data = {}
        return data

    def get_user_exist(self, data):
        url = '/api/v1/users/users/'
        res_data = self._get(url, data)
        if res_data:
            data = {
                'id': res_data[0]['id'],
                'name': res_data[0]['name'],
                'username': res_data[0]['username'],
                'email': res_data[0]['email']
            }
        else:
            data = {}
        return data

    def get_node_list(self):
        url = '/api/v1/assets/nodes/'
        data = {}
        res_data = self._get(url, data)
        return res_data

    def get_node_exist(self, data):
        url = '/api/v1/assets/nodes/'
        # data = {'full_value': self.full_value}
        res_data = self._get(url, data)

        if res_data:
            data = {
                'id': res_data[0]['id'],
                'name': res_data[0]['name'],
                'value': res_data[0]['value'],
                'full_value': res_data[0]['full_value']
            }
        else:
            data = {}
        return data

    def create_assets_nodes(self, data):
        url = '/api/v1/assets/nodes/'
        # data = {
        #     "value": "北京机器",
        #     "full_value": "/Default/北京机器"
        # }
        res_data = self._post(url, json=data)
        return res_data

    def get_accounts_accounts_list(self):
        url = '/api/v1/accounts/accounts/'
        data = {}
        account_list = []
        res_data = self._get(url, data)
        for info in res_data:
            data = {
                'id': info['id'],
                'name': info['name'],
                'username': info['username'],
                'asset': info['asset']['address'],
            }
            account_list.append(data)
        return account_list

    def get_accounts_accounts_exists(self, data):
        url = '/api/v1/accounts/accounts/'
        res_data = self._get(url, data)
        if res_data:
            for info in res_data:
                data = {
                    'id': info['id'],
                    'name': info['name'],
                    'username': info['username']
                }
        else:
            data = {}
        return data

    def get_assets_hosts(self):
        url = '/api/v1/assets/hosts/'
        data = {}
        res_data = self._get(url, data)
        return res_data

    def get_asset_exists(self, data):
        url = '/api/v1/assets/hosts/'
        res_data = self._get(url, data)
        # print(res_data)
        if res_data:
            data = {
                'id': res_data[0]['id'],
                'hostname': res_data[0]['name'],
                'ip': res_data[0]['address'],
                'platform': res_data[0]['platform']
            }
        else:
            data = {}
        return data

    def create_assets_hosts(self, data):
        url = '/api/v1/assets/hosts/'
        # data = {
        #     "value": "北京机器",
        #     "full_value": "/Default/北京机器"
        # }
        res_data = self._post(url, json=data)
        return res_data

    def update_assets_hosts(self, data, host_id):
        url = '/api/v1/assets/hosts/%s/' % host_id
        res_data = self._put(url, data)
        if 'id' in res_data.keys():
            data = {
                'id': res_data['id'],
                'name': res_data['name'],
                'address': res_data['address'],
                'platform': res_data['platform']
            }
        else:
            data = {}
        return data

    def delete_assets_hosts(self, host_id):
        url = '/api/v1/assets/hosts/{}/'.format(host_id)
        # print(url)
        res_data = self._delete(url)
        if res_data.status_code in [204]:
            res_data = {"状态": "删除成功"}
        else:
            print("删除资产 %s 失败，错误码%s" % (host_id, res_data.status_code))
            res_data = {}

        return res_data

    def account_create(self, data):
        url = '/api/v1/accounts/accounts/'
        res_data = self._post(url, json=data)
        # print(res_data)
        if 'id' in res_data.keys():
            data = {
                'id': res_data['id'],
                'name': res_data['name'],
                'username': res_data['username'],
                'asset_id': res_data['asset']['id'],
                'asset_name': res_data['asset']['name'],
                'asset_address': res_data['asset']['address'],
                'date_created': res_data['date_created']
            }
        else:
            data = {}
        return data

    def get_perms_asset_permissions(self, data):
        url = '/api/v1/perms/asset-permissions/'
        res_data = self._get(url, data)
        print(res_data)
        if res_data:
            data = {
                'name': res_data[0]['name'],
                'id': res_data[0]['id'],
                'accounts': res_data[0]['accounts'],
                'date_start': res_data[0]['date_start'],
                'date_expired': res_data[0]['date_expired']
            }
        else:
            data = {}
        return data

    def creat_perms_asset_permissions(self, data):
        url = '/api/v1/perms/asset-permissions/'
        res_data = self._post(url, json=data)
        data = res_data
        return data

    def update_perms_asset_permissions(self, data, perms_id):
        url = '/api/v1/perms/asset-permissions/{}/'.format(perms_id)
        res_data = self._put(url, data)
        # print(res_data)
        data = res_data
        return data

    def delete_asset_permissions(self, permissions_id):
        url = '/api/v1/perms/asset-permissions/{}/'.format(permissions_id)
        res_data = self._delete(url)
        if res_data.status_code in [204]:
            res_data = {"状态": "删除成功"}
        else:
            print("删除授权 %s 失败，错误码%s" % (permissions_id, res_data.status_code))
            res_data = {}
        return res_data

    def perms_asset_permissions_users_relations(self, data):
        url = '/perms/asset-permissions-users-relations/'
        res_data = self._get(url, data)
        return res_data





jumpserver_api = JumpserverApi()
