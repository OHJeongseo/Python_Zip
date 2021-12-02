import requests
from bs4 import BeautifulSoup

#네이버 영화랭킹(평점순) 사이트에서 데이터 추출
req= requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20211115") 
 
#데이터를 텍스트형태로 읽어서 파싱(html분석)
html= req.text
soup= BeautifulSoup(html, 'html.parser')

#원하는 데이터(영화 평점순으로 영화 이름, 평점)를 추출
# movieScore= soup.find_all("td","point")
# movieTitle= soup.find_all("div","tit5")
# #print(movieScore)
 #추출한 데이터의 크기만큼 반복하여 문자열만 추출하여 결과를 출력, 2(find_all,select_one+select)가지 방법을 사용
# for i in range(len(movieScore)):
#     score= movieScore[i].get_text().strip() #영화 평점요소 문자만 추출
#     title= movieTitle[i].get_text().strip() #영화 이름요소 문자만 추출
#     print(i+1,"순위",title, score)

tbody= soup.select_one('#old_content > table > tbody')
trs= tbody.select('tr')
for tr in trs:
  name= tr.select_one('div.tit5 >a') #영화 제목을 추출하여 저장하고
  if(name!=None): #추출한 데이터여부확인하여 
      print(name.get_text()) #있는 데이터만 출력

  point= tr.select_one('td.point') #영화 평점를 추출하여 저장하고
  if(point!=None):
      print(point.get_text())
 
