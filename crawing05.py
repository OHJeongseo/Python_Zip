import requests
from bs4 import BeautifulSoup
import re

#로또 공식 사이트에서 데이터를 추출
res= requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin') 
soup= BeautifulSoup(res.content, 'html.parser') #파일형식

#원하는 데이터(로또 당첨번호)를 추출하여 출력한다, 2개(select, find_all)의 방법으로 사용
#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p-> 사이트에서 제공하는 태그(선택자) 경로(copy)
#p사용시 문자이기 때문에 'end='가 인식되지않는다, 하위 경로를 사용한다
rotto= soup.select('div > div.num.win > p > span') 
#print(rotto)
for i in rotto:
    num= i.get_text() 
    print(num, end='\t')

print()

ballNum= soup.find_all('span', class_='ball_645')
#print(ballNum)
for i in ballNum:
    num= i.get_text() 
    print(num, end='\t')


    

