import requests
from bs4 import BeautifulSoup
import re

#다음 뉴스 경제 사이트에서 데이터 추출
res= requests.get('http://media.daum.net/economic/')
soup= BeautifulSoup(res.content, 'html.parser') #바이너리 형식으로 가져와서(res.content), html 분석(파싱)

#원하는 데이터(a href https://v.)를 추출하여 출력
links= soup.select('a[href]')
# print(links)
# print(len(links))
for t in links:
    # a href에서 'https://v.숫자와 문자가 1회이상 반복되는 패턴'을 검색
     #정규식 패턴 설명-> '.' 임의의 문자,  '\w' 숫자와 문자, '+' 1회이상 
    if re.search('https://v.\w+', t['href']): 
        #공백을 제거하고 문자만 추출하여 출력
        print(t.get_text().strip())



    