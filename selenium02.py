from selenium import webdriver as wd #웹 브라우저 원격 조작에 사용하는 라이브러리
import time

path= 'C:\\Users\\wjdtj\\Downloads\\chromedriver_win32\\chromedriver.exe' #크롬드라이버 실행파일 위치
 #옵션설정
options= wd.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver= wd.Chrome(path, options= options)

 #인터파크 사이트
driver.get("http://tour.interpark.com")

 #검색 설정
driver.find_element_by_id('SearchGNBText').send_keys('스위스') #검색어 입력, send_keys-> 키보드 입력, id속성으로 추출
driver.find_element_by_class_name('search-btn').click() #클래스 이름으로 해당요소 추출
driver.implicitly_wait(10) #대기 시간 설정

driver.find_element_by_id('li_R').click() #해외여행 클릭
driver.implicitly_wait(10)

#body > div.container > div.searchSct > div > div.panelZone > div:nth-child(1) > div > ul > li

for page in range(1,8):
    driver.execute_script("searchModule.SetCategoryList({},'')".format(page))  #스크랩트 실행, format(page) 1
    time.sleep(3)
    print(str(page)+"번째 페이지") 
     #find_elements_by_css_selector-> css선택자로 요소 여러개 추룰
    boxItem= driver.find_elements_by_css_selector('.panelZone >.oTravelBox >.boxList >li')
     
     #여행 정보 추출(제목, 가격)하여 출력
    for li in boxItem:
         #find_element_by_css_selector-> css선택자로 요소 하나 추룰
        print('제목', li.find_element_by_css_selector('h5.proTit').text) 
        print('가격', li.find_element_by_css_selector('.proPrice').text.split('원')[0])
        print('='*100)
