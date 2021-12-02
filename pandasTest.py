import pandas as pd# 테이블 형태를 다루는 라이브러리 1차원 series, 2차원 DataFrame 3차원 Panel
 
 #사전(딕셔너리)
data= {
    'name': ['Mark','Jane','aaa','rr'],
    'age': [33,44,55,11],
    'score': [91.2, 88.5, 55.6, 88.9]
}

 #2차원 테이블 형태로 변환
df= pd.DataFrame(data)
print(df)
print(type(df))
 #테이블에 함수를 설정하여 결과를 출력
print(df.sum()) #합계
print(df.mean()) #평균(float64-실수형)
print(df.age) #df['age'] int64-정수형 