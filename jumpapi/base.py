import requests, datetime, json
from httpsig.requests_auth import HTTPSignatureAuth

from jumpserver import settings
#172.27.232.250
# new_KEY_ID = '5a7ffec1-e19e-4256-a316-5a370531360c'
# new_SECRET = 'Ap7LxpUWQiTmta9ODeowIWBeqMZIUPtiWv3D'
# Jumpserver_host = 'http://172.27.232.250'
# signature_headers = ['(request-target)', 'accept', 'date', 'host']
# algorithm = 'hmac-sha256'
class JumpserverCli:
    '''
    跳板机
    '''

    def __init__(self):
        self.host = settings.JUMPSERVER.get("Host")
        self.AccessKeyID = settings.JUMPSERVER.get("AccessKeyID")
        self.AccessKeySecret = settings.JUMPSERVER.get("AccessKeySecret")
        self.algorithm = settings.JUMPSERVER.get("algorithm")
        self.signature_headers = ['(request-target)', 'accept', 'date']
        self.gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
        self.headers = {
            'Accept': 'application/json',
            'Date': datetime.datetime.utcnow().strftime(self.gmt_form)
        }
        self.auth = HTTPSignatureAuth(key_id=self.AccessKeyID, secret=self.AccessKeySecret, algorithm=self.algorithm, headers=self.signature_headers)

    def __format_response(self, res):
        data = res.json()
        return data

    def _get(self, url, data):
        url = self.host + url
        kwargs = {
            'auth': self.auth,
            'headers': self.headers,
        }

        res = requests.get(url, data, **kwargs)
        return self.__format_response(res)

    def _get_no_data(self, url):
        url = self.host + url
        kwargs = {
            'auth': self.auth,
            'headers': self.headers,
        }

        res = requests.get(url, **kwargs)
        return self.__format_response(res)

    def _post(self, url, data=None, json=None):
        url = self.host + url
        kwargs = {
            'auth': self.auth,
            'headers': self.headers,
        }

        res = requests.post(url, data, json, **kwargs)
        return self.__format_response(res)

    def _put(self, url, data=None):
        url = self.host + url
        kwargs = {
            'auth': self.auth,
            'headers': self.headers,
        }

        res = requests.put(url, json=data, **kwargs)
        return self.__format_response(res)

    def _delete(self, url):
        url = self.host + url
        kwargs = {
            'auth': self.auth,
            'headers': self.headers,
        }

        res = requests.delete(url, **kwargs)
        return res

