#-*- coding: utf-8 -*-
import os,sys
import pytest
from playwright.sync_api import sync_playwright
from common.exceptions import GUITestException

# @pytest.fixture(scope="function")
# def page(get_target_browser, get_headless_bool):
#     with sync_playwright() as p:
#         browser = getattr(p, get_target_browser).launch(headless=get_headless_bool)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         context.close()
#         browser.close()
        
