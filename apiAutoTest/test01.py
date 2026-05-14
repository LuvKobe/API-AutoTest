import requests

# r = requests.get("https://www.baidu.com")
#
# print(r.status_code)
# print(r.text)

get_r = requests.get("https://www.baidu.com")
post_r = requests.post("https://www.baidu.com")

#req_r1 = requests.request(method="get", url="https://www.baidu.com")
#req_r2 = requests.request(method="post", url="https://www.baidu.com")

req_get = requests.request("GET", "https://www.baidu.com")
req_post = requests.request("POST", "https://www.baidu.com")

print("get:", get_r.status_code)
print("post:", post_r.status_code)
# print("method_get:", req_r1.status_code)
# print("method_post:", req_r2.status_code)
print("method_get:", req_get)
print("method_post:", req_post)