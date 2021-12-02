import requests
from bs4 import BeautifulSoup

#다음 영화랭킹(예매순위) 사이트에서 데이터 추출하여 텍스트형식으로 읽어서 파싱(html분석)
req= requests.get("https://movie.daum.net/ranking/reservation") 
html= req.text
soup= BeautifulSoup(html, 'html.parser')

#원하는 데이터(영화 이름, 평점, 예약률) 추출하여 결과를 출력
ols= soup.find('ol', 'list_movieranking')
rankcont= ols.find_all('div', 'thumb_cont')
#print(rankcont)

for i in rankcont:
    moviename= i.find('a','link_txt').get_text() #제목
    moviegrade= i.find('span','txt_grade').get_text() #평점
    movieReser= i.find('span', 'txt_num').get_text() #예매률
    #개봉일 데이터추출(문자+숫자)
    movieopendate= i.find('span', 'txt_info').get_text() 
    #가져온 데이터에서 숫자만 추출
    moviedate= movieopendate.split('개봉')[1].strip() 

    #결과 출력
    print(moviename)
    print('평점 :',moviegrade)
    print('예매률 :', movieReser)
    print('개봉일 :',moviedate)
    print()
    
