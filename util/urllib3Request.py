import urllib3
import json

http = urllib3.PoolManager()

# get


def urllib3Get(url, param):
    req = http.request(
        'GET',
        url,
        fields=param)

    if req.status == 200:
        data = json.loads(req.data.decode('utf-8'))
        results = data['results']
        return results
    return []
