from selenium import webdriver as wd #웹 브라우저 원격 조작에 사용하는 라이브러리
from selenium.webdriver.common.keys import Keys # END Key를 사용 import
import time


path= 'C:\\Users\\wjdtj\\Downloads\\chromedriver_win32\\chromedriver.exe' #크롬드라이버 실행파일 위치
 #옵션설정
options= wd.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver= wd.Chrome(path, options= options)

#백종원의 요리비책으로 검색한 주소
driver.get("https://www.youtube.com/c/paikscuisine/videos")
body_tag= driver.find_element_by_tag_name('body')
print(body_tag)

body_tag.send_keys(Keys.END) #스크롤 1번 진행

#화면의 길이 확인
print(driver.execute_script('return document.documentElement.scrollHeight'))

while True:
    last_height= driver.execute_script('return document.documentElement.scrollHeight')
    print('last_height= ', last_height)

    #10번 스크롤 하기
    for i in range(10):
        body_tag.send_keys(Keys.END)
        time.sleep(1)
    new_height= driver.execute_script('return document.documentElement.scrollHeight')
    print('new_height= ', new_height)

    if new_height== last_height:
        print("화면 길이가 같아서 반복문 종료")
        break
    print("="*100)    

