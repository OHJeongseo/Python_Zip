import matplotlib.pyplot as plt  # 데이터를 시각화 자료를 만드는 라이브러리

 # 직선 그래프
x= [1,4,9,16,25,36,49,64]
# plt.plot(x)
# plt.show()

y= [i for i in range(1,9)]
#plt.plot(x,y)
 #라벨 설정
plt.xlabel('x')
plt.ylabel('y')
 #제목
plt.title('matplotlib sample')
#plt.show()

y1= [13,16,15,18,16,17,16]
 # plot 그래프를 보여준다
plt.plot(y1)
plt.show()