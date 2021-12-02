import numpy as np # 수치 데이터 처리를 위한 라이브러리

 #배열을 활용한 여러가지 방법
ar1= np.array([1,2,3,4,5]) #배열-> [1 2 3 4 5]
print(ar1)
print(type(ar1))

lst1= [1,2,3,4,5] #리스트-> [1, 2, 3, 4, 5]
print(lst1)
print(type(lst1))

ar2= np.array([[10,20,30],[40,50,60]])
print(ar2)

ar3= np.arange(1,11,2) #1~ 11까지 2씩 증가
print(ar3)

ar4= np.arange(10) #0~ 9, #(10)+1 1~ 10
print(ar4)

ar5= np.array([1,2,3,4,5,6]).reshape((3,2)) #reshape-> 행,열
print(ar5)

ar6= np.zeros((2,3)) #0으로 2행 3열
print(ar6)

ar7= ar2[0:2, 0:2] #
print(ar7)

ar8= ar2[0, :] #
print(ar8)

ar9= ar1*10
print(ar9)
 
print(ar1+ar9)
print(ar1*2)
print(ar1/2)
print("="*10)
print(ar2)
print(ar5)

# 행,열 곱
ar10= np.dot(ar2,ar5)
print(ar10)

ar2[:1]= 0
print(ar2)


