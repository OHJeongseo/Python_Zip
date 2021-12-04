from io import BytesIO
import re
import pandas as pd
from bs4.element import Comment
import requests
from bs4 import BeautifulSoup
import pymysql
import base64


#db 설정
dbURL= "127.0.0.1"
dbPost= 3306
dbUser= "root"
dbPass= "root"

#저장된 데이터 가져오기
df= pd.read_csv('diablo.csv', encoding='cp949') #pandas로 파일읽기
df1= pd.read_csv('diablo01.csv')

#데이터
df01= pd.DataFrame(df)
#이미지 데이터
#df1= pd.read_csv('diablo01.csv')
#print(len(df1))



#db 연결
#conn= pymysql.connect(host= dbURL, port= dbPost, user= dbUser, passwd= dbPass, db='bigdb', charset='utf8', use_unicode=True) 
conn= pymysql.connect(host= dbURL, port= dbPost, user= dbUser, passwd= dbPass, db='diadb', charset='utf8', use_unicode=True) 
#db 테이블 데이터추가 SQL
insert= "insert into `item_dto`(`names`,`options`,`recommends`,`categorys`,`images`) values(%s,%s,%s,%s,%s)"
#insert= "insert into `diablo_item`(`item_img`) values(%s)"
# #select_last_date= "select tmef from `forecast` order by tmef desc limit 1"

#db에 설정한 테이블에 데이터를 추가한다
for i in range(len(df)):
    cur= conn.cursor()
    cur.execute(insert,(df01['0'][i],df01['1'][i],df01['2'][i],df01['3'][i],df1['0'][i]))
    #cur.execute(insert,(df['0'][i]))
    conn.commit()

