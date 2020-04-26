import sys
import importlib
import math
import POIEntity


sys.path.append(sys.path[0] + '/../../')


class POICurd:

    def __init__(self):
        DataBase = importlib.import_module('util.DataBase').DataBase
        Urllib3Request = importlib.import_module(
            'util.Urllib3Request').Urllib3Request

        self.urlConfig = importlib.import_module('config.urlConfig')

        self.dataBase = DataBase({
            'schema': 'bmapdata',
            'tableName': 'poi'
        })

        self.urllib3Request = Urllib3Request()

    def requestPoiData(self, param):
        results = []
        urllib3Request = self.urllib3Request
        urlConfig = self.urlConfig
        data = urllib3Request.urllib3Get(urlConfig.urlDict['POISearch'], param)
        for result in data["results"]:
            poiEntity = POIEntity.POIEntity(result)
            results.append(poiEntity)
        data["results"] = results
        return data

    def insertPoiData(self, datas):
        db = self.dataBase
        insertValues = []
        updateValues = []
        for data in datas:
            res = db.query(
                """select uid from "bmapdata".poi where uid=%s""", [data.uid])
            # 已有值做更新操作，否则插入
            if res is None:
                insertValues.append((data.uid, data.name, data.address, data.province, data.city, data.area,
                                     data.street_id, data.tag, data.type, data.detail_url, data.telephone, data.lng, data.lat))
            else:
                updateValues.append((data.name, data.address, data.province, data.city, data.area,
                                     data.street_id, data.tag, data.type, data.detail_url, data.telephone, data.lng, data.lat, data.uid))

        if len(updateValues) > 0:
            db.update(
                """update "bmapdata".poi set name=%s,address=%s,province=%s,city=%s,area=%s,street_id=%s,tag=%s,telephone=%s,type=%s,detail_url=%s,lng=%s,lat=%s where uid=%s""",
                updateValues)
        if len(insertValues) > 0:
            db.insert(
                """insert into "bmapdata".poi values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", insertValues)


if __name__ == "__main__":
    poiCurd = POICurd()
    pageSize = 20
    queryParam = {
        'query': '自然地物',
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
