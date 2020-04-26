import sys
import importlib

sys.path.append(sys.path[0] + '/../')

DataBase = importlib.import_module('util.DataBase').DataBase

if __name__ == '__main__':
    DB = DataBase(match='')
    sql = """insert into "bmapdata".poi ("uid","name") values('123','ydx')"""
    DB.insert(sql)
