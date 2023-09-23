from PageObject.login_page import YmwLogin
from PageObject.search_page import YmwSearch
from Utils.log import Log
import allure
import pytest


@allure.feature('登陆用例')
@allure.title('登陆')
@allure.severity('blocker')
def test_case1(driver_fix, by_fix):
    dl = YmwLogin(driver_fix)
    dl.login(by_fix)
    Log().info('success')


@allure.feature('搜索用例')
@allure.title('搜索')
@allure.severity('blocker')
@pytest.mark.parametrize('product_name', ['电饭锅'])
def test_case2(driver_fix, by_fix, product_name):
    try:
        s = YmwSearch(driver_fix)
        t = s.search(by_fix, product_name)
        assert t == '操作成功'
        Log().info('success')
    except Exception as er:
        Log().exception(er)
        raise
