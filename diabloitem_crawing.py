from os import name
from selenium import webdriver as wd #웹 브라우저 원격 조작에 사용하는 라이브러리
import time
import re
import pandas as pd


path= 'C:\\Users\\wjdtj\\Downloads\\chromedriver_win32\\chromedriver.exe' #크롬드라이버 실행파일 위치
 #옵션설정
options= wd.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver= wd.Chrome(path, options= options)

 #디아블로2 인벤 사이트
driver.get("https://diablo2.inven.co.kr/")



 
#아이템 DB 클릭
driver.find_element_by_link_text('아이템 DB').click() #클래스 이름으로 해당요소 추출
#driver.implicitly_wait(10) #대기 시간 설정

# driver.find_element_by_link_text('대거').click() #클래스 이름으로 해당요소 추출
# driver.implicitly_wait(10) #대기 시간 설정

# Info= driver.find_elements_by_css_selector('table > tbody >tr') 
#driver.implicitly_wait(10) #대기 시간 설정

category1= ['대거','한손검','양손검','클럽','메이스','해머','한손도끼','양손도끼','스태프',
            '원드','셉터','스피어','폴암','재벌린','보우','크로스보우','스로잉','클러','오브',
            '헬름','아머','쉴드','글러브','부츠','벨트','서클릿',
            '반지','목걸이','주얼','부적']

#print(len(category1))
datas= []
for a in range(len(category1)):
    
    driver.find_element_by_link_text(category1[a]).click() #클래스 이름으로 해당요소 추출
    #time.sleep(3) # 추가!!

    Info= driver.find_elements_by_css_selector('table > tbody >tr') 
    for j in Info:    
        item_name= j.find_elements_by_class_name('item-name')
        options= j.find_elements_by_class_name('options')
        recommended_job_core_skills=  j.find_elements_by_class_name('recommended-job-core-skills')
        for i in range(len(item_name)):
            datas.append([re.sub('\n', '/', item_name[i].text),
                        re.sub('\n', '/', options[i].text),
                        re.sub('\n', '/', recommended_job_core_skills[i].text), category1[a]])
    
#print(datas)



# datas= []
# for j in Info:    
#     # print("이름:\n", j.find_element_by_class_name('item-name').text)
#     # print("옵션:\n", j.find_element_by_class_name('options').text)
#     # print("추천 직업/핵심 장비:\n", j.find_element_by_class_name('recommended-job-core-skills').text)
#     # print("="*50)
    
#     item_name= j.find_elements_by_class_name('item-name')
#     options= j.find_elements_by_class_name('options')
#     recommended_job_core_skills=  j.find_elements_by_class_name('recommended-job-core-skills')
#     for i in range(len(item_name)):
#         datas.append([re.sub('\n', '/', item_name[i].text),
#                       re.sub('\n', '/', options[i].text),
#                       re.sub('\n', '/', recommended_job_core_skills[i].text)])

# print(datas)

df= pd.DataFrame(datas)
df.to_csv('diablo.csv', header='False' ,encoding='utf-8-sig')

#리스트의 데이터를 csv파일로 내보낸다
# with open('diablo.csv','w') as file:
#     file.write('아이템, 옵션, 추천 직업/핵심 장비 카테고리\n')
#     for item in datas:
#         row= ','.join(item)
#         file.write(row+'\n')
    
    
 
    

