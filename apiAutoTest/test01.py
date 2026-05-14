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

# url = "http://121.196.200.210:8080/blog/getBlogMessage"
#
# # 定义查询参数
# params = {
#     "blogId": 2
# }
#
# # 定义请求头信息
# header = {
#     "usertokenheader":"eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlck5hbWUiOiJ6aGFuZ3NhbiIsImV4cCI6MTc3ODc1MTE5M30.atkDG3UYE7IPxjQd7HwQNrVsy5Y89uhVLMWBIBnPaAg"
# }
#
# # 使用GET方式请求
# r = requests.request(url=url, params=params, headers=header, method='GET')
# print(r.json())

# '''
#     博客系统登录接口
#     POST 表单格式
# '''
#
# url = "http://121.196.200.210:8080/user/login"
#
# data = {
#     "userName": "zhangsan",
#     "password": "123456"
# }
#
# r = requests.request(method="POST",url=url, data=data)
# print(r.json())

'''
    博客园用户详情页
    添加用户登录凭证--cookie（.Cnblogs.AspNetCore.Cookies）
'''

url = "https://account.cnblogs.com/user/userinfo"

cookie = {
    ".Cnblogs.AspNetCore.Cookies":"CfDJ8OBZrxGJLy5MvghieKIKXCxbUmIkNTWX8sFnVgjSYCK2xJeRRRkWqJpqml3XWNmu3h_h2ZF3JQfhpPEwc8yqABU5rTqRfr-02D0yGdZBQaGyWq2-ArdENUlfGM81xX6aGUq3rcpt84qAyN0ybJF9ZR5VSiedSoHJJV8VXFvsUSJkWiHbdITWfR0ZpmxvcGkEsxMDu0lYKxcn_BdaSC-RgZyOLM9KX28IgLqwHXcw-Js-YjSYZT68CpMs6awhj8wmxzRxztaHetu_zZHq-zevyw_N9037Z6XNfBTox8M_bManwl5oV6dY8G9PrhKbadQIfvvX-AKP8mZLLyCVvUDooEGWLYgCb1wyc9FBWMua0y-96Sf2rv_-RBsJPZFCR0EuHlWoHqvct7fa2Z9JdnAMFzUdjc0Yv3coRcwRg8k2n-72RsgMLCy7BmYe0puqFS8QqGNrpCcUOOkIO85-aNr0fbywN1ErrMdx283X7B8ROPTtJ8vr_AsDFItcPUdLiZFBzVnWibu-UWJ5vGGl-WdnkEch46v1NaqYjDkOBzE-NmM5hB9ZKHeVmMlHNIFNzaQAHA;"
}

r = requests.request(method="GET",url=url,cookies=cookie)

print(r.text)