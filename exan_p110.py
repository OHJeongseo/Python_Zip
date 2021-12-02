#p110~ 111
training_data= [['연두', 3, '사과'],
                ['노랑', 3, '사과'],
                ['빨강', 2, '포도'],
                ['빨강', 1, '포도'],
                ['노랑', 3, '레몬']]
                
def fruit_counts(data): #과일이 몇개 있는지 확인하는 함수
    counts= {}
    for row in data:
        label= row[-1] #과일의 인덱스 위치
        if label not in counts: #과일이 없으면 
            counts[label]= 0
        counts[label]+= 1 #과일이 있으면
    return counts

result= fruit_counts(training_data)
print(result)

def fruit_color(data): #색깔이 몇개가 있는지 확인하는 함수
    counts= {}
    for row in data:
        color= row[0] #색깔을 인덱스 위치 
        if color not in counts: #색깔이 없으면
            counts[color]= 0
        counts[color]+= 1 #색깔이 있으면
    return counts

colorCnt= fruit_color(training_data)
print(colorCnt)

 #
import pandas as pd, matplotlib.pyplot as plt  # 데이터를 시각화 자료를 만드는 라이브러리

#pandas를 사용하여 DataFrame을 만들고 만든 DataFrame를 파일로 만들기
df= pd.DataFrame([[500, 450, 570, 610],
                  [630, 700, 820, 900],
                  [1100, 1030, 1200, 1380],
                  [1500, 1650, 1700, 1850],
                  [1990, 2020, 2300, 2400],
                  [1020, 1600, 2200, 2550]],
                index= ['2015','2016','2017','2018','2019','2020'],
                columns= ['1분기', '2분기', '3분기', '4분기'] )
print(df)
#df.to_csv('seles.csv', header='False') #파일 내보내기

 #df의 결과를 차트(라인플롯)로 만들기
y1= [500, 450, 570, 610]
y2= [630, 700, 820, 900]
y3= [1100, 1030, 1200, 1380]
y4= [1500, 1650, 1700, 1850]
y5= [1990, 2020, 2300, 2400]
y6= [1020, 1600, 2200, 2550]
x= range(len(y1))
xLabel= ['first', 'second', 'third','fourth']
plt.plot(x, y1, color='b')
plt.plot(x, y2, color='orange')
plt.plot(x, y3, color='green')
plt.plot(x, y4, color='red')
plt.plot(x, y5, color='purple')
plt.plot(x, y6, color='brown')
plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarterly')
plt.ylabel('sales')
plt.xticks(x, xLabel, fontsize=10)
plt.legend(['2015','2016','2017','2018','2019','2020'])
plt.show()
