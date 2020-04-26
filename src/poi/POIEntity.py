
# POI实体类


class POIEntity:
    def __init__(self, result):
        self.uid = result["uid"]
        self.name = result["name"]
        self.address = result["address"]
        self.province = result["province"]
        self.city = result["city"]
        self.area = result["area"]
        self.street_id = result["street_id"] if "street_id" in result else None
        self.tag = result["detail_info"]["tag"] if "detail_info" in result else None
        self.type = result["detail_info"]["type"] if "detail_info" in result else None
        self.detail_url = result["detail_info"]["detail_url"] if "detail_info" in result else None
        self.telephone = result["telephone"] if "telephone" in result else None
        self.lng = result["location"]["lng"]
        self.lat = result["location"]["lat"]
