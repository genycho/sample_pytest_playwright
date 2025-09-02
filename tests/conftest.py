#-*- coding: utf-8 -*-
import pytest
import os
from playwright.sync_api import sync_playwright

###### COMMON ######
def pytest_addoption(parser):
    parser.addoption("--saucelabdemo_url", action="store", default="https://www.saucedemo.com", help="By default: https://www.saucedemo.com")
    parser.addoption("--target_url", action="store", default="https://www.saucedemo.com", help="테스트 대상 웹 애플리케이션의 Base URL")
    parser.addoption("--target_browser", action="store", default="chromium", choices=["chromium", "firefox", "webkit"], help="테스트 브라우저 선택")
    parser.addoption("--headless_bool", action="store", default=False, help="By default: False")
    
@pytest.fixture(scope='session')
def get_demourl_baseurl(pytestconfig):
   return pytestconfig.getoption("--saucelabdemo_url")

@pytest.fixture(scope="session")
def get_target_url(pytestconfig):
    return pytestconfig.getoption("--target_url")

@pytest.fixture(scope="session")
def get_target_browser(pytestconfig):
    return pytestconfig.getoption("--target_browser")

@pytest.fixture(scope="session")
def get_headless_bool(pytestconfig):
    return pytestconfig.getoption("--headless_bool")

@pytest.fixture(scope="function")
def page(get_target_browser, get_headless_bool):
    with sync_playwright() as p:
        browser = getattr(p, get_target_browser).launch(headless=get_headless_bool)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()



