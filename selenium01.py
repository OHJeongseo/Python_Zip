from selenium import webdriver as wd #웹 브라우저 원격 조작에 사용하는 라이브러리

path= 'C:\\Users\\wjdtj\\Downloads\\chromedriver_win32\\chromedriver.exe' #크롬드라이버 실행파일 위치
 #옵션설정
options= wd.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver= wd.Chrome(path, options= options)
driver.get('https://naver.com') #네이버 사이트
#print(driver)
 
 #검색 설정
driver.find_element_by_id('query').send_keys('파이썬') #검색어 입력, send_keys-> 키보드 입력
driver.find_element_by_id('search_btn').click() #검색버튼 클릭
