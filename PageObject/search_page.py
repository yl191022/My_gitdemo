# 搜索页面操作类
from Commen.base import Base
from selenium.webdriver.common.keys import Keys
from time import sleep


class YmwSearch(Base):
    def search(self, by_fix, product_name):
        self.get_url('http://192.168.44.129:8080/EasyBuy/Home?action=index')
        sleep(1)
        self.sen_dkeys((by_fix.NAME, 'keyWord'), product_name)
        self.sen_dkeys((by_fix.NAME, 'keyWord'), Keys.ENTER)
        sleep(1)
        self.more_element((by_fix.LINK_TEXT, '加入购物车'), 0)
        sleep(1)
        return self.get_txt((by_fix.ID, 'showMessage'))
