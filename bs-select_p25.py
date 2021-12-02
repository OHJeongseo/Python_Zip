 #파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
from bs4 import BeautifulSoup  #파이썬 스크레이핑(웹사이트에서 데이터를 추출) 라이브러리 사용

 #분석 대상 html
html= """
    <html><body>
    <div id="meigen">
    <h1>위키북스 도서</h1>
    <ul class="items">
        <li>유니티 게임 이펙트 입문</li>
        <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
        <li>모던 웹사이트 디자인의 정석</li>
    </ul>
    </div>
    </body></html>
"""
 #html 분석
soup= BeautifulSoup(html, 'html.parser')
 #타이틀(h1) 부분을 추출
h1= soup.find('h1').string
  #css선택자 지정하여 원하는 부분을 추출한다
h1_1= soup.select_one('h1').string  #css선택자로 요소 하나를 추출한다
h1_2= soup.select_one('div#meigen >h1').string 
print(h1_2)
 #목록(li) 부분을 추출
li_list= soup.select('div#meigen >ul.items >li') #css선택자로 요소 여러개를 리스트로 추출한다
print(li_list)
for li in li_list: #for문을 사용하여 리스트를 출력
    print(li.string)