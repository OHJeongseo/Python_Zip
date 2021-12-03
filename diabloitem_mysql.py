import re
import pandas as pd
from bs4.element import Comment
import requests
from bs4 import BeautifulSoup
import pymysql

#db 설정
dbURL= "127.0.0.1"
dbPost= 3306
dbUser= "root"
dbPass= "root"


df= pd.read_csv('diablo.csv', encoding='cp949') #pandas로 파일읽기

df01= pd.DataFrame(df)
#print(df01['0']) 
#print(df01['1'])



#db 연결
conn= pymysql.connect(host= dbURL, port= dbPost, user= dbUser, passwd= dbPass, db='bigdb', charset='utf8', use_unicode=True) 
#db 테이블 데이터추가 SQL
insert= "insert into `diablo_item`(`item_name`,`options`,`recommended_job`,`category`) values(%s,%s,%s,%s)"
#select_last_date= "select tmef from `forecast` order by tmef desc limit 1"

#db 데이터추가
for i in range(len(df01['0'])):
    cur= conn.cursor()
    cur.execute(insert,(df01['0'][i],df01['1'][0],df01['2'][i],df01['3'][i]))
    conn.commit()

