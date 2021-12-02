import requests
from bs4 import BeautifulSoup

#네이버 영화랭킹 사이트에서 데이터를 가져와서
req= requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver") 
#텍스트 형식으로 데이터 추출
html= req.text

#텍스트 형식의 데이터에서 원하는 영화랭킹 1~50위까지 데이터를 추출
soup= BeautifulSoup(html, 'html.parser') #html 분석

#원하는 데이터를 감싸는 태그, 태그의 id또는 class(css선택자)를 통해서 데이터를 추출하여 저장한다 
movie_ranking_list= soup.find_all("div", class_="tit3") #find_all 요소 여러개를 리스트로 추출
for i in range(len(movie_ranking_list)):
    print((i+1),"위 ",movie_ranking_list[i].get_text().strip())