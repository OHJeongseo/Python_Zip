import requests
from bs4 import BeautifulSoup
import re

#다음 뉴스 경제 사이트에서 데이터 추출
res= requests.get('http://media.daum.net/economic/') 
soup= BeautifulSoup(res.content, 'html.parser')

#원하는 데이터(댓글 많은 뉴스의 제목 추출)을 추출하여 제목과 댓글수를 리스트로 저장하여 출력한다
#cSub > div > div.section_cate.section_ranking > div.box_cate.box_bestreply > ol > li:nth-child(1) > span.cont_thumb > strong > a
links2= soup.select('div.box_cate.box_bestreply > ol > li')
#print(links2)
datas= []
for t in links2:
    #print(t.select_one('a.link_txt').get_text()) #제목
    #print(t.select_one('span.info_ranking').get_text()) #댓글수
    title= t.select_one('a.link_txt').get_text()
    count= t.select_one('span.info_ranking').get_text()
    datas.append([title,count]) #리스트에 뉴스제목,댓글수 추가

print(datas) #제목과 댓글 같이 출력