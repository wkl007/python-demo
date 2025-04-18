import requests

r = requests.get('https://www.baidu.com')
print(r.status_code)
print(r.text)

r2 = requests.get('https://www.baidu.com', params={'q': 'python', 'cat': '1001'})
print(r2.url, r2.encoding, r2.content)

r3 = requests.get(
    'https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no')
print(r3.json())

# r4 = requests.get('https://www.douban.com/',
#                   headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r4.text)

r5 = requests.post('https://accounts.douban.com/login',
                   data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
#
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

print(r5.headers)
print(r5.headers['Date'])
print(r5.cookies)

# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
#
# >>> r.cookies['ts']
# 'example_cookie_12345'
# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
#
# >>> cs = {'token': '12345', 'status': 'working'}
# >>> r = requests.get(url, cookies=cs)
# 最后，要指定超时，传入以秒为单位的timeout参数：
#
# >>> r = requests.get(url, timeout=2.5) # 2.5秒后超时
