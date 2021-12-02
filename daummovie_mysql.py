from bs4.element import Comment
import requests
from bs4 import BeautifulSoup
import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

#db 설정
dbURL= "127.0.0.1"
dbPost= 3306
dbUser= "root"
dbPass= "root"

#db 연결
conn= pymysql.connect(host= dbURL, port= dbPost, user= dbUser, passwd= dbPass, db='bigdb', charset='utf8', use_unicode=True) 
#db sql문
insert_movies= "insert into `daummovie`(`moviename`,`moviegrade`,`moviereser`,`movieopendate`) values(%s,%s,%s,%s)"
# select_last_date= "select movieopendate from `daummovie` order by movieopendate desc limit 1"

req= requests.get('https://movie.daum.net/ranking/reservation')
html= req.text
soup= BeautifulSoup(html,'lxml')

#원하는 데이터(영화제목,평점,예매률,개봉일)을 추출하여 db(daummoive Table)에 값을 넣는다
ols= soup.find('ol', 'list_movieranking')
rankcont= ols.find_all('div', 'thumb_cont')

#커서 생성
cur= conn.cursor() 
for i in rankcont:
    moviename= i.find('a','link_txt').get_text() #제목
    moviegrade= i.find('span','txt_grade').get_text().strip() #평점
    movieReser= i.find('span', 'txt_num').get_text().strip() #예매률
    movieopendate= i.find('span', 'txt_info').get_text() #개봉일 
    moviedate= movieopendate.split('개봉')[1].strip() #개봉일에서 숫자만 추출
    #db에 값을 넣는다
    # cur.execute(insert_movies,(moviename,moviegrade,movieReser,moviedate))
    # conn.commit()
    # print(moviename,moviegrade,movieReser,moviedate)


#daummoive Table에서 moviename, moviegrade(평점)
#  높은순으로 moviegrade(평점) 같으면, moviename을 오름차순으로 5개출력
select_date= "select moviename, moviegrade from `daummovie` order by moviegrade desc, moviename asc limit 1, 5"
cur.execute(select_date)
movies= cur.fetchall()
print(movies) #튜플 반환


#평점 분류(9점이상,8점이상,6점이상,6점미만)하여 그래프(pie)로 그리기

select_grade= 'select moviegrade from `daummovie`'
cur.execute(select_grade)
grade= cur.fetchall()

movies_grade= {'9점이상':0, '8점이상':0, '6점이상':0, '6점이하':0} 

for movie in grade:
    movie= float(movie[0]) #평점(str)-> (float)으로 변환하여 비교
    print(movie)
    if movie>= 9:
        movies_grade['9점이상']+= 1
    elif movie>=8:
        movies_grade['8점이상']+= 1
    elif movie>=6:
        movies_grade['6점이상']+= 1
    else:
        movies_grade['6점이하']+= 1
print(movies_grade)

#한글처리
font_name= mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name() 
mpl.rc('font', family=font_name)

#평점의 결과를 그래프로 그리기
figure= plt.figure()
axes= figure.add_subplot(111)
axes.pie(movies_grade.values(), labels=movies_grade.keys(), autopct='%.1f%%')
plt.show()