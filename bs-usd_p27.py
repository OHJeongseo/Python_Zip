#파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
from bs4 import BeautifulSoup #파이썬 스크레이핑 라이브러리(html,xml에 있는 원하는 정보 추출)
import urllib.request as req #url라이브러리, 웹사이트에 있는 데이터를 추출할때 사용한다

#네이버 금융에서 환율 정보추출
url= "https://finance.naver.com/marketindex/"
res= req.urlopen(url)

#원/달러 환율, 등락(up/down)가져와서 문자만추출하고 결과를 출력한다
soup= BeautifulSoup(res, 'html.parser')
price= soup.select_one('div.head_info >span.value').string
updown= soup.select_one('div.head_info >span.blind').string
print("usd/krw= ", price)
print("updown= ", updown)