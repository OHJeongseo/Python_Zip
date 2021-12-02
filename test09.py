import csv, re

f= open('popSeoul.csv', 'r')
reader= csv.reader(f)
#print(reader)
output= []

 #test08.py + usercsv.py를 한번에 작성한 파일 
for i in reader:
    tmp= [] #여러번 반복되지않도록 리스트를 생성
    for j in i:
        try:
            if re.search('\d', j): #숫자[0-9]패턴을 확인하고
                #i[i.index(j)]= float(re.sub(',','',j)) # , 사용안함
                #output.append(i)
                tmp.append(float(re.sub(',','',j))) # 숫자로 변환한다
            else:
                tmp.append(j) #숫자가 아닌것은 그대로 추가한다
        except:
            pass
    output.append(tmp) #추가(tmp)한 리스트(숫자패턴일경우 숫자로 변환한)를 출력할 리스트(output)에 담는다
#print(output)

new= [['구','한국인','외국인','외국인비율(%)']]
for i in output:
    foreign= 0
    try:
        foreign= round(i[2]/(i[1]+i[2])*100,1) #비율을 계산하고
        if foreign > 3:
            #print(i[0],i[1],i[2],foreign)
            new.append([i[0],i[1],i[2],foreign]) #설정완료된 값을 리스트에 추가한다
    except:
        pass
print(new)