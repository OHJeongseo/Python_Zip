nums= [1,1,1,2,2,3,2,3,2,3,3,3,1]

#nums(리스트)의 값에서 같은 숫자가 몇개가 있는지 확인하는 함수
def max_count(nums):
    counts= {} # dict선언-> 키, 값을 사용
    for i in nums:
        if i in counts: #키값이 있으면 1+ 2)반복이 되면서 i(키)가 저장되면서 같은Key가 있으면 key의값 증가
            counts[i]+= 1
        else: #키값이 없으면 i,   1)처음 반복될때는 i(키) 없고 
            counts[i]= i
    return counts 

counts= max_count(nums)
first= [] #list선언-> 키를 저장하는데 사용
max_count= max(counts.values()) #값이 가장큰수를 max함수를 사용하여 저장
for name, count in counts.items():
    print(name, ":", count, "번") #키, 값을 출력
    if count == max_count:  #가장큰 값을 확인하여
        first.append(name) #first(리스트)에 키를 저장
print('1등 :', first) #first출력

#1~10까지의 합을 구하는 함수
def sum(n):
    hap= 0
    for i in range(1,n+1): #range(시작값,마지막값)에서 'n'에 값을 +1를 하지않을 경우에 0~9까지만 반복된다
        hap +=i
    return hap

print(sum(10)) 