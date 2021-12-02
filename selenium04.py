from selenium import webdriver as wd #웹 브라우저 원격 조작에 사용하는 라이브러리
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib as mpl
import time, re
import pandas as pd


path= 'C:\\Users\\wjdtj\\Downloads\\chromedriver_win32\\chromedriver.exe' #크롬드라이버 실행파일 위치
 #옵션설정
options= wd.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver= wd.Chrome(path, options= options)

#백종원의 요리비책으로 검색한 주소
driver.get("https://www.youtube.com/c/paikscuisine/videos")
page= driver.page_source

soup= BeautifulSoup(page, 'html.parser')
all_videos= soup.find_all(id= 'dismissible')

#영상의 제목, 시간, 조회수 추출하여 리스트로 저장
datas= []
for video in all_videos:
    title= video.find(id= 'video-title')
    video_num= video.find('span', {'class':'style-scope ytd-grid-video-renderer'})
    video_time= video.find('span', {'class':'style-scope ytd-thumbnail-overlay-time-status-renderer'})
    datas.append([title.text, video_time.text.strip(), video_num.text])
#print(datas)


youtube= pd.DataFrame(datas, columns= ('제목', '재생시간', '조회수'))
#print(youtube.head())
#print(youtube)

#파일로 내보내기
#youtube.to_csv('recipe5.csv', mode= 'w', encoding='utf-8', index=True)

#한글처리
font_name= mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name() 
mpl.rc('font', family=font_name)

dict_youtube= {'100만이상':0, '50만이상':0, '10만이상':0} 

#조회수를 확인해서 조회수별로 개수를 구하기
for item in datas:
    #조회수에서 숫자추출
    item= float(str(item).split('조회수')[1].split('만회')[0].strip())
    #print(item)

    if item>= 100:
        dict_youtube['100만이상']+= 1
    elif item>= 50:
        dict_youtube['50만이상']+= 1
    elif item>= 10:
        dict_youtube['10만이상']+= 1
print(dict_youtube)

#조회수의 결과를 그래프로 그리기
figure= plt.figure()
axes= figure.add_subplot(111)
axes.pie(dict_youtube.values(), labels=dict_youtube.keys(), autopct='%.1f%%')
plt.show()