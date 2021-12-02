 #파이썬을 이용한 머신러닝, 딥러닝 실전개발 입문
import requests 

r= requests.get("http://api.aoikujira.com/time/get.php") #데이터 가져오기
#print(r) 
text= r.text #텍스트 형식으로 데이터 추출
print(text)
bin= r.content #바이너리 형식으로 데이터 추출
print(bin)