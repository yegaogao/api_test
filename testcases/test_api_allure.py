import allure
import pytest
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml

data =read_yaml("data/test_data.yaml")
BASE_URL="https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_client():
    return RequestUtil(BASE_URL)

@allure.feature("帖子管理模块")
class TestPosts:
    @allure.story("获取帖子")
    @allure.title("获取单条帖子")
    def test_get_post(self,api_client):
        with allure.step("1.准备测试数据"):
            url=data["get_post"]["url"]
            expected_id= data["get_post"]["expected_id"]

        with allure.step("2.发送GET请求"):
            response=api_client.get(url)

        with allure.step("3.断言状态码和响应字段"):
                assert response.status_code==200
                assert response.json()["id"]==expected_id
                
    @allure.story("创建帖子")
    @allure .title("新建帖子")
    def test_create_post(self,api_client):
        with allure.step("1.准备测试数据"):

            url=data["create_post"]["url"]
            payload=data["create_post"]["payload"]
            expected_status=data["create_post"]["expected_status"]

        with allure.step("2.发送POST请求"):
                response=api_client.post(url,json_data=payload)
            
        with allure.step("3.断言状态码和标题"):
                assert response.status_code==expected_status
                assert response.json()["title"]==payload["title"]
