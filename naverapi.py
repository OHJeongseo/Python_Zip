import urllib.request
import datetime
import json



def getRequestUrl(url):
    req= urllib.request.Request(url)

    req.add_header("X-Naver-Client-Id", clientId)
    req.add_header("X-Naver-Client-Secret", clientSecret)

    try:
        response= urllib.request.urlopen(req)
        if response.getcode()== 200:
            print("[%s] Url Request Success: " %datetime.datetime.now())
            return response.read().decode('utf-8')
    
    except Exception as e:
        # print(e)
        # print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None


def getNavrSearch(node, srcText, start, display):
    base= 'https://openapi.naver.com/v1/search'
    node= '/news.json'
    parameters= '?query=%s&start=%s&display=%s' %(urllib.parse.quote(srcText), start, display)
    url= base+node+parameters
    responseDecode= getRequestUrl(url)

    if(responseDecode== None):
        return None
    else:
        return json.loads(responseDecode) #json문자열-> python객체로 변환 


def getPostData(post, jsonResult, cnt):
    title= post['title']
    description= post['description']
    org_link= post['originallink']
    link= post['link']
    pDate= post['pubDate']

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'org_link':org_link,
                        'link':link, 'pDate': pDate})
    

node= 'news'
srcText= '선거'
cnt= 0
jsonResult= []

jsonResponse= getNavrSearch(node, srcText, 1, 50)
total= jsonResponse['total']

while((jsonResponse!= None) and (jsonResponse['display']!= 0)):
    for post in jsonResponse['items']:
        cnt+= 1
        getPostData(post, jsonResult, cnt)

    start= jsonResponse['start']+jsonResponse['display']
    jsonResponse= getNavrSearch(node, srcText, start, 10)

print('전체검색: %d 건' %total)

 #파일로 내보내기(json형식으로)
with open('%s_naver_%s.json' %(srcText, node), 'w', encoding='UTF-8') as outfile:
    jsonfile= json.dumps(jsonResult, indent= 4, sort_keys= True, ensure_ascii= False ) #pytho-> json으로 변환
    outfile.write(jsonfile)

print('가져온 데이터: %d 건' %(cnt))
print('%s_naver_%s.json SAVED' %(srcText, node))



