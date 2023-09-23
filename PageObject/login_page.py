# 登陆页面操作类
from Commen.base import Base
from time import sleep


class YmwLogin(Base):
    def login(self, by_fix):
        self.get_url('http://192.168.44.129:8080/EasyBuy/Login?action=toLogin')
        self.sen_dkeys((by_fix.ID, 'loginName'), 'admin')
        self.sen_dkeys((by_fix.ID, 'password'), '123456')
        self.cl_ick((by_fix.CLASS_NAME, 'log_btn'))
        sleep(1)
