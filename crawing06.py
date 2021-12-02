import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

#네이버증권 사이트에서 데이터를 추출
res= requests.get('https://finance.naver.com/') 
soup= BeautifulSoup(res.content, 'html.parser')

# 원하는 데이터(인기검색종목 추출)를 추출하여 결과(종목명(회사),현재가격, 등락)를 출력
#container > div.aside > div > div.aside_area.aside_popular > table > tbody
company= soup.select_one('div.aside_area.aside_popular > table > tbody')
trs= company.select('tr')

datas= []
for tr in trs:
    name= tr.select_one('th >a').get_text() #회사명
    curr_price= tr.select_one('td').get_text() #현재 가격
    ch_direction= tr['class'][0] #상승/하락
    ch_price= tr.select_one('td >span').get_text().strip() #상승또는 하락 가격
    datas.append([name, curr_price, ch_direction, ch_price]) 
print(datas) 

#csv파일에서 사용자가 sheet를 만들어서 sheet에 데이터를 출력한다
write_wb= Workbook()
write_ws= write_wb.create_sheet('결과') #sheet 생성
for data in datas:
    write_ws.append(data)  #생성한 sheet에 데이터를 가져온다
write_wb.save(r'textsave.xlsx') #파일 저장