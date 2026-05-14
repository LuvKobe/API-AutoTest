import requests

# r = requests.get("https://www.baidu.com")
#
# print(r.status_code)
# print(r.text)

# get_r = requests.get("https://www.baidu.com")
# post_r = requests.post("https://www.baidu.com")
#
# #req_r1 = requests.request(method="get", url="https://www.baidu.com")
# #req_r2 = requests.request(method="post", url="https://www.baidu.com")
#
# req_get = requests.request("GET", "https://www.baidu.com")
# req_post = requests.request("POST", "https://www.baidu.com")
#
# print("get:", get_r.status_code)
# print("post:", post_r.status_code)
# # print("method_get:", req_r1.status_code)
# # print("method_post:", req_r2.status_code)
# print("method_get:", req_get)
# print("method_post:", req_post)


'''
    请求博客详情页接口
    必须要先登录 --> 然后在请求头添加用户登录凭证（User_token_header）
    带有参数
'''

url = "http://121.196.200.210:8080/blog/getBlogMessage"

# 定义查询参数
params = {
    "blogId": 2
}

# 定义请求头信息
header = {
    "usertokenheader":"eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlck5hbWUiOiJ6aGFuZ3NhbiIsImV4cCI6MTc3ODc1MTE5M30.atkDG3UYE7IPxjQd7HwQNrVsy5Y89uhVLMWBIBnPaAg"
}

# 使用GET方式请求
r = requests.request(url=url, params=params, headers=header, method='GET')
print(r.json())