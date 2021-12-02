import urllib.request
from bs4 import BeautifulSoup
import pandas as pd   
 
#원하는 데이터(할리스매장정보)를 추출하는 함수를 정의하여 결과를 출력
def hollys_store(result):
    for page in range(1,10): #가져올 매장정보에 대한 페이지범위를 설정(1~ 10page)
        Hollys_url= 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
        #url(Hollys_url)에서 가져온 데이터를 html변수에 저장한다
        html= urllib.request.urlopen(Hollys_url) 
        #파싱(html분석)
        soupHollys= BeautifulSoup(html, 'html.parser')
        
        #원하는 데이터(매장명, 시도, 주소, 전화번호)를 추출
        tag_tbody= soupHollys.find('tbody') #원하는 데이터를 감싸고 있는 태그를 1개요소로 가져온다
        for store in tag_tbody.find_all('tr'): #사용하고자 하는 데이터를 가지고 있는 태그를 가져온다
            if len(store) <= 3:
                break
            store_td= store.find_all('td') #실제데이터를 가지고 있는 태그를 가져와서
            store_name= store_td[1].string #매장명 데이터 추출-> 문자만 사용
            store_sido= store_td[0].string #지역 데이터 추출-> 문자만 사용
            store_address= store_td[3].string #주소 데이터 추출-> 문자만 사용
            store_phone= store_td[5].string #전화번호 데이터 추출-> 문자만 사용
            result.append([store_name]+[store_sido]+[store_address]+[store_phone]) #가져온 데이터를 리스트형태로 저장
    
    return 

result= [] #원하는데이터를 저장할 리스트형 변수 선언
print('Hollys store crawling >>>>>>>>>>>>>>>>')
hollys_store(result)  #원하는 데이터를 추출하는 함수에 저장할 리스트 변수를 매개변수로 전달

#추출한 결과값(result)을 2차원표 형식 가공하여 칼럼이름 설정하여 저장
hollys_tbl= pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone-number')) 
print(hollys_tbl) #결과 출력
del result[:] #리스트의 모든항목 삭제

