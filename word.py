import wordcloud #글자를 그림으로 그릴수있는 라이브러리 
import matplotlib.pyplot as plt

keywords= {'안녕':2, '하세요':1, '빅데이터':5, '웹크롤링':3}

wc= wordcloud.WordCloud(font_path='c:/Windows/fonts/malgun.ttf')
cloud= wc.generate_from_frequencies(keywords)

#keywords를 그림을 그린다(개수에 따라 크기가 다르게 표시)
figure= plt.figure()
plt.imshow(cloud)
plt.show()
#figure.savefig('word.png') #이미지로 저장