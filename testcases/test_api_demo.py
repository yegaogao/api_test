import requests
import pytest
BASE_URL = "https://jsonplaceholder.typicode.com"

# def test_get_post():
#     # 1. 准备数据（URL）
#     url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # 2. 发送请求
#     response = requests.get(url)
    
#     # 3. 断言结果
#     assert response.status_code == 200
#     assert response.elapsed.total_seconds() < 2
#     print(response.json())  # 打印返回的 JSON 数据


# def test_post_post():
#     url = "https://jsonplaceholder.typicode.com/posts"
    
#     # 2. 发送请求
#     response = requests.post(url,json={"title": "foo", "body": "bar", "userId": 1})
    
#     # 3. 断言结果
#     assert response.status_code == 201
#     assert response.json()["title"] == "foo"
#     assert response.elapsed.total_seconds() < 2
#     print(response.json())  # 打印返回的 JSON 数据

# def test_put_post():
#     url = "https://jsonplaceholder.typicode.com/posts/1"
    
#     # 2. 发送请求
#     response = requests.put(url,json={"id": 1, "title": "updated", "body": "bar", "userId": 1})
    
#     # 3. 断言结果
#     assert response.status_code == 200
#     assert response.json()["title"] == "updated"
#     assert response.elapsed.total_seconds() < 2
#     print(response.json())  # 打印返回的 JSON 数据

# def test_delete_post():
#     url = "https://jsonplaceholder.typicode.com/posts/1"
    
#     # 2. 发送请求
#     response = requests.delete(url)
    
#     # 3. 断言结果
#     assert response.status_code == 200
#     assert response.elapsed.total_seconds() < 2
#     print(response.json())  # 打印返回的 JSON 数据

# def test_headers_post():
#     url = "https://jsonplaceholder.typicode.com/posts/1"
#     headers = {"Authorization": "Bearer fake_token_123"}
    
#     # 2. 发送请求
#     response =requests.get(url, headers=headers)
    
#     # 3. 断言结果
#     assert response.status_code == 200
#     assert response.elapsed.total_seconds() < 2
#     print(response.json())  # 打印返回的 JSON 数据


def test_get1_post():
    # 1. 准备数据（URL）
    url = f"{BASE_URL}/posts/1"
    
    # 2. 发送请求
    response = requests.get(url)
    
    # 3. 断言结果
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.elapsed.total_seconds() < 2
    print(response.json())  # 打印返回的 JSON 数据

# def test_get2_post():
#     url = f"{BASE_URL}/posts"
    
#     response = requests.get(url)
    
#     assert response.status_code == 200
#     assert len(response.json()) == 100
#     assert response.elapsed.total_seconds() < 2
#     print(response.json())  # 打印返回的 JSON 数据


def test_post_post():
    url = f"{BASE_URL}/posts"
    
    # 2. 发送请求
    response = requests.post(url,json={"title": "foo", "body": "bar", "userId": 1})
    
    # 3. 断言结果
    assert response.status_code == 201
    assert response.json()["title"] == "foo"
    assert response.elapsed.total_seconds() < 2
    print(response.json())  # 打印返回的 JSON 数据

def test_put_post():
    url=f"{BASE_URL}/posts/1"
    response=requests.put(url,json={"id":1,"title":"updated","body":"bar","userId":1})
    assert response.status_code==200
    assert response.json()["title"]=="updated"
    print(response.json())  # 打印返回的 JSON 数据

def test_delete_post():
    url=f"{BASE_URL}/posts/1"
    response=requests.delete(url)
    assert response.status_code==200
    assert response.elapsed.total_seconds()<2
    print(response.json())

def test_get404_post():
    
    # 2. 发送请求
    response = requests.get(f"{BASE_URL}/posts/99999")
    
    # 3. 断言结果
    assert response.status_code == 404
    assert response.elapsed.total_seconds() < 2

# def test_get2_post():
#     params = {"userId": 1}
    
#     response = requests.get(f"{BASE_URL}/posts",params =params )
    
#     assert response.status_code == 200
#     assert response.elapsed.total_seconds() < 2
#     for post in response.json(): assert post["userId"] == 1
#     print(response.json())  # 打印返回的 JSON 数据

def test_headers_post():
    url=f"{BASE_URL}/posts/1"
    headers={"Authorization":"bearer fake_tonken_123"}
    response=requests.get(url,headers=headers)
    assert response.status_code==200
    assert response.elapsed.total_seconds()<2
    print(response.json())

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_post_by_id(post_id):
    url=f"{BASE_URL}/posts/{post_id}"
    response=requests.get(url)
    assert response.status_code==200
    data = response.json()
    assert data["id"] == post_id
    print(response.json())



