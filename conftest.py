from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


# 定义夹具返回浏览器驱动对象
@pytest.fixture(scope='session')   # 作用域是会话级别，每启动一次用例执行，所有的夹具只会调用一次
def driver_fix():
    global dr
    dr = webdriver.Chrome()
    dr.maximize_window()
    yield dr
    print('这是后置操作')


# 夹具返回By定位方法
@pytest.fixture(scope='session')
def by_fix():
    # yield By
    return By   # 这种格式也可以


# 失败截图的钩子函数
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    req = outcome.get_result()
    if req.when == 'call' and req.outcome == 'failed':
        img = dr.get_screenshot_as_png()
        allure.attach(img, '失败截图', allure.attachment_type.PNG)
