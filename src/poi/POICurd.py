import sys
import importlib
import math


sys.path.append(sys.path[0] + '/../../')


class POICurd:

    def __init__(self):
        DataBase = importlib.import_module('util.DataBase').DataBase
        POIEntity = importlib.import_module('src.poi.POIEntity').POIEntity
        Urllib3Request = importlib.import_module(
            'util.Urllib3Request').Urllib3Request

        self.urlConfig = importlib.import_module('config.urlConfig')

        self.dataBase = DataBase({
            'schema': 'bmapdata',
            'tableName': 'poi'
        })

        self.urllib3Request = Urllib3Request()

        self.POIEntity = POIEntity

    def requestPoiData(self, param):
        results = []
        urllib3Request = self.urllib3Request
        urlConfig = self.urlConfig
        data = urllib3Request.urllib3Get(urlConfig.urlDict['POISearch'], param)
        for result in data["results"]:
            poiEntity = self.POIEntity(result)
            results.append(poiEntity)
        data["results"] = results
        return data

    def insertPoiData(self, datas):
        db = self.dataBase
        insertValues = []
        updateValues = []
        for data in datas:
            res = db.query(
                """select uid from bmapdata.poi where uid=%s""", [data.uid])
            # 已有值做更新操作，否则插入
            if data.uid is None:
                continue
            if res is None:
                insertValues.append((data.uid, data.name, data.address, data.province, data.city, data.area,
                                     data.street_id, data.tag, data.type, data.detail_url, data.telephone, data.lng, data.lat))
            else:
                updateValues.append((data.name, data.address, data.province, data.city, data.area,
                                     data.street_id, data.tag, data.type, data.detail_url, data.telephone, data.lng, data.lat, data.uid))

        if len(updateValues) > 0:
            db.update(
                """update bmapdata.poi set name=%s,address=%s,province=%s,city=%s,area=%s,street_id=%s,tag=%s,type=%s,detail_url=%s,telephone=%s,lng=%s,lat=%s where uid=%s""",
                updateValues)
        if len(insertValues) > 0:
            db.insert(
                """insert into bmapdata.poi values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", insertValues)

