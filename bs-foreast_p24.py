 #파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
from bs4 import BeautifulSoup  #파이썬 스크레이핑(웹사이트에서 데이터를 추출) 라이브러리 사용
import urllib.request as req #파이썬 웹사이트에 있는 데이터를 추출하기 위한 라이브러리, 데이터를 다운로드 할수있다

url= "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp" #url 설정
res= req.urlopen(url) #파일에 저장
soup= BeautifulSoup(res, 'html.parser') #html 분석
#print(soup)

title= soup.find('title').string #find()메서드를 사용하여 'title'부분을 추출하여 문자부분만 저장하고 출력
print(title) 

wf= soup.find('wf').string #find()메서드를 사용하여 'wf'부분을 추출하여 문자부분만 저장하고 출력
print(wf)

