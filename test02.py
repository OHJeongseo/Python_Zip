# 함수사용
def seperate():
    a= int(input("수 입력:")) #input 문자타입으로 (변환할 타입)으로 묶어서 받는다
    if a%2==0:
        print('짝수')
    else:
        print('홀수')

def addReturn(a,b):
    return a+b

seperate() 
print(addReturn(3,5))