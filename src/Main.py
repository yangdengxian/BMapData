import importlib
import math
import sys
import time

sys.path.append(sys.path[0] + '/../')

# 主方法


class Main:
    def __init__(self):
        POICurd = importlib.import_module('poi.POICurd').POICurd

        self.poiTypeThreadsList = ['美食', '酒店', '购物', '生活服务',
                                   '丽人', '旅游景点', '休闲娱乐', '运动健身',
                                   '教育培训', '文化传媒', '医疗', '汽车服务',
                                   '交通设施', '金融', '房地产', '公司企业',
                                   '政府机构', '出入口', '自然地物']
        self.poiCurd = POICurd()

    def execute(self, threadName, delay):
        time.sleep(delay)
        poiCurd = self.poiCurd
        pageSize = 20
        queryParam = {
            'query': threadName,
            'region': '北京',
            'output': 'json',
            'scope': 2,
            'page_num': 0,
            'page_size': pageSize,
            'ak': poiCurd.urlConfig.urlDict['AK']
        }

        content = poiCurd.requestPoiData(queryParam)
        results = content["results"]

        for i in range(1, math.ceil(content["total"]/pageSize)):
            queryParam["page_num"] = i
            results.extend(poiCurd.requestPoiData(queryParam)["results"])

        poiCurd.insertPoiData(results)
        print("%s: %s" % (threadName, time.ctime(time.time())))


if __name__ == "__main__":
    # 多线程
    Thread = importlib.import_module('util.Thread').Thread
    main = Main()
    for value in main.poiTypeThreadsList:
        thread = Thread(main.poiTypeThreadsList.index(
            value), value, 0, main.execute)
        thread.start()
