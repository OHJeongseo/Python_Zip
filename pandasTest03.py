import pandas as pd# 테이블 형태를 다루는 라이브러리 1차원 series, 2차원 DataFrame 3차원 Panel

data_dic= {
    'year': [2018,2019,2020,2021],
    'sales': [350,400,1050,2000]
}
print(data_dic)
 #사전-> DataFrame
df1= pd.DataFrame(data_dic)
print(df1)
print(type(df1))

 # 리스트 형태로 사용 # index 행 이름, columns 열 이름
df2= pd.DataFrame([[89.2, 92.5, 90.8],[92.8, 89.9, 95.2]], index=['중간고사','기말고사'], columns=['1반', '2반', '3반'])
print(df2)
df3= pd.DataFrame([[20201101, 'Kim', 90, 95],[20201102, 'Pack', 78, 88],
                   [20201103, 'Hong', 58, 77],[20201104, 'Lee', 95, 66]],
                   columns= ['학번', '이름', '중간고사', '기말고사'] )
print(df3)
df4= pd.DataFrame([[20201101, 'Kim', 90, 95],[20201102, 'Pack', 78, 88],
                   [20201103, 'Hong', 58, 77],[20201104, 'Lee', 95, 66]],
                   )
df4.columns= ['학번', '이름', '중간고사', '기말고사']
print(df4)
print(df4.tail())
df3.to_csv('pandastest.csv', header='False') #파일 내보내기
df5= pd.read_csv('pandastest.csv', encoding='utf-8') #파일 읽기
print(df5)

