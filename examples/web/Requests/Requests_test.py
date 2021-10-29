import requests 
r = requests.get('https://api.github.com/events')
print(r)
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
r = requests.put('https://httpbin.org/put', data = {'key':'value'})  
r = requests.delete('https://httpbin.org/delete')  
r = requests.head('https://httpbin.org/get')  
r = requests.options('https://httpbin.org/get')

payload = {'key1': 'value1', 'key2': 'value2'}  
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url) 

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}  
r = requests.get('https://httpbin.org/get', params=payload)  
print(r.url)

r = requests.get('https://api.github.com/events')
print(r.text)

print(r.encoding)

r.encoding = 'ISO-8859-1'
print(r.text)

print (r.content)

from PIL import Image  
from io import BytesIO  
r = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Requests_Python_Logo.png/330px-Requests_Python_Logo.png')
i = Image.open(BytesIO(r.content))
i.show()

r = requests.get('https://api.github.com/events')
print(r.json())
print(r.raise_for_status())
print(r.status_code)

r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
print(r.raw.read(10))

# filename = "test.txt"
# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)

url = 'https://api.github.com/some/endpoint'  
headers = {'user-agent': 'my-app/0.0.1'}  
r = requests.get(url, headers=headers)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)
print(r1.text == r2.text)

import json
url = 'https://api.github.com/some/endpoint'  
payload = {'some': 'data'}  
r = requests.post(url, data=json.dumps(payload))  

url = 'https://api.github.com/some/endpoint'  
payload = {'some': 'data'}  
r = requests.post(url, json=payload)

# url = 'https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests'
# files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
# print(r.text)

# url = 'https://httpbin.org/post'
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# r = requests.post(url, files=files)
# print(r.text)

url = 'https://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
print(r.text)

r = requests.get('https://httpbin.org/get')
print(r.status_code)
print(r.status_code == requests.codes.ok)

# bad_r = requests.get('https://httpbin.org/status/404')
# print(bad_r.status_code)
# print(bad_r.raise_for_status())

print(r.headers)

print(r.headers['Content-Type'])
print(r.headers.get('content-type'))

# url = 'https://example.com/some/cookie/setting/url'
# r = requests.get(url)
# r.cookies['example_cookie_name']

# url = 'https://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)

# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'https://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# print(r.text)

r = requests.get('http://github.com/')
print(r.url)
print(r.status_code)
print(r.history)

r = requests.get('http://github.com/', allow_redirects=False)
print(r.status_code)
print(r.history)

