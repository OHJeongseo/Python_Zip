import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt #그래프 그리기
import matplotlib as mpl #한글처리
 
 #접근 허용하지않을 경우  
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'}

#네이버 뉴스 홈 사이트
req = requests.get('https://news.naver.com/main/home.naver', headers=header)
html= req.text
soup= BeautifulSoup(html, 'html.parser')

#폰트설정(한글사용)
font_name= mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name() 
mpl.rc('font', family=font_name)

#언론사 추출 가져오기
news= {}
for i in soup.find_all('span', class_='writing'):
  if(news.get(i.string)==None): #언론사별 뉴스 갯수 확인(key-언론사 이름)
    news[i.string]= 1
  else:
    news[i.string]+= 1
print(news)

figure= plt.figure()
axes= figure.add_subplot(111)

axes.pie(news.values(), labels= news.keys(), autopct= '%.1f%%') #autopct 퍼센트(소수점1개까지만)표시
plt.show()


  
