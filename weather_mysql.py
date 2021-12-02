from bs4.element import Comment
import requests
from bs4 import BeautifulSoup
import pymysql

#db 설정
dbURL= "127.0.0.1"
dbPost= 3306
dbUser= "root"
dbPass= "root"

#db 연결
conn= pymysql.connect(host= dbURL, port= dbPost, user= dbUser, passwd= dbPass, db='bigdb', charset='utf8', use_unicode=True) 
#db sql문
insert_weather= "insert into `forecast`(`city`,`tmef`,`wf`,`tmn`,`tmx`) values(%s,%s,%s,%s,%s)"
select_last_date= "select tmef from `forecast` order by tmef desc limit 1"

req= requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
html= req.text
soup= BeautifulSoup(html,'lxml')

cur= conn.cursor()
cur.execute(select_last_date)
conn.commit()
last_date= cur.fetchone()
#print(last_date)

weather= {}
for i in soup.find_all('location'):
    weather[i.find('city').text]=[] 
    for j in i.find_all('data'):
        temp= []
        while last_date is not None: #데이터 여부확인
            if tuple(j.find('tmef').text)> last_date: #last_date 이후의 데이터만 db에 넣음 
                temp.append(j.find('tmef').text) #날짜
                temp.append(j.find('wf').text) #날씨
                temp.append(j.find('tmn').text) #최소기온
                temp.append(j.find('tmx').text) #최고기온
                weather[i.find('city').string].append(temp)
        temp.append(j.find('tmef').text) #날짜
        temp.append(j.find('wf').text) #날씨
        temp.append(j.find('tmn').text) #최소기온
        temp.append(j.find('tmx').text) #최고기온
        weather[i.find('city').string].append(temp)        
# print(weather.keys())
# print(weather['부산'])
print(weather)

 #db에 값을 넣기
for i in weather:
    for j in weather[i]:
        cur= conn.cursor()
        cur.execute(insert_weather,(i,j[0],j[1],j[2],j[3]))
        conn.commit()
