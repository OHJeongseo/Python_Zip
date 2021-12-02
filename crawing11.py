import requests
from bs4 import BeautifulSoup
import re
 
 #접근 허용하지않을 경우 
header = {'User-Agent': 'Mozilla/5.0'}

#멜론 주간차트 사이트에서 데이터 추출(이 사이트의 경우 접근을 허용하지않기 때문에 위의 접근허용 header를 정의)
req = requests.get('https://www.melon.com/chart/week/index.htm', headers= header)
html= req.text
soup= BeautifulSoup(html, 'html.parser')

#원하는 데이터(멜론 차트순위, 곡이름, 가수이름, 앨범)를 추출하여 리스트에 넣는다
tbody= soup.select_one('#frm > div > table > tbody')      
trs= tbody.select('tr#lst50')
datas= []
for tr in trs:
  rank= tr.select_one('span.rank').get_text() #순위
  name= tr.select_one('div.rank01').get_text() #곡 이름
  name= re.sub('\n', '', tr.select_one('div.rank01').get_text()) 
  name= name.replace(',','')
  singer= tr.select_one('div.rank02 >a').get_text() #가수 이름
  album= tr.select_one('div.rank03 >a').get_text() #앨범
  datas.append([rank,name,singer,album])
print(datas) #리스트 변수 출력 결과 실행

## 리스트의 데이터를 csv파일로 내보낸다
# with open('melon.csv','w') as file:
#     file.write('순위, 곡명, 가수, 앨범\n')
#     for item in datas:
#         row= ','.join(item)
#         file.write(row+'\n')



  
