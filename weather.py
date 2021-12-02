import requests
from bs4 import BeautifulSoup
import pandas as pd

respones= requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
soup= BeautifulSoup(respones.text, 'html.parser')

table= soup.find('table', {'class':'table_develop3'})

 #지역, 온도, 습도 추출
# for tr in table.find_all('tr'):
#     tds= tr.find_all('td')
#     if len(tds) > 0:
#         print('tds[0].text(지역)= ', tds[0].text)
#         print('tds[5].text(온도)= ', tds[5].text)
#         print('tds[10].text(습도)= ', tds[10].text)

#     print('='*10)

# #None 이용: a 태그가 없으면 None 출력
# for tr in table.find_all('tr'):
#     tds= tr.find_all('td')
#     for td in tds:
#         if(td.find('a')):
#             print('a 있음')
#         else:
#             print('a 없음')

# a가 있을때만 지역, 온도, 습도 추출
datas= [] #지역,온도,습도를 저장할 리스트 선언
for tr in table.find_all('tr'):
    tds= tr.find_all('td')
    for td in tds:
        if(td.find('a')): #a 태그가 있는지 확인
            print('tds[0].text(지역)= ', tds[0].text)
            print('tds[5].text(온도)= ', tds[5].text)
            print('tds[10].text(습도)= ', tds[10].text)
            datas.append([tds[0].text, tds[5].text, tds[10].text]) #지역,온도,습도 리스트에 추가
    print('='*10)
print(datas) #결과 출력

 #결과를 파일로 저장
# with open('weather.csv', 'w') as file:
#     print('파일 저장')
#     file.write('point, temp, hum \n')
#     for item in datas:
#         print('item= ',item)
#         row= ','.join(item) # ,를 기준으로 합친다
#         file.write(row+'\n')

 #weather.csv파일을 읽어서 출력
# df= pd.read_csv('weather.csv', index_col= 'point', encoding='euc-kr')
# print(df)

