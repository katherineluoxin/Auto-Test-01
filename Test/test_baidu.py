import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaiDu(unittest.TestCase):
    driver = webdriver.Chrome()

    '''def setUp(self):
        self.driver.implicitly_wait(3)

    # driver.close():关闭当前页面
    # driver.quit():关闭浏览器
    def tearDown(self):
        self.driver.quit()'''

    # 请求网页
    def test_01(self):
        self.driver.get('https://www.baidu.com')
        # 获取当前网页源代码
        print(self.driver.page_source)
        time.sleep(2)

    # 定位元素
    def test_02(self):
        self.driver.get('https://www.baidu.com')
        # find_element_by_id
        self.driver.find_element_by_id('kw').send_keys('python3学习')
        time.sleep(2)
        # 使用clear（）清除输入框中内容
        self.clear()

    # find_element_by#find_element_by_class
    # find_element_by_name
    # find_element_by_tag_name：通过标签名，如div，
    # find_element_by_xpath
    # find_element_by_css_selector

    # 操作表元素
    def test_03(self):
        self.driver.get('https://mail.qq.com/')
        self.driver.find_element_by_id('switcher_plogin').click()

        # CheckBox
        self.driver.find_element_by_id('p_low_login_enable').click()  # 执行两次是取消

        # select下拉框，没有找到合适的链接
        self.driver.get('https://cd.nuomi.com/?lf=2')
        trip = self.driver.find_element_by_class_name('item new-item')
        Select(trip).select_by_index('1')
        Select(trip).select_by_value('audi')
        Select(trip).select_by_visible_text('beauty')
        # 取消选中的所有选项
        trip.deselect_all()

    # 行为链有时候在页面中的操作可能要有很多步，那么这时候可以使用鼠标行为链类ActionChains来完成。
    # 比如现在要求将鼠标移动到某个元素上执行点击事件。
    def test_04(self):
        self.driver.get('https://www.baidu.com')
        input_tag = self.driver.find_element_by_id('kw')
        submit_tag = self.driver.find_element_by_id('su')

        actions = ActionChains(self.driver)
        actions.move_to_element(input_tag)
        actions.send_keys_to_element(input_tag, 'python学习')
        actions.move_to_element(submit_tag)
        actions.perform()  # 执行以上操作

        # 还有更多鼠标操作：
        # click_and_hold(element):点击但不松开鼠标
        # context_click(element):右键点击
        # double_click(element)：双击

    # cookie 操作
    # 获取全部cookie:
    # for cookie in driver_path.get_cookies()
    #   print(cookie)
    # 根据cookie的key获取value
    # value = driver.get_cookie(key)
    # 删除所有cookie:
    # driver.delete_all_cookies()
    #  删除特定的cookie:
    # driver.delete_cookie(key)
    def test_05(self):
        self.driver.get('https://www.baidu.com/')
        print(self.driver.get_cookie('V'))  # v为cookie的name值

    # 页面等待
    # 现在的网页采用ajax技术，需要等待页面加载出来。
    # selenium提供了两种方式：隐式等待和显式等待
    # 1.隐：调用driver.implicitly_wait.那么在获取不可用的元素之前，会先等待10秒时间。
    # 2.显式：显式等待是表名某个条件成立后才执行获取元素等待的操作。也可以在等待的时候指定一个最大的时间。
    # 如果超过这个时间那么就抛出一个异常。显式等待应该使用selenium.webdriver.support.excepted_conditions期待条件
    # 和selenium.webdriver.support.ui.WebDriverWait来配合完成。
    def test_06(self):
        self.driver.get('https://www.baidu.com/')

        self.driver.implicitly_wait(20)
        print(self.driver.get_cookie('V'))

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, 'asdf'))  # 如果没有这个ID=asdf的元素就抛出异常
        )

    # 切换页面：有时候窗口中有多个子tab页面，这时候需要进行切换。
    # selenium提供了一个叫做switch_to_window来进行切换。具体切换到
    # 那个页面，可以从driver.window_handles中找到。
    def test_07(self):
        url_1 = 'https://www.baidu.com'
        url_2 = 'https://www.douban.com'
        self.driver.get(url_1)
        self.driver.execute_script('window.open("%s")' % url_2)  # 打开一个标签页

        # 切换页面：switch_to_window.要先获取窗口句柄。从0开始，
        self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.current_url)  # https://www.douban.com/

    # 代理ip
    def test_08(self):
        ip = '60.177.230.210:18118'
        options = self.webdriver.ChromeOptions()
        options.add_argument('--proxy-server=http://%s' % ip)

        driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)
        self.driver.get('http://httpbin.org/ip')

    # webElement元素：WebDriver类。
    def test_09(self):
        self.driver.get('http://www.baidu.com')

        submit_tag = self.driver.find_element_by_id('su')
        print(type(submit_tag))  # <class 'selenium.webdriver.remote.webelement.WebElement'>
        print(submit_tag.get_attribute('value'))  # 百度一下


if __name__ == "__main__":
    unittest.main(verbosity=2)
