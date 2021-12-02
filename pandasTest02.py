import pandas as pd# 테이블 형태를 다루는 라이브러리 1차원 series, 2차원 DataFrame 3차원 Panel

 #apt.csv파일을 읽어 DateFrame형태로 출력
df= pd.read_csv('apt.csv', encoding='cp949') #pandas로 파일읽기
print(type(df))
print(len(df))
print(df.head())
print(df.tail())

 #면적(130이상) 출력
print(df.면적>130) # df.지역
print(df[df.면적>130])

 #면적(130이상)의 아파트의 가격 출력
print(df.가격[df.면적>130])

 #면적(130이상)의 가격이 2억 미만인 아파트의 가격출력 &and
print(df.가격[(df.면적>130)&(df.가격<20000)]) 
 #면적(130이상)이거나 가격이 2억 미만인 아파트의 가격출력 |or
print(df.가격[(df.면적>130)|(df.가격<20000)])

 #df.loc[원하는 행 조건, 원하는 열의 조건]
 #아파트+ 가격을 10번째 까지 출력
print(df.loc[:10, ['아파트', '가격']])

 #정렬
dfAsc= df.sort_values(by='가격', ascending=False) #가격이 높은순(False)으로 가공 
print(dfAsc)
print(dfAsc.loc[:10, ['아파트','가격']])

 #4억원을 초과하는 가격으로 거래된 아파트,가격 출력
print(df.가격[df.가격>40000])
print(df.loc[:,['아파트','가격']][df.가격>60000])
 #추가
df['단가']= df.가격/df.면적
print(df.loc[:10, ('가격','면적', '단가')])

 #지역에 강릉이 들어간 자료만 출력
print(df[df.지역.str.find('강릉')>-1]) #str.find(없으면 -1)  #str.index(없으면 error)
local_area= df[df.지역.str.find('강릉')>-1]
 #강릉이 들어간 지역, 가격, 단가
print(local_area.loc[:10,('지역','가격','단가')])
