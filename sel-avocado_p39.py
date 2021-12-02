 #파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
from bs4 import BeautifulSoup 
fp= open('fruits-vegetables.html', encoding= 'utf-8')
soup= BeautifulSoup(fp, 'html.parser')

 #아보카도 
#print(soup.select_one("li:nth-of-type(5)").string) #아보카도가 나오지 않음, 연근
print(soup.select_one("#ve-list >li:nth-of-type(4)").string)
print(soup.select("#ve-list >li[data-lo='us']")[1].string)
print(soup.select("#ve-list >li.black")[1].string)
#print(soup)
cond= {"data-lo":"us", "class":"black"}
print(soup.find("li",cond).string)
print(soup.find(id="ve-list").find("li",cond).string)