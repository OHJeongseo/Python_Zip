 #파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
from bs4 import BeautifulSoup 
import re #정규표현식 사용

html= """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo</li>
        <li><a href="https://example.com/aaa">aaa</li>
    </ul>
"""

soup= BeautifulSoup(html, "html.parser")
li= soup.find_all(href= re.compile(r"^https://")) #패턴사용, r(문자열 사용)
print(li)
for e in li:
    print(e.attrs['href']) #href만 출력
