# 数据库的操作封装
import pymysql


class DB:
    dbcon = None

    @classmethod
    def db_connect(cls, ip, account, pwd, data_base, po_rt=3306):
        try:
            cls.dbcon = pymysql.connect(host=ip, user=account, password=pwd,
                                        database=data_base, port=po_rt)
            return cls.dbcon
        except Exception as err:
            print('连接错误', err)

    @classmethod
    def creat_yb(cls):
        cour = cls.dbcon.cursor()
        return cour

    @classmethod
    def zsg(cls, zsg_sql):
        try:
            zxq = cls.creat_yb()
            zxq.execute(zsg_sql)
            zxq.execute('commit')
        except Exception as err:
            cls.dbcon.rollback()
            print('语法错误', err)

    @classmethod
    def query(cls, query_sql):
        try:
            zxq = cls.creat_yb()
            zxq.execute(query_sql)
            return zxq.fetchall()
        except Exception as err:
            print('语法错误', err)

    @classmethod
    def db_close(cls):
        cls.dbcon.close()

# 调试
# DB.db_connect('192.168.44.128', 'root', 'Woniu123!', 'easybuy')
# DB.zsg('delete from easybuy_user where id=98k')
# print(DB.query('select * from easybuy_user'))
