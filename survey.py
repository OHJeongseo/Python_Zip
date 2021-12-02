import pandas as pd

df= pd.read_csv('survey.csv', encoding='cp949') #pandas로 파일읽기
 #head() 출력
print(df.head())
print(df.mean()) #평균

 #수입(income) 평균, 합계
print("수입평균:",df.income.mean())
print("수입합계:",df.income.sum())
print("수입중앙값:",df.income.median())

print(df.describe()) #기본 정보(통계)
print(df.income.describe()) #income 통계

print(df.sex.value_counts()) #성별 분포


