import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

#db 설정
dbURL= "127.0.0.1"
dbPost= 3306
dbUser= "root"
dbPass= "root"

#db 연결
conn= pymysql.connect(host= dbURL, port= dbPost, user= dbUser, passwd= dbPass, db='bigdb', charset='utf8', use_unicode=True) 
#db sql문, 부산에 대한 정보를 가져오는 sql로 설정
select_date= "select * from `forecast` where city= '부산'"

#한글 설정
font_path= "c:/Windows/fonts/malgun.ttf"
font_name= mpl.font_manager.FontProperties(fname=font_path).get_name() #폰트설정(한글사용)
mpl.rc('font', family=font_name)

#sql 실행, 데이터를 가져온다
cur= conn.cursor()
cur.execute(select_date)
result= cur.fetchall()

high= []
low= []
wf= []
xdata= []

#최고 기온, 최저기온 저장
for row in result:
    high.append(row[5])
    low.append(row[4])
    xdata.append(row[2].split('-')[2]) #시간(날짜(일),날짜시간(일))
#print(high)

#부산 날씨 직선 그래프로 그린다
plt.figure(figsize=(10,6)) #그래프 크기
plt.plot(xdata, low, label= '최저기온')
plt.plot(xdata, high, label= '최고기온')

plt.legend() 
plt.show()

#부산(지역) wf(날짜)별 count 출력
#select wf, count(*) from forecast where city='부산' group by wf;
select_data1= "select wf, count(*) from forecast where city='부산' group by wf"
cur.execute(select_data1)
result1= cur.fetchall()

#가져온 데이터(날짜별 개수)를 그래프로 그린다
wfData= []
wfDataCount= []
for row in result1:
    wfData.append(row[0])
    wfDataCount.append(row[1])
plt.bar(wfData,wfDataCount) #바 형태의 그래프
plt.show()

plt.title('부산 날씨 그래프(%)')
plt.pie(wfDataCount, labels=wfData, autopct='%.1f%%') #원 형태의 그래프
plt.show()
