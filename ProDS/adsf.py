from requests import get
from bs4 import BeautifulSoup as Soup
import pandas as pd
from datetime import datetime

Name = []
MovieId = []
Year = []
Rating = []
Meta_score = []
Votes = []
Genre = []
Director = []
Stars = []

Date = datetime.today().strftime("%Y-%m")    # YYYYmmddHHMMSS 형태의 시간 출력

url = get('https://www.imdb.com/movies-coming-soon/' + Date + '/?ref_=cs_dt_pv')
request = url.text
soup_data = Soup(request, 'html.parser')
movies = soup_data.findAll('div', {'class' : 'list_item odd'})

for i in movies:
    # 영화 제목
    Name.append(i.h4.a.text[:-7])
    # 영화 년도
    Year.append(i.h4.a.text[-5:-1])
    # 영화 ID
    MovieId.append(i.h4.a["href"][-8:-1])
    # 영화 장르
    tmp = i.select('p> span')
    tmp = list(filter(lambda x: str(x)[:6] == '<span>', tmp))
    tmp = list(map(lambda x: str(x).replace('<span>','').replace('</span>',''), tmp))
    Genre.append(tmp)
    # 영화 감독
    Director.append(i.find('div', {'class' : 'txt-block'}).span.text.strip())
    # 영화 배우
    
    Stars_ = list(map(lambda x: str(x).replace('</a>',''), i.select('div.txt-block> a')))
    # print(Stars_)

    result = []
    for e in Stars_:
        sign = False
        a_result = ''

        for c in e :
            if sign:
                a_result += c

            elif c == '>':
                sign = True
        
        result.append(a_result)

    Stars.append(result)

    # Stars.append(result)
    # print(result)


    # Meta Score
    try :
        Meta_score.append(i.tr.find('div', {'class':'rating_txt'}).span.text.strip())
    except:
        Meta_score.append(0)

print(Stars)