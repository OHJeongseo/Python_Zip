import usercsv, re #usercsv-> 사용자 정의한 py파일(csv파일 읽고 저장하고 숫자문자('102,100'등)를 숫자로 변환하는 기능을 설정)

total= usercsv.opencsv('popSeoul.csv') #csv파일 저장
newPop= usercsv.swithcsv(total) #csv파일의 숫자문자를 숫자로 변환

print(newPop[:4])
new= [['구', '한국인', '외국인', '외국인비율(%)']]

 #반복문을 사용해서 new리스트에 들어갈 값을 설정하고 설정된 값을 출력한다
for i in newPop: 
    foreign= 0
    try:
        foreign= round(i[2]/(i[1]+i[2])*100,1) #new에 외국인비율(%)를 구한다
        #print(i[0], foreign)
        if foreign > 3:
            #print(i[0],foreign)
            new.append([i[0],i[1],i[2],foreign]) #설정한 값을 기존리스트에 추가한다
    except:
        pass

print(new)