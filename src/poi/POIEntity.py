
# POI实体类


class POIEntity:
    def __init__(self, result):
        self.uid = result["uid"] if "uid" in result else None
        self.name = result["name"] if "name" in result else None
        self.address = result["address"] if "address" in result else None
        self.province = result["province"] if "province" in result else None
        self.city = result["city"] if "city" in result else None
        self.area = result["area"] if "area" in result else None
        self.street_id = result["street_id"] if "street_id" in result else None
        self.tag = result["detail_info"]["tag"] if "detail_info" in result and "tag" in result["detail_info"] else None
        self.type = result["detail_info"]["type"] if "detail_info" in result and "type" in result["detail_info"] else None
        self.detail_url = result["detail_info"]["detail_url"] if "detail_info" in result and "detail_url" in result["detail_info"] else None
        self.telephone = result["telephone"] if "telephone" in result else None
        self.lng = result["location"]["lng"] if "location" in result and "lng" in result["location"] else None
        self.lat = result["location"]["lat"] if "location" in result and "lat" in result["location"] else None
