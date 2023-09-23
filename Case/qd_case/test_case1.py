from time import sleep
import pytest
from Utils.excel_utils import Excel
from selenium.webdriver.common.keys import Keys
import allure
from Utils.log import Log


@allure.epic('易买网添加商品测试用例')
class TestShop:
    @allure.feature('用例一')
    @allure.title('登陆')
    @allure.severity('critical')
    def test_case1(self, driver_fix, by_fix):
        driver_fix.get('http://192.168.44.129:8080/EasyBuy/Login?action=toLogin')
        driver_fix.find_element(by_fix.ID, 'loginName').send_keys('admin')
        driver_fix.find_element(by_fix.ID, 'password').send_keys(123456)
        driver_fix.find_element(by_fix.CLASS_NAME, 'log_btn').click()
        Log().info('success')
        sleep(1)

    @allure.feature('用例二')
    @allure.title('搜索商品添加至购物车')
    @allure.severity('blocker')
    @pytest.mark.parametrize('product_name', Excel.excel_read('/Pytest_framework/Data/testdata'))
    def test_case2(self, driver_fix, by_fix, product_name):
        driver_fix.find_element(by_fix.NAME, 'keyWord').send_keys(product_name)
        driver_fix.find_element(by_fix.NAME, 'keyWord').send_keys(Keys.ENTER)
        sleep(1)
        button = driver_fix.find_elements(by_fix.LINK_TEXT, '加入购物车')
        button[0].click()
        sleep(1)
        add_resout = driver_fix.find_element(by_fix.ID, 'showMessage').text
        try:
            assert add_resout == '操作成功'           # 判断添加购物车是否成功
            driver_fix.find_element(by_fix.XPATH, '//div[@id="MyDiv1"]/div/div[1]/span/img').click()
            Log().info('success')
        except Exception as er:
            Log().info(er)
            driver_fix.find_element(by_fix.XPATH, '//div[@id="MyDiv1"]/div/div[1]/span/img').click()
            raise
