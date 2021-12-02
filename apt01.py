import usercsv, re, csv

#apt_201910.csv 파일 3줄 출력
#ap= usercsv.opencsv('apt_201910.csv')
apt= usercsv.swithcsv(usercsv.opencsv('apt_201910.csv')) #csv파일읽고 저장하고 숫자변환하는 코드를 한줄로 작성
# print(apt[:3])

#apt_201910.csv 총개수
#print(len(apt))

#시군구 단지명 가격
#for i in apt[:6]:
#    print(i[0],i[4],i[-4])

 #강원도'i[0]'의 면적(120이상)'i[5]' 가격(3억이하)'i[-4]' 시군구 단지명 가격출력, #i[]-> 출력하고자 하는 인덱스의 위치값 
new_list= [['시군구','단지명','가격']]
for i in apt:
    try:
        if i[5]>120 and i[-4]>=30000 and re.match('강원',i[0]):
            #print(i[0],i[4],i[-4])
            new_list.append([i[0],i[4],i[-4]])
    except:
        pass
print(new_list)

#파일 저장-> 종료포함
# with open('apt11.csv','w', newline='') as f:
#     a= csv.writer(f, delimiter= ',')
#     a.writerow(new_list)



total= ['종로구','151,767', '11,093', '27,394']
 # , 제외하고 숫자를 정수형으로 표현하여 출력
for i in total:
    if re.search(',',i):
        total[total.index(i)]= int(re.sub(',','',i))
print(total)
 #다차원 리스트-> 리스트안에 리스트가 포함되어있는
pop= [
    ['종로구', 151767.0], ['중구', 126409.0],
    ['용산구', 228830.0],['광진구', 352692.0],
    ['동대문구', 346551.0]
    ] 
 #30만명보다 인구'pop[1]'->가 적은 지역의 이름을 출력
for i in pop:
    if i[1] <300000:
        print(i[0])