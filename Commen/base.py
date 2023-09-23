# 封装基类


class Base:
    def __init__(self, driver):         # 初始化浏览器对象
        self.driver = driver

    def loca_tion(self, loc):            # 找单个元素并返回
        return self.driver.find_element(*loc)

    def get_url(self, url):          # 请求url地址
        self.driver.get(url)

    def cl_ick(self, loc):           # 点击
        self.loca_tion(loc).click()

    def sen_dkeys(self, loc, value):        # 输入
        self.loca_tion(loc).send_keys(value)

    def get_txt(self, loc):          # 获取文本值
        txt = self.loca_tion(loc).text
        return txt

    def more_element(self, loc, index_num):     # 获取多个页面元素
        m = self.driver.find_elements(*loc)
        m[index_num].click()
