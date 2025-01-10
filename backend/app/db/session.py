import pymysql

from app.core.config import settings


def get_db_connection():
    # 获取数据库连接
    connection = pymysql.connect(
        host=settings.mysql_host,  # 数据库主机
        port=settings.mysql_port,  # 数据库端口
        user=settings.mysql_user,  # 数据库用户名
        password=settings.mysql_password,  # 数据库密码
        db=settings.mysql_db,  # 数据库名称
    )
    return connection  # 返回数据库连接
