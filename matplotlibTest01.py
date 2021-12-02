import matplotlib.pyplot as plt # 데이터를 시각화 자료를 만드는 라이브러리
import numpy as np  

 #점선 그래프 'bo'-> 'b(Blue)'는 색상을 표시하고 'o'는 모양을 표시
points= np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p= np.array([2.5,2])
plt.plot(points[:,0],points[:,1],"ro") #빨간색 점표시
plt.plot(p[0],p[1],"bo") #파란색 점표시
plt.show()