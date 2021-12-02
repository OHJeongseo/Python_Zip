import numpy as np, usercsv, pandas as pd

#quest.csv 파일 읽기
# f= open('quest.csv', 'r')
# reader= csv.reader(f) 


 #파일읽어서 배열형태로 저장
#quest= np.array(usercsv.swithcsv(usercsv.opencsv('quest.csv')))
f= pd.read_csv('quest.csv', encoding='cp949') #pandas로 파일읽기
quest= np.array(f)
print(quest)
 #5보다 큰수 확인
print(quest>5) #5보다 큰수는 True, 작은수는 False로 출력된다
quest[quest>5]= 5 #5보다 큰수를 5로 입력
print(quest)
