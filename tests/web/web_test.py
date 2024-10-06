import pytest
from time import sleep
from assertpy import assert_that
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.login_page import RegisterPage
from tests.web.pages.login_page import CalculatePage

class TestReg(WebBase):
    
    def test_register(self):
        RegisterPage(self.driver).elements.register.click()
        RegisterPage(self.driver).register_inputs('admin', 'test1234', 'test1234')
        RegisterPage(self.driver).elements.register.click()

        sleep(5)
        
        assert_that(RegisterPage(self.driver).elements.username_logged_in.text).is_equal_to('admin')

class TestWeb(WebBase):

    def test_login(self):
        # Login
        LoginPage(self.driver).login('admin', 'test1234')

        sleep(5)

        assert_that(LoginPage(self.driver).elements.username_logged_in.text).is_equal_to('admin')

class TestCalc(WebBase):

    def test_calc_add_e2e(self):
        # Login
        LoginPage(self.driver).login('admin', 'test1234')

        # 1 + 2
        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyadd.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        sleep(5)

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('3')

    def test_calc_sub_e2e(self):
        # Login
        LoginPage(self.driver).login('admin', 'test1234')

        # 5 - 3
        CalculatePage(self.driver).elements.keyclear.click()
        CalculatePage(self.driver).elements.key5.click()
        CalculatePage(self.driver).elements.keysubtract.click()
        CalculatePage(self.driver).elements.key3.click()
        CalculatePage(self.driver).elements.keyequals.click()

        sleep(5)

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('2')

    def test_calc_div_e2e(self):
        # Login
        LoginPage(self.driver).login('admin', 'test1234')

        # 6 / 2
        CalculatePage(self.driver).elements.keyclear.click()
        CalculatePage(self.driver).elements.key6.click()
        CalculatePage(self.driver).elements.keydivide.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()
        
        sleep(5)

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('3')

    def test_calc_multi_e2e(self):
        # Login
        LoginPage(self.driver).login('admin', 'test1234')

        # 2 x 2
        CalculatePage(self.driver).elements.keyclear.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keymultiply.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        sleep(5)

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('4')

class TestHistory(WebBase):

    def test_calculator_history(self):
        # Login
        LoginPage(self.driver).login('admin', 'test1234')

        # 1 + 2
        CalculatePage(self.driver).elements.keyclear.click()
        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyadd.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()
        CalculatePage(self.driver).elements.keyclear.click()

        # 6 / 2
        CalculatePage(self.driver).elements.key6.click()
        CalculatePage(self.driver).elements.keydivide.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        CalculatePage(self.driver).elements.historybutton.click()

        sleep(5)

        assert_that(CalculatePage(self.driver).elements.historypanel.value).is_equal_to('1+2=3\n6/2=3\n')

