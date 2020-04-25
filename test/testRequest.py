import sys
import importlib
sys.path.append(sys.path[0] + '/../')

print(sys.path)

urllib3Request = importlib.import_module('util.urllib3Request')
urlConfig = importlib.import_module('config.urlConfig')

result = urllib3Request.urllib3Get(urlConfig.urlDict['POISearch'], {
    'query': 'ATM机',
    'region': '北京',
    'output': 'json',
    'ak': urlConfig.urlDict['AK']
})
print(result)
