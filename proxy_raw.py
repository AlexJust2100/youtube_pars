import re
import json
import requests

headers = {
    'Server': 'cloudfare',
    'Vary': 'Accept-Encoding',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

all_ = []
urls = ["https://www.us-proxy.org/","https://free-proxy-list.net/uk-proxy.html","https://free-proxy-list.net/","https://www.sslproxies.org/"]

for url in urls:
    request = requests.get(url=url, headers=headers)
    response = request.text
    ip_port_match = re.findall(r'<td>(\b(?:\d{1,3}\.){3}\d{1,3}\b)</td>.*?<td>(\b\d+\b)</td>', str(response))
    if ip_port_match:
        ip_port_match = [':'.join(match) for match in ip_port_match]
        all_.extend(ip_port_match)
all_ = list(set(all_))
all_.sort()
data = {'proxy':all_}
response = requests.post("https://getpantry.cloud/apiv1/pantry/3460f78b-e943-4035-b59a-54e966f8a374/basket/RAW", json=data)

