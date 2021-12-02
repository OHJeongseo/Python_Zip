import csv, re

 #파일 읽어서 저장하고 저장된 리스트를 반환하는 함수
def opencsv(filename):
    f= open(filename, 'r')
    reader= csv.reader(f)
    output= []
    for i in reader:
        output.append(i)
    return output
    
 #숫자패턴을 확인해서 숫자로 변환하여 반환하는 함수
def swithcsv(listname):
    for i in listname: 
        for j in i:
            try:
                i[i.index(j)]= float(re.sub(',','',j)) 
            except:
                pass
    return listname