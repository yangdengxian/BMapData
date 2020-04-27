import psycopg2
import importlib
import logger
import sys
from DBUtils.PooledDB import PooledDB
from DBUtils.PersistentDB import PersistentDB, PersistentDBError, NotSupportedError

sys.path.append(sys.path[0] + '/../')

# db class


class DataBase:
    # init
    def __init__(self, match):
        try:
            dbParms = importlib.import_module('config.dataSource').db
            self.poolDB = PooledDB(
                # 指定数据库连接驱动
                creator=psycopg2,
                **dbParms['poolDB'],
                **dbParms['dbDriver']
            )
            self.connection = self.poolDB.connection()
            self.cursor = self.connection.cursor()
            self.schema = match["schema"]
            self.tableName = match["tableName"]
        except Exception as e:
            logger.error('数据库连接错误:%s' % e)
            raise

    # 取单条数据
    def query(self, sql, data):
        cur = self.cursor
        cur.execute(sql, data)
        res = cur.fetchone()
        return res

    def insert(self, sql, datas):
        try:
            self.transact(sql, datas)
            print("数据新增成功")
        except Exception as e:
            logger.error('数据新增失败:%s' % e)

    def update(self, sql, datas):
        try:
            self.transact(sql, datas)
            print("数据更新成功")
        except Exception as e:
            logger.error('数据更新失败:%s' % e)

    def delete(self, sql, datas):
        self.transact(sql, datas)

    def transact(self, sql, datas):
        conn = self.connection
        try:
            cur = self.cursor
            # 执行sql语句
            cur.executemany(
                sql, datas)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()
