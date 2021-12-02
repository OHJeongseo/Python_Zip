import csv, re
 #파일(csv)를 읽어서 리스트로 저장하는 함수
def opencsv(filename):
    f= open(filename, 'r')
    reader= csv.reader(f) #csv파일을 읽어서 reader변수에 담는다
    output= []
    for i in reader:
        output.append(i)
    return output #읽은 csv파일을 리스트 output에 담아 반환한다

total= opencsv('popSeoul1.csv')
for i in total[:5]: #슬라이싱을 사용하여 1번째부터 5번째까지만 출력한다
    print(i)

 # ,를 제외한다
for i in total[:5]: 
    for j in i:
        try:
             #i.index(j)-> 변경(re.sub)된 위치를 가져온다
            i[i.index(j)]= float(re.sub(',','',j)) #리스트로 저장된 데이터에서 쉼표표시를 제거한후 float으로 변환
        except:
            pass
print(total[:5]) #변환된 값을 출력

