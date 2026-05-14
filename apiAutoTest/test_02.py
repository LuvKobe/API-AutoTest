import requests
from bs4 import BeautifulSoup

# class Test():
#     def test01(self):
#         r = requests.get("http://www.baidu.com")
#         print(r.text)
#
#     def test02(self):
#         url = "http://121.196.200.210:8080/user/login"
#
#         data = {
#             "userName": "zhangsan",
#             "password": "123456"
#         }
#
#         r = requests.request(method="POST",url=url, data=data)
#         print(r.json())

# class Test():
#     def __init__(self):
#         print("-----init-------")
#     def test_a(self):
#         print("-----test_a----")

class Test():

    def test01(self):
        url = "http://121.196.200.210:8080/user/login"
        data = {
            "userName": "zhangsan",
            "password": "123456"
        }
        r = requests.request(method="POST",url=url, data=data)
        print(r.json())