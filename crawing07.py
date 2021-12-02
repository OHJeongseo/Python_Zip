import requests
from bs4 import BeautifulSoup

#데이터(종목번호)를 설정하여 데이터에 대한 정보(종목에 대한 현재가격)를 추출하여 결과를 출력한다
codes= ['000270', '277810'] #추출할 코드(종목:기아,레인보우로보틱스)를 리스트로 저장
prices= [] #추출한 데이터를 저장할 리스트를 선언

#코드(종목)의 가격만 추출
for code in codes:
    #네이버 증권사이트에서 코드(해당종목)에 대한 정보를 추출
    url= 'https://finance.naver.com/item/main.naver?code='+code
    res= requests.get(url)

    #코드(해당종목)에서 원하는데이터(해당 종목 현재가격)을 추출하여 리스트에 저장
    soup= BeautifulSoup(res.content, 'html.parser')
    today= soup.select_one('p.no_today') #하나의 요소를 추출하고
    #print(price) 
    price= today.select_one('.blind') #하나의 요소안에 있는 '.blind'클래스(요소의 문자->가격)를 추출한다
    prices.append(price.get_text())

#결과를 출력
print(prices) #저장한 리스트를 출력하여 결과를 보여준다


