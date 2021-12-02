 #파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
from bs4 import BeautifulSoup  #파이썬 스크레이핑(웹사이트에서 데이터를 추출) 라이브러리 사용

 #분석하고 싶은 html
html= """
    <html><body>
    <h1>스크레이피이란</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
 #html 분석
soup= BeautifulSoup(html,'html.parser') 
print(soup)

 #원하는 부분을 추출하여 요소의 글자를 출력
h1= soup.html.body.h1
p1= soup.html.body.p
p2= p1.next_sibling.next_sibling
print("h1 =", h1.string) #.string-> 요소의 글자부분을 추출
print("p1= ", p1.string)
print("p2= ", p2.string)

html2= """
    <html><body>
    <h1 id="title">스크레이피이란</h1>
    <p id="body">웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""

soup= BeautifulSoup(html2, 'html.parser')
 #find() 메서드로 원하는 부분(id로 요소를 찾는)을 추출하여 출력하기
title= soup.find(id='title')
print("#title= ", title.string)
body= soup.find(id='body')
print("#body= ", body.string)