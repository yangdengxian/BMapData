# postgresql
db = {
    'dbDriver': {
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': 5432,
        'dbname': 'postgres',
        'application_name': 'bmapdata'
    },

    'poolDB': {
        # 连接池允许的最大连接数,0和None表示没有限制
        'maxconnections': 100,
        # 初始化时,连接池至少创建的空闲连接,0表示不创建
        'mincached': 5,
        # 连接池中空闲的最多连接数,0和None表示没有限制
        'maxcached': 10,
        # 连接池中最多共享的连接数量,0和None表示全部共享
        'maxshared': 10,
        # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
        # False表示不等待然后报错
        'blocking': True,
        # 开始会话前执行的命令列表
        'setsession': [],
        'ping': 0
    }

}
