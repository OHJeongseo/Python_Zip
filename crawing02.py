import requests
from bs4 import BeautifulSoup

 #다음 뉴스 IT 사이트에서  데이터를 가져와서
res= requests.get('http://media.daum.net/digital/')
soup= BeautifulSoup(res.content, 'html.parser') #html 분석

#뉴스의 제목만 추출하여 결과를 출력한다 
link_title= soup.find_all('a','link_txt')
#결과를 출력할때 제목의 크기만큼 반복해서 문자열만 추출하고 공백을 제거
for num in range(len(link_title)):
    print(link_title[num].get_text().strip())
