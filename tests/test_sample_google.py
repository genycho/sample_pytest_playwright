#-*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright

### 
# 참고 사이트 : https://helloahram.tistory.com/222 
# 타겟 사이트 : https://www.saucedemo.com/ 
###

# with sync_playwright() as p:

#     # 브라우저(Chromium) 열기
#     # headless=False는 브라우저가 눈에 보이도록 설정
#     browser = p.chromium.launch(headless=False) 
#     page = browser.new_page()
    
#     # 웹 페이지 열기
#     page.goto('https://www.google.com')
    
#     # 페이지 제목 출력
#     print("Page Title: ", page.title())
    
#     # 브라우저 닫기
#     browser.close()