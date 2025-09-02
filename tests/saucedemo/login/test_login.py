#-*- coding: utf-8 -*-
import pytest
import time
from playwright.sync_api import Page, expect
import saucedemo_elements as elements
import saucedemo_testdata as testdata
import playwright

@pytest.mark.parametrize("test_id, test_pw", [(testdata.TEST_USERID01,testdata.TEST_USERPW), (testdata.TEST_USERID03,testdata.TEST_USERPW)])
def test_login_success(page, get_target_url, test_id, test_pw):   
    """ 정상 로그인 """
    playwright.screenshotOnFailure = True
    page.goto(f"{get_target_url}")
    assert page.title() == "Swag Labs"
    expect(page.locator(elements.LOCATOR_LOGIN_PAGETITLE)).to_contain_text('Swag Labs')
    ## 아이디/비밀번호 입력
    page.locator(elements.LOCATOR_LOGIN_IDTXT).fill(test_id)
    page.locator(elements.LOCATOR_LOGIN_PWTXT).fill(test_pw)
    page.locator(elements.LOCATOR_LOGIN_LOGINBTN).click()
    time.sleep(testdata.WAITSECONDS_FOR_COMMON)
    ## 메인페이지 
    page.locator(elements.LOCATOR_MAIN_FIRSTITEMTXT).wait_for(state="visible", timeout=60000)
    expect(page.locator(elements.LOCATOR_MAIN_PAGETITLE)).to_contain_text('Swag Labs')
    time.sleep(testdata.WAITSECONDS_FOR_COMMON)

@pytest.mark.parametrize("test_id, test_pw", [('wrong_iddd',testdata.TEST_USERPW), (testdata.TEST_USERID01,'wrong_pw123@')])
def test_login_fail(page, get_target_url, test_id, test_pw):   
    """ 로그인 실패 """
    playwright.screenshotOnFailure = True
    page.goto(f"{get_target_url}")
    assert page.title() == "Swag Labs"
    expect(page.locator(elements.LOCATOR_LOGIN_PAGETITLE)).to_contain_text('Swag Labs')
    ## 아이디/비밀번호 입력
    page.locator(elements.LOCATOR_LOGIN_IDTXT).fill(test_id)
    page.locator(elements.LOCATOR_LOGIN_PWTXT).fill(test_pw)
    page.locator(elements.LOCATOR_LOGIN_LOGINBTN).click()
    time.sleep(testdata.WAITSECONDS_FOR_COMMON)
    ## 메인페이지 
    expect(page.locator(elements.LOCATOR_LOGIN_MSG)).to_contain_text("Username and password do not match any user in this service")
    time.sleep(testdata.WAITSECONDS_FOR_COMMON)
    
def test_login_blockeduser(page, get_target_url):   
    """ block된 사용자로 로그인 시도  """
    playwright.screenshotOnFailure = True
    page.goto(f"{get_target_url}")
    assert page.title() == "Swag Labs"
    expect(page.locator(elements.LOCATOR_LOGIN_PAGETITLE)).to_contain_text('Swag Labs')
    ## 아이디/비밀번호 입력
    page.locator(elements.LOCATOR_LOGIN_IDTXT).fill(testdata.TEST_USERID02)
    page.locator(elements.LOCATOR_LOGIN_PWTXT).fill(testdata.TEST_USERPW)
    page.locator(elements.LOCATOR_LOGIN_LOGINBTN).click()
    time.sleep(testdata.WAITSECONDS_FOR_COMMON)
    ## 메인페이지 
    expect(page.locator(elements.LOCATOR_LOGIN_MSG)).to_contain_text("Sorry, this user has been locked out.")
    time.sleep(testdata.WAITSECONDS_FOR_COMMON)