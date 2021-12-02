text= "<title>지금은 문자열 연습입니다.</title>"

print(text[0:7])
 #위치를 찾는 
print(text.find('문')) # 위치를 찾는다 true= 위치 값, false= -1
print(text.find('파')) 
print(text.index('문'))
#print(text.index('파')) # 위치를 찾는다 true= 위치 값, false= error 발생

text1= "    <title>지금은 문자열 연습입니다.</title>    "
text2=";"
 #공백 제거
print(text1.strip()+text2) #공백제거
print(text1.lstrip()+text2) #왼쪽공백 제거
print(text1.rstrip()+text2) #오른쪽공백 제거
print(text.replace('<title>',"<div>")) #변경(기존값, 수정값)
print(text.replace('<title>', ''))

import re #정규표현식(메타문자) 사용
text3= ('111<head>안녕하세요</head>22')
 # <head> </head>안에 있는 문자를 찾는다
body= re.search('<head.*/head>', text3) # '.*'->문자가 한번이상 들어가는 

body= body.group()
print(body)

text4= ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
 # <title> </title>안에 있는 문자를 찾는다
body= re.search('<title.*/title>',text4) #문자열 전체에서 검색하여 처음으로 매치되는 문자열을 찾는다.
body= body.group() #매치된 문자열 출력
print(body)
 # sub(pattern, new_text, text)-> text의 pattern에 맞는부분을 new_text로 대체한다
body= re.sub('<.+?>', '', body) #태그를 제외한 문자만 가져오고, '.+'-> 문자,숫자,빈칸 등이 자유롭게 반복, '?'-> 한번이상 반복
print(body) #가져온 값(가공)을 출력

