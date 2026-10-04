import requests


class RequestUtil:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()  # 使用 Session 可以保持登录状态、复用连接

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, headers=headers)

    def post(self, endpoint, json_data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=json_data, headers=headers)