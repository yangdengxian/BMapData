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
                # 连接池允许的最大连接数,0和None表示没有限制
                maxconnections=5,
                # 初始化时,连接池至少创建的空闲连接,0表示不创建
                mincached=2,
                # 连接池中空闲的最多连接数,0和None表示没有限制
                maxcached=5,
                # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
                maxshared=3,
                # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
                # False表示不等待然后报错
                blocking=True,
                # 开始会话前执行的命令列表
                setsession=[],
                # ping Mysql服务器检查服务是否可用
                ping=0,
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
        return cur.fetchone()

    def insert(self, sql, datas):
        conn = self.connection
        try:
            cur = self.cursor
            # 执行sql语句
            cur.executemany(
                sql, datas)
            # 提交到数据库执行
            conn.commit()
            print("数据新增成功")
        except Exception as e:
            # 如果发生错误则回滚
            conn.rollback()
            logger.error('数据新增失败:%s' % e)

    def update(self, sql, datas):
        conn = self.connection
        try:
            cur = self.cursor
            # 执行sql语句
            cur.executemany(
                sql, datas)
            # 提交到数据库执行
            conn.commit()
            print("数据更新成功")
        except Exception as e:
            # 如果发生错误则回滚
            conn.rollback()
            logger.error('数据更新失败:%s' % e)

    def delete(self, sql):
        self.transact(sql)

    def transact(self, sql):
        conn = self.connection
        try:
            cur = self.cursor
            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()
