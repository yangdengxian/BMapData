import urllib3
import json


class Urllib3Request:
    def __init__(self):
        self.http = urllib3.PoolManager()

    # get
    def urllib3Get(self, url, param):
        req = self.http.request(
            'GET',
            url,
            fields=param)

        if req.status == 200:
            data = json.loads(req.data.decode('utf-8'))
            return data
        return {}

    # POST
    def urllib3Post(self, url, param):
        req = self.http.request(
            'POST',
            url,
            fields=param)

        if req.status == 200:
            data = json.loads(req.data.decode('utf-8'))
            results = data['results']
            return results
        return []
