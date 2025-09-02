#-*- coding: utf-8 -*-
"""
- 참고 사이트 : https://helloahram.tistory.com/222 
- 샘플 타겟 사이트 : https://www.saucedemo.com/ 
- 레코드 명령어 : npx playwright codegen
- 웹UI 자동화 요구사항
1) 타겟 url을 외부에서 전달받게 - 디폴트 값 https://www.saucedemo.com
2) 수행할 브라우저를 외부에서 전달받아 실행하게 
3) UI 엘리먼트를별도 분리하여 정의 
- 샘플 E2E 테스트 시나리오
1)(로그인 페이지)아이디/비밀번호 넣고 로그인 
2)(그 다음 페이지)나중에 생각 
1')별도 TC로 분리하여 다양한 로그인 실패 상황 parameterize 
"""
import pytest
import time
from playwright.sync_api import Page, expect
import saucedemo_elements as elements
import saucedemo_testdata as testdata

def test_basicflow_01(page, get_target_url):
    """
    1)로그인 \n
    2)첫번째 아이템 카트 담기 \n
    3)카트에서 아이템 삭제 \n
    4)로그아웃 \n
    """
    page.goto(f"{get_target_url}")
    assert page.title() == "Swag Labs"
    # assert "Swag Labs" in (page.locator(elements.LOCATOR_LOGIN_PAGETITLE)).text_content()
    expect(page.locator(elements.LOCATOR_LOGIN_PAGETITLE)).to_contain_text('Swag Labs')
    ## 아이디/비밀번호 입력
    page.locator(elements.LOCATOR_LOGIN_IDTXT).fill(testdata.TEST_USERID01)
    page.locator(elements.LOCATOR_LOGIN_PWTXT).fill(testdata.TEST_USERPW)
    ## 로그인 버튼 클릭
    page.locator(elements.LOCATOR_LOGIN_LOGINBTN).click()
    time.sleep(5)
    ## 메인페이지 
    # assert "Swag Labs" == (page.locator(elements.LOCATOR_MAIN_PAGETITLE)).text_content()
    time.sleep(2)
    page.locator(elements.LOCATOR_MAIN_FIRSTITEMTXT).wait_for(state="visible", timeout=60000)
    expect(page.locator(elements.LOCATOR_MAIN_PAGETITLE)).to_contain_text('Swag Labs')
    # assert 'Sauce Labs Backpack' == (page.locator(elements.LOCATOR_MAIN_FIRSTITEMTXT)).text_content()
    expect(page.locator(elements.LOCATOR_MAIN_FIRSTITEMTXT)).to_contain_text('Sauce Labs Backpack')
    page.locator(elements.LOCATOR_MAIN_FIRSTITEM_ADDTOCARTBTN).click()
    # assert '1' == (page.locator(elements.LOCATOR_MAIN_CARTTXT)).text_content()
    expect(page.locator(elements.LOCATOR_MAIN_CARTTXT)).to_contain_text('1')

    time.sleep(2)
    page.locator(elements.LOCATOR_MAIN_FIRSTITEM_REMOVECARTBTN).click()
    # assert '' == (page.locator(elements.LOCATOR_MAIN_CARTTXT)).text_content()
    expect(page.locator(elements.LOCATOR_MAIN_CARTTXT)).to_have_text('')

    ## 공통
    page.get_by_role("button", name=elements.ROLE_COMMON_OPENSIDEBTN).click()
    page.locator(elements.LOCATOR_COMMON_LOGOUTBTN).click()
    # assert "Swag Labs" == (page.locator(elements.LOCATOR_LOGIN_PAGETITLE)).text_content()
    time.sleep(10)
    