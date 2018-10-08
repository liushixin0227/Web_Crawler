import http.cookiejar
import socket
import urllib
from urllib.error import URLError
from urllib.request import Request, HTTPBasicAuthHandler, HTTPCookieProcessor, HTTPPasswordMgrWithDefaultRealm, \
    build_opener, ProxyHandler

from urllib.parse import urlparse

urllib.request.build_opener()
# url请求
from urllib import error

response_get = urllib.request.urlopen('http://www.baidu.com')
print(response_get.closed)
print(response_get.getheader('Server'))

# URL传参
data = bytes(urllib.parse.urlencode({'name': 'liushixin'}), encoding='utf8')
response_post = urllib.request.urlopen('http://httpbin.org/post', data)
print(response_post.read().decode('utf8'))

# 请求超时
try:
    response_timeout = urllib.request.urlopen('http://httpbin.org/post', timeout=0.1)
except error.URLError as e:
    print(type(e.reason), type(socket.timeout))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# 登陆验证
username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handle = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handle)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

# IP代理
proxy_handler = ProxyHandler(
    {
        'http': 'http://127.0.0.1:9743',
        'https': 'https://127.0.0.1:9743'
    }
)

handler = build_opener(proxy_handler)
try:
    response_proxy = opener.open('http://www.baidu.com')
    print(response_proxy.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# 获取Cookie
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response_cookie = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)

# 解析链接
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
