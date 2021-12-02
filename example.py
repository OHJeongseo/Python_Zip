import random

 #p41 1~ 10까지의 합 출력
sum= 0
for i in range(1, 10+1): #+1을 작성하지않으면 9까지의 범위이기때문에 결과는 45가 된다
    sum+= i
print('합계:',sum)


 #p44 2단~ 9단까지 출력
for i in range(2, 10):
    print('[',i,'단]')
    for j in range(1, 10):
        print(i,'*',j, '=', i*j)
    print()


 #p75 문자열서 무작위로 5개 문자를 추출하여 새로운 변수'pw'에 하나씩 병합
pw= str() #문자열 생성
chars= '한글우수'
for i in range(5):
    pw= pw+random.choice(chars) #무작위 문자병합
print(pw)


 #p83 'animal'리스트에 새가 저장되어 있는 위치(인덱스만) 저장하는 리스트'bird_pos'를 생성
bird_pos= []
animal= ['새', '코끼리', '강아지', '새', '강아지', '새']
for i, an in enumerate(animal): #리스트에 저장된 모든 항목을 순서대로 일련의 번호를 부여할수있다, 반환값은 2개(일련번호(인덱스),원소값)
    print('i :', i)
    print('animal :', an)
    if(an=='새'):
        bird_pos.append(i)
print(bird_pos)


 #p84 'mylist'에서 짝수만 출력
mylist= [3,5,4,9,2,8,2,1]
newlist= [i for i in mylist if (i%2)==0] #리스트 함축
print(newlist)
 #p85 19세이상인 사람만 추출하여 리스트 adult에 저장
people= [31, 53, 41, 19, 15, 18, 21, 13]
adult= [i for i in people if (i>=19)] #리스트 함축
print(adult)

 #p90 항목이 2인것만 추출하여 newlist 생성
mylist= [[1,2],[3,4,5],[6,7]]
newlist= [x for x in mylist if len(x)==2] #len을 사용하여 원소의 길이를 확인한다
print(newlist)


  