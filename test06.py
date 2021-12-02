import re, codecs

f= codecs.open('friends101.txt', 'r', encoding='utf-8') #파일을 읽기모드로 가져온다  
script101= f.read() #파일을 읽어서 변수에 담는다

print(script101[:100]) #[:]슬라이싱-> 원하는 범위를 설정할수있다

 #'+' 최소 한 번 이상 반복
Line= re.findall(r'Monica:.+',script101) #findall->모든 패턴를 찾아 리스트로 반환 #r->정규표현식 사용할때 작성한다
print(Line[:3])
print(type(Line))

char= re.compile(r'[A-Z][a-z]+:') # 정규표현식을 컴파일하여 변수에 저장한다
print(re.findall(char, script101)) #저장한 변수(패턴)를 사용하여 매칭되는 모든결과를 리스트형태로 변환하여 출력한다
a= [1,2,3,4,5,2,2]

#집합(set) 중복되지않고 정렬되지않는, {}를 사용 ,로 구분되며 키(key)만 있고 값은 없는 형식 
print(set(a)) 
print(set(re.findall(char, script101)))
y= set(re.findall(char, script101))
print(type(y))
z= list(y)
character= []

for i in z:
    character +=[i[:-1]] # ':'을 제거(슬라이싱을 사용하여 마지막부분을 제외)하고 리스트로 담는다

print(character)

ch= 'Scene:'
ch= re.sub(':', '', ch) # 문자열에 맞는 패턴을 2번째 인자(교체할 문자열)로 교체한다-> : 사용하지 않는다
print(ch)

# f= open('moni.txt','w', encoding='utf-8') #파일을 쓰기모드로 가져온다
# monica= ''
# for i in Line:
#     monica +=i
# f.write(monica)
# f.close

txt= re.findall(r'\([A-Za-z].+[a-z|\.]\)',script101)[:6] # [선택적인] # .+
print(txt)
print(type(txt))

 #
a= '제 이메일 주소는 greate@naver.com   오늘은 today@naver.com 내일은 apple@gmail.com  life@abc.co.kr 라는 메일을 사용합니다'
a1= re.findall(r'[a-z]+@[a-z.]+',a) #이메일주소만 가져오기 
print(a1)

words= ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
 #a로 시작되는 단어만 가져오기
for i in words: 
    m= re.search(r'a[a-z]+',i) # 패턴과 일치만 한다면 문자열의 시작과는 상관없이 전부 찾는다
    if m:
        print(m.group())
print()
for i in words:
    #m= re.match(r'a[a-z]+',i) # 문자열의 처음부터 시작해서 작성한 패턴이 일치하는지 확인
    m= re.match(r'a\D+', i) # \d(숫자[0-9]), \D(숫자가 아닌[^0-9])
    if m:
        print(m.group()) # 매치된 문자열 출력(m에 담겨진 값)

        