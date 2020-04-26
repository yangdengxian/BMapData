import sys
import importlib
sys.path.append(sys.path[0] + '/../')

print(sys.path)

Urllib3Request = importlib.import_module('util.Urllib3Request').Urllib3Request
urlConfig = importlib.import_module('config.urlConfig')

urllib3Request = Urllib3Request()
result = urllib3Request.urllib3Get(urlConfig.urlDict['POISearch'], {
    'query': 'ATM机',
    'region': '北京',
    'output': 'json',
    'ak': urlConfig.urlDict['AK']
})
print(result)
