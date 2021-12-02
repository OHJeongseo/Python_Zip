from matplotlib import legend
import pandas as pd #파일 읽기 사용
import matplotlib as mpl #폰트 설정
import matplotlib.pyplot as plt #그래프 그리기 사용

 #파일을 읽어서 결과를 출력(한글 인코딩, index_col를 설정)
df= pd.read_csv('weather.csv', index_col= 'point', encoding='euc-kr')
#print(df)

 #서울, 인천, 대전, 대구, 광주, 부산, 울산만 추출
city_df= df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']] #loc[행,열] 특정부분에 대한 조건을 사용
print(city_df)
# print(df.loc['서울']) #서울 추출
# print(df.loc[['서울','부산']]) #서울, 부산추출

 #그래프 그리기
font_name= mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name() #폰트설정(한글사용)
mpl.rc('font', family=font_name)
  #차트 종류, 제목, 차트크기, 범례, 폰트 크기 설정
ax= city_df.plot(kind= 'bar', title= '날씨', figsize=(12,7), legend= True, fontsize= 12)
ax.set_xlabel('도시', fontsize= 12)
ax.set_ylabel('기온/습도',fontsize= 12)
ax.legend(['기온', '습도'], fontsize= 12)
plt.show()


