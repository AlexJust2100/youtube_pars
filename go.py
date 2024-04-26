import itertools
from urllib.request import Request, urlopen
import urllib
import urllib.parse
import urllib.request

headers = {
    'Server': 'cloudfare',
    'Vary': 'Accept-Encoding',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

characters = "0123456789abcdefghijklmnopqrstuvwxyzABEFGHIJKNOPQRSTUVWXYZ-_"

combinations = itertools.product(characters, repeat=11)
i = []
for combo in combinations:
    string = ''.join(combo)
    req_ = Request("https://www.youtube.com/watch?v=" + string, headers=headers)
    req = urlopen(req_)
    status = req.status
    if status == 200:
        raw = req.read()
        body = str(raw)
        if 'owner' in body and "b'" not in body[:5]:
            data = {"urls":[srting]}
            data_encoded = urllib.parse.urlencode(data).encode('utf-8')
            request = urllib.request.Request("https://getpantry.cloud/apiv1/pantry/3460f78b-e943-4035-b59a-54e966f8a374/basket/URLs", data=data_encoded, method='POST')
            urllib.request.urlopen(request)

