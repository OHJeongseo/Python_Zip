import requests #웹상에서 값을 가져온다

URL= 'https://www.naver.net'
response= requests.get(URL) #URL의 값을 가져와서
html_data= response.text #텍스트형태로 저장
print(html_data)

print(html_data.find('<h3 class="blind">')) #일치하는 문자열을 출력
print(html_data.find['급'])
print()
