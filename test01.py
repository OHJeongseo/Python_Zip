print('Hello')
a= 0
print(a)
print(type(a))
b= "Hello World"
print(type(b))
print(b)
c= "\'안녕하세요\'"
print(c)
print(b+c)
print(2*3)
print('2'*3)
print(c*3)
#문자열 인덱스
print(b[0])
print(b[-1])
d= '안녕하세요'
print(d[1:3])
print(d[0:5:2])
print(d[:])
# 리스트(주소, 중복허용)
l= list()
print(l, type(l))
lst= [1,2,3]
print(lst, type(lst))
l= [1,2,3,4,5,6,7,8,9]
print(l[0])
print(len(l))
print(l[len(l)-1]) #리스트 마지막 값 출력
l[0]= 99 #리스트[0] 값 변경
print(l[0])
l[1]= [1,2,3] #리스트안 리스트를 넣기
print(l)
l[2]= '문자' #리스트에 문자열을 넣기
print(l)
l.append(999) #추가
print(l)
l.remove(5) #삭제
print(l)

#튜플(주소, 값 변경안됨 ,중복허용안함)
t= tuple()
print(t, type(t))
t1= (1,2,3)
print(t1, type(t1))
print(t1[0], t1[0:2])
print(t1+t1)
#t1[0]= 5 /t1의 0번째 5로 수정-> 에러발생
#print(t1)

#딕셔너리{key, value} (dict())
d= dict()
print(d, type(d))
d= {
    'a': 1,
    'b': 2,
    'c': 3
}
print(d,type(d))
print(d['a'])
d['c']= 33
print(d)
#print(d['d'])-> 에러발생(키,값이 없음)
d1= d.keys
print("d1 :",d1)
d2= d.items
print("d2 :",d2)
d3= d.values
print("d3 :",d3)

# 조건문
a= 2
if(a==1):
    print(1)
else:
    print('1이 아닙니다')

if(a==1):
    print(1)
elif(a==2):
    print(2)
else:
    print(3)

# 반복문
for i in [1,2,3]:
    print(i)

for i in (1,2,3):
    print(i)

for i in "Hello":
    print(i)

num= 5
while(num > 0):
    print(num)
    num -=1

num= 10
# while문 사용 print(10,9,8,7, --end--)
# while(num > 0):
#     print(num)
#     num -=1
#     if(num==6):
#         print('--end--')
#         break

while(num > 0):
    if(num==6):
        print('--end--')
        break
    print(num, end=' ') # 한줄로 출력
    num -=1

for i in range(10):
    print(i)


 #1~100 까지의 수에서 7의 배수와 합계 출력
sum= 0
for i in range(100):
    if(i%7==0):
        sum +=i
        print(i, end= ' ')
print("\nsum :",sum)


 # * * * \n * * * \n * * *
for i in range(3):
    for j in range(3):
        print('*', end= ' ')
    print()


a= input('숫자 입력') #입력(input)
print(a)
print(type(a)) #문자 타입
a= int(a)
print(type(a)) #int 타입
a= float(a)
print(type(a)) #float 타입
