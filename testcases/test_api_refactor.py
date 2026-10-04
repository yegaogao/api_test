import pytest
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml

# 1. 读取 YAML 数据
data = read_yaml("data/test_data.yaml")
BASE_URL = "https://jsonplaceholder.typicode.com"


# 2. 用 fixture 提供请求工具实例
@pytest.fixture
def api_client():
    return RequestUtil(BASE_URL)


# 3. 写测试用例，使用读取到的数据
def test_get_post_refactor(api_client):
    # 从 YAML 里拿数据
    url = data["get_post"]["url"]
    expected_id = data["get_post"]["expected_id"]

    # 发请求
    response = api_client.get(url)

    # 断言
    assert response.status_code == 200
    assert response.json()["id"] == expected_id


def test_create_post_refactor(api_client):
    url = data["create_post"]["url"]
    payload = data["create_post"]["payload"]
    expected_status = data["create_post"]["expected_status"]

    response = api_client.post(url, json_data=payload)

    assert response.status_code == expected_status
    assert response.json()["title"] == payload["title"]