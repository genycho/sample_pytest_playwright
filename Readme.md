## pytest&playwright 샘플/템플릿 프로젝트
1년 반 전쯤 pytest와 playwright(어쩌면 cypress일지도) 조합으로 이전에 쓰던 selenium을 대체해 보려고 했다. 

자동화 코드를 javascript로 작성하는 건 싫어해서. 

그때 당시에는 playwright가 자동으로(?)해주는게 많아서인지 계속 문제가 꼬리에 꼬리를 물고 발생했다. 
(그냥 python으로 작성할 땐 괜찮았음) 

python으로 작성하는 경우 참조할 내용도 잘 검색되지 않아 못써먹겠다 싶어 드랍했었다. 
이제 1년 넘게 지난 지금. 많은 사람들이 playwright를 얘기하고 있고, 
검색해보면 아예 pytest-playwright 플러그인, 라이브러리들이 검색되는 거 보면 상황이 많이 나아진 것 같다. 

그래서 재시도. 

Playwright 사이트의 글 
https://playwright.dev/python/docs/test-runners

python 플러그인(?) 
https://pypi.org/project/pytest-playwright/

따라하기 
https://helloahram.tistory.com/222

## Requirements
pip install -r requirements.txt

- pytest>=8.2.2
- requests>=2.25.1
- pytest-html>=3.1.1
- unittest-xml-reporting>=3.0.4
- pytest-cov>=4.0.0

- pytest-playwright

playwright install

## 
------------------------------
> 폴더 구조:   

### src
- 비어있음

### tests
- common

- saucedemo

------------------------------
> 샘플 구성:   
- 참고 사이트 : https://helloahram.tistory.com/222 
- 샘플 타겟 사이트 : https://www.saucedemo.com/ 
- 레코드 명령어 : npx playwright codegen
- 웹UI 자동화 요구사항
    1) 타겟 url을 외부에서 전달받게 - 디폴트 값 https://www.saucedemo.com
    2) 수행할 브라우저를 외부에서 전달받아 실행하게 
    3) UI 엘리먼트를별도 분리하여 정의 
- 샘플 E2E 테스트 시나리오
    1) (로그인 페이지)아이디/비밀번호 넣고 로그인 
    2) (그 다음 페이지)나중에 생각 
    a) 별도 TC로 분리하여 다양한 로그인 실패 상황 parameterize 
