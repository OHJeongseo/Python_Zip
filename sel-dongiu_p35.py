 #파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
from bs4 import BeautifulSoup, StopParsing 
import urllib.request as req

url= "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res= req.urlopen(url)

#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a
##mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li:nth-child(1) > a

soup= BeautifulSoup(res, 'html.parser')
a_list= soup.select("#mw-content-text >div >ul >li a")

for a in a_list:
    name= a.string 
    print("-",name)
