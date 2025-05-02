
from requests import Session
import json


class BaseSession(Session):
    def __init__(self, base_url, username=None, password=None, header=None):

        self.base_url = base_url
        self.username = username
        self.password = password
        self.header = header
        super(BaseSession, self).__init__()

    def get(self, url, **kwargs):
        kwargs.setdefault('timeout', 60)
        url = self.base_url+url
        return super().get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        self._set_header()
        kwargs.setdefault('timeout', 60)
        url = self.base_url + url
        return super().post(url, data=data, headers=self.header, json=json, **kwargs)

    def put(self, url, data=None, **kwargs):
        self._set_header()
        kwargs.setdefault('timeout', 60)
        url = self.base_url + url
        return super().put(url, data=data, headers=self.header, **kwargs)

    def delete(self, url, data=None, **kwargs):
        self._set_header()
        kwargs.setdefault('timeout', 60)
        url = self.base_url + url
        return super().delete(url, data=data, headers=self.header, **kwargs)

    def set_auth(self, auth_url='api/Login/Authenticate'):
        if self.header is None:
            self._set_header()
        data = {
               "name": self.username,
               "password": self.password
              }
        try:
            api_response = self.post(
                auth_url,
                data=json.dumps(data),
                # headers=self.header,
                verify=False)
            token = json.loads(api_response.text)['data']['token']
            self.headers.update({"Authorization": "Bearer "+token})
        except Exception as e:
            raise Exception(
                "API set_auth fail.relative_url: {}, request_data:{}, exception:{}".format(auth_url, data, e)
            )

    def _set_header(self, header=None):
        if header is None:
            header = {
                "Content-Type": "application/json",
                "charset": "UTF-8"
            }
        self.header = header

    def get_with_header(self, url, **kwargs):
        kwargs.setdefault('timeout', 60)
        json_headers = {'content-type': "application/json"}
        # url = self.base_url+url
        return super().get(url, headers=json_headers, **kwargs)


if __name__ == '__main__':
    base_url = 'http://cmsportal.internal.iherbtest.cn/'
    username = 'admin'
    password = 'd033e22ae348aeb5660fc2140aec35850c4da997'

    session = BaseSession(base_url,username,password)
    session.set_auth()
    create_key_end_point = 'api/KeyManager/CreateKey'
    crate_key_data =\
        {
            "key": "IDS_CMS_AUTOMATION_005",
            "content": "string",
            "description": "string",
            "applyAll": True
        }
    header = {
        "Content-Type": "application/json",
        "charset": "UTF-8"
    }
    response = session.post(
        create_key_end_point,
        data=json.dumps(crate_key_data),
        # headers=header
    )
