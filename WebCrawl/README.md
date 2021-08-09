# 웹 크롤링



- 브라우저 모듈 import

```python
import webbrowser;
```



- requests 모듈

```python
import requests
```



- import BeautifulSoup

```python
from bs4 import BeautifulSoup

```



- urllib 패키지 이용한 서버 요청

```python
from urllib.request import urlopen
```



### webbrowser 

- 웹브라우저 열기

```python
webbrowser.open('www.naver.com')
```



### requests 

1. 응답코드 

```python
requests.get("http://www.naver.com")
```

```python
<Response [200]>
```

응답 성공 : 200

응답 오류 : 400번대

클라이언트 오류 : 400번대

서버 오류 : 500번대



	2. text로 url 불러오기.

```python
url = 'www.naver.com'
requests.get(url).text
```



### BeautifulSoup

1. html 형태로 불러오기

```python
html_website_ranking = requests.get(url).text
soup_website_ranking = BeatifulSoup(html_website_ranking,"html.parser")
```

```python
<!DOCTYPE html>

<html lang="en">
<head>
<meta content="origin-when-cross-origin" name="referer"/>
<!-- Google Tag Manager -->
<script>
...
```



2. html의 특정태그 요소 찾기  

```python
# p 태그 요소 안에서 a 태그의 요소를 찾음
website_ranking = soup_website_ranking.select('p a')
```

```python
[<a href="https://support.alexa.com/hc/en-us/articles/200444340" target="_blank">this explanation</a>,
 <a href="/siteinfo/google.com">Google.com</a>,
 <a href="/siteinfo/naver.com">Naver.com</a>
 ...
```



3.  태그 내부의 text만 출력

```python
print(website_ranking[1].get_text()) # 태그 내부의 text를 반환하는 함수 
print(website_ranking[2].text)
```

```python
Google.com
Naver.com
```



4. 모든 랭킹을 리스트에 담기

```python
# 모든 랭킹을 가져와서 리스트에 담기
website_ranking_domain = [website_ranking_element.get_text() for website_ranking_element in website_ranking]

website_ranking_domain[:6]
# 순위와 상관없는 첫 번째 요소 제거
# website_ranking_domain.pop(0) 
```



5. 데이터 프레임에 데이터 담기

```python
import pandas as pd

website_ranking_dict = {'Website': website_ranking_domain}

df = pd.DataFrame(website_ranking_dict,columns=['Website'], index=range(1,(len(website_ranking_domain)+1)))

```

```python
	Website
1	Google.com
2	Naver.com
3	Youtube.com
4	Daum.net
5	Tistory.com
6	Kakao.com
```



---



1. 문서에서 원하는 내용 추출

```python
# html 문서에서 원하는 내용 추출
from urllib.request import urlopen
import bs4

url = "http://www.naver.com"
res = urlopen(url)
bs_obj = bs4.BeautifulSoup(res,'html.parser') # 반환 결과가 html 형태로 반환

print(bs_obj.prettify()) # 들여쓰기 해서 계층적인 구조로 출력
```

```python
<!DOCTYPE html>
<html data-dark="false" lang="ko">
 <head>
  <meta charset="utf-8"/>
  <title>
   NAVER
  </title>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=1190" name="viewport"/>
  <meta content="NAVER" name="apple-mobile-web-app-title">
   <meta content="index,nofollow" name="robots">
    <meta content="네이버 메인에서 다양한 정보와 유용한 컨텐츠를 만나 보세요" name="description">
```



2. find() : 선택자에 의해서 찾은 요소 중 첫 번째 요소를 반환

   findAll() / find_all() : 선택자에 의해서 찾은 모든 요소를 리스트로 반환

   ```python
   # 문자열
   html_str ="<html><div>hello</div><div>hi!!!</div></html>"
   # 문자열을 bs object로 변환
   bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
   
   # find() 이용해서 div 태그 반환 받기
   print(bs_obj.find("div"))
   
   # findAll() 이용해서 div 태그 반환 받기
   bs_obj.findAll("div")
   
   
   ```

   ```python
   <div>hello</div>
   [<div>hello</div>, <div>hi!!!</div>]
   ```



3. class 속성을 사용해서 선택

```python
html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul", {"class":"reply"})
```

```python
<ul class="reply">
<li>ok</li>
<li>no</li>
<li>sure</li>
</ul>
```



4. 형제노드 찾기 .next_sibling

```python
html_str = """
<html>
    <body>
        <h1>파이썬 프로그래밍</h1>
        <p>웹 페이지 분석</p><p>크롤링</p><p>파싱</p>        
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
p1 = bs_obj.find("p")
p1
print(p1.next_sibling)
```

```
<p>웹 페이지 분석</p>
<p>크롤링</p>
```



5. 속성 값 추출하기 (a태그의 href 속성 추출)

```python
html_str = """
<html>
    <body>
        <ul class="ko">
            <li><a href="https://www.naver.com/">네이버</a></li>
            <li><a href="https://www.daum.net/">다음</a></li>
        </ul>
        <ul class="sns">
            <li><a href="https://www.goole.com/">구글</a></li>
            <li><a href="https://www.facebook.net/">페이스북</a></li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
a_t = bs_obj.find("a")
a_t
# 모든 a 태그의 href 주소 얻어오기;
a_ts = bs_obj.findAll("a")
a_ts
lis = []

for a_t in a_ts:
    print(a_t['href'])
    lis.append(a_t['href'])
    
lis

```

```python
<a href="https://www.naver.com/">네이버</a>
['https://www.naver.com/',
 'https://www.daum.net/',
 'https://www.goole.com/',
 'https://www.facebook.net/']
```



- selector 함수 사용할 수 있음.

```python
for i in bs_obj.select('a[href]') :
    print(i.text)
    
```

```python
네이버
다음
구글
페이스북
```







### urllib

1. urllib 서브 패키지 request의 urlopen() 모듈 이용

```python
# urllib 패키지 이용한 서버 요청
from urllib.request import urlopen
url = "http://www.naver.com"
res = urlopen(url)
print(res.read())
```

```python
b'\n<!doctype html>                          <html lang="ko" data-dark="false"> <head> <meta charset="utf-8"> <title>NAVER</title> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=1190"> <meta name="apple-mobile-web-app-title" content="NAVER"/> <meta name="robots" content="index,nofollow"/> 
```





---

---

# 쇼핑몰 크롤링

### 쇼핑몰 상품 페이지에서 상품의 이름, 할인 전 가격, 할인 후 가격 추출 해서 DF에 넣고 csv파일로 저장하기



1.  requests.get(url)로 서버로부터 응답 권한이 있는지 확인.

   - 403 Error 일 경우 / html.parser 이용

     - ```python
       res = urlopen(url)
       bs_obj = BeautifulSoup(html, "html.parser")
       ```

     

2. 페이지에서 상품전체를 나타내는 태그를 크롬 개발자도구를 이용해 찾는다.

   - 모든 상품 정보가 들어있는 태그가 ``ul class="prdList grid4"`` 인 경우

     - ```python
       ul = bs_obj.find("ul", {"class":"prdList grid4})
       ```

   - ul 태그 안의 각각 제품들의 태그가 ``div class="box"`` 인 경우

     - ```python
       prd_boxes = ul.findAll("div",{"class":"box"})
       ```

     - ```python
       print(len(prd_boxes)) # 로 상품의 개수가 알맞게 나왔는지 확인.
       ```

   - prd_boxes 태그 중 ``상품 제목``의 태그가 ``p class="name"``의 ``span`` 태그 인 경우

     - ```python
       # 첫번 째 제품명 출력
       prd_boxes[0].find("p",{"class","name"}).find("span") .text
       ```

     - ```python
       # 전체 상품명 출력
       for box in prd_boxes:
           p_tag = box.find("p",{"class":"name"})
           span = p_tag.find("span")
           print(span.text)
       ```

   - prd_boxes 태그 중 ``상품 가격``의 태그가 ul 태그 밑에 span 태그에 원래가격과 할인가격이 있다.

     - ```python 
       # 첫번째 제품의 할인 전 가격과 할인 후 가격 출력
       price_ul = prd_boxes[0].find("ul")
       price_span = price_ul.findAll("span")
       # 할인 전 가격은 span의 1번 인덱스, 할인 후 가격은 마지막 인덱스에 있다.
       print(price_span[1].text)	# 할인 전 가격
       print(price_span[-1].text)  # 할인 후 가격
       ```

     - ```python
       # 전체 가격 출력
       for box in prd_boxes :
           price_ul = box.find("ul")
           price_span = price_ul.findAll("span")
           print("가격 : ", price_span[1].text)
           print("세일 가격 : ", price_span[-1].text)
       ```

       

3.  수집한 데이터 DF 저장

   - 수집 데이터를 저장할 빈 리스트 생성

     - ```python
       # 수집 데이터를 저장할 빈 리스트 생성
       prd_list = []
       price_list = []
       sale_price_list = []
       ```

   - 각각 추출한 데이터 빈 리스트에 저장

     - ```python
       for box in prd_boxes :
           # 제품명 추출 코드
           p_tag = box.find("p",{"class":"name"})
           span = p_tag.find("span")
           # 가격 추출 코드
           price_ul = box.find("ul")
           price_span = price_ul.findAll("span")
           # 최종 data 추출 후 리스트에 저장
           prd_list.append(span.text)
           price_list.append(price_span[1].text)
           sale_price_list.append(price_span[-1].text)
       ```

   - 데이터 프레임에 저장하기

     - ```python
       prd_dict={"품목":prd_list,
                 "가격":price_list,
                 "세일가격":sale_price_list}
       prd_df = pd.DataFrame(prd_dict,index=range(1,(len(prd_list)+1)))
       ```

   - 데이터 프레임 csv 파일로 저장하기

     - ```python
       prd_df.to_csv("./crawl_data/prd1page.csv")
       ```






---

---



# 구글맵스 geocode

``` 
경찰서을 불러서 구글지도에 마커 표시
```



1. 사용 데이터 프레임 불러오기

   - ```python
     crime_anal_police = pd.read_csv('./data/02. crime_in_Seoul.csv',
                           thousands=',', # 천 단위 구분 기호 정수형태로 부르기
                                    encoding='euc-kr')
     ```

2. googlemaps 패키지 import 후 googlemaps  클라이언트 생성

   - ```python
     import googlemaps # 안되면 pip install googlemaps
     gmapsKey = 'api key'
     gmaps = googlempas.Clinet(key=gmapsKey)
     ```

3. 경찰서 정보를 geocode를 이용해서 저장

   - geocode('경찰서', language='ko')

   - ```python
     tmp = gmaps.geocode('서울중부경찰서', language='ko')
     ```

   - ```python
     tmp[0]['formatted_adreess'] # '대한민국 서울특별시 중구 을지로동 수표로 27'
     tmp[0]['geometry']['location']['lat'] # 37.5636465
     tmp[0]['geometry']['location']['lng'] # 126.9895796
     ```

4. 모든 경찰서 정보 저장

   - ```python
     #데이터 저장할 빈 list 필요
     station_address=[]
     station_lat=[]
     station_lng=[]
     
     for name in station_name :
         # 각 경찰서에 대한 geocode 추출
         tmp = gmaps.geocode(name, language='ko')
         station_address.append(tmp[0].get('formatted_address')) # 경찰서 주소 저장 : dict.get(key) -> key에 대한 value 반환
         
         # 위 경도 추출
         tmp_loc = tmp[0].get('geometry')
     
         station_lat.append(tmp_loc['location']['lat'])
         station_lng.append(tmp_loc['location']['lng'])
                                    
     ```

5.  DF으로 저장하기

   - ```python
     cols = {"경찰서명" : station_name,
             "주소":station_address,
             "lat":station_lat,
             "lng":station_lng}
     
     df_police = pd.DataFrame(cols, index=range(1,(len(station_name)+1)))
     df_police
     ```

6. DF을 .csv로 저장

   ```python
   df_police.to_csv("./crawl_data/서울시경찰서정보.csv")
   ```





---

---

# FOLIUM



1. folium 패키지 : 지도 이용해 data 시각화  

   ```python
   import folium
   map_osm = folium.Map(location=[45.5236, -122.67], zoom_start =13)
   map_osm
   ```

   

2.  위에 수집한 서울시 경찰서 위치를 지도에 시각화

   - 수집한 경찰서 csv 파일 불러온 후 경찰서명,위도,경도 데이터 각각 리스트에 저장

   - ```python
     police_adr = pd.read_csv('./crawl_data/서울시경찰서정보.csv', index_col=0)
     
     police_lat = police_adr['lat']
     police_lng = police_adr['lng']
     police_info = police_adr['경찰서명']
     
     # 서울을 중심으로 지도를 다시 생성
     map_police = folium.Map(location=[lat,lng], zoom_start = 18)
     map_police
     
     ```

   - for 문을 이용해 각 경찰서 위치에 마커 표시하기

   - ```python
     for k in range(1,len(police_info)+1) :
         folium.Marker([police_lat[k],police_lng[k]], # 위경도
                      popup = police_info[k],
                      icon = folium.Icon(icon='info-sign')).add_to(map_police)
     
     ```

   - 



---

---

# 시카고 샌드위치 가게 정보 크롤링 지도 시각화

```  
'https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'

위 사이트에서 main url에서 가게 순위, 가게명, sub page 링크
sub page에서 상품명, 상품 가격, 가게 위치 정보를 수집해서 구글 지도에 위치를 마커 표시하기.
```



1. BeautifulSoup 객체에 넣기 위해 변수 작업

   - HTTP Error 403 에러 피하기 위해 header 설정

     - ```python
       req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
       res = urlopen(req)
       
       soup_obj = BeautifulSoup(res, "html.parser")
       ```

2.  url에서 랭킹 정보가 들어있는 태그를 찾기.

   - 사이트 내 랭킹 정보가 div class="sammy" 태그 밑에 있음

     - ```python
       # div class="sammy"에 저장된 모든 샌드위치 랭킹정보를 저장.
       soup_list = soup_obj.findAll('div',{"class":"sammy"})
       ```

   - 가게 순위는 class="sammyRank", 상호명은 class="sammyListing", 서브 페이지 url은 a href= 태그 밑에

3.  50개의 가게 정보를 리스트에 저장

   - list에 저장

     - ```python
       rank =  []
       main_menu = []
       cafe_name = []
       url_link = []
       
       # soup_list안의 레스토랑 각각에 대한 정보를 추출해서 list에 저장하는 코드
       for item in soup_list : #레스토랑 1개의 정보가 item에 저장
           rank.append(item.find(class_='sammyRank').get_text())
           tmp_listing = item.find(class_="sammyListing").get_text()
           main_menu.append(tmp_listing.split('\n')[0])
           cafe_name.append(tmp_listing.split('\n')[1])
           url_link.append(urljoin(url_base,item.find('a')['href']))
       ```

4. 수집한 자료를 df로 저장후 csv로 파일 저장

   - ```python
     # 수집한 자료를 df로 만들어서 csv로 저장
     data = {'Rank':rank, 'Cafe':cafe_name, 'Menu':main_menu, 'URL':url_link}
     
     df = pd.DataFrame(data)
     # df
     df.to_csv('./crawl_data/시카고샌드위치가게.csv',sep=',',encoding='utf-8')
     ```

5.  각 가게의 위치 주소와 가격이 각 서브 페이지 링크의 p class="addy" 에 있는 것을 접근 해 저장하기

   - ```python
     req = Request(df['URL'][0], headers={'User-Agent':'Mozilla/5.0'})
     res = urlopen(req)
     soup_tmp = BeautifulSoup(res,'html.parser')
     temp_string = soup_tmp.find('p','addy').get_text() # 가격과 주소
     ```

   - 주소, 가격 추출

     ```python
     temp_stinrg # $10. 2109 W. Chicago Ave., 773-772-0406, theoldoaktap.com
     
     # 띄어쓰기 단위로 스플릿
     temp_string.split() #['$10.', '2109', 'W.', 'Chicago', 'Ave.,', '773-772-0406,', 'theoldoaktap.com']
     
     # 주소는 [1]번 인덱스 부터 뒤에서 2번째 인덱스 전[-2] 까지 리스트 형태를 ' '로 join 해 str으로 만들기
     ' '.join(temp_string.split([1:-2]) # 2109 W. Chicago Ave.,
              
     # 가격 추출, 가격은 temp_string.split()의 0번인덱스고 가격의 마지막이 , 빼고 추출하기 위해 [0][-1]로 추출
     temp_string.split()[0][-1]
     ```

   - 전체 가격과 주소 추출

     ```python
     # 가격과 주소를 저장할 빈 리스트 생성
     price = []
     address []
     
     # DF에 저장된 URL을 활용해 모든 price와 address 추출
     for i in df.index :
         req = Request(df['URL'][i],headers={'User-Agent':'Mozilla/5.0'}) # 객체 생성
         html = urlopen(req) # 요청후 응답 반환
         soup_tmp = BeautifulSoup(html,'html.parser') #bs 객체 생성
         temp_string = soup_tmp.find('p','addy').get_text() # 주소와 가격이 포함된 정보 추출
         price.append(temp_string.split()[0][:-1]) # 추출한 정보에서 가격을 분리해서 list에 저장
         address.append(' '.join(temp_string.split()[1:-2])) # 추출한 정보에서 주소를 분리해서 list에 저장
     
     ```

     

6.  여러 번 반복 접근을 해야 하므로 상태 진행바를 통해서 진행 상태 확인

   - ```python
     from tqdm import tqdm_notebook # 반복문의 반복 요소에 적용시키면 반복요소가 얼마나 진행되었는지 상태바를 표시
     
     price = []
     address = []
     
     for i in tqdm_notebook(df.index) :
         req = Request(df['URL'][i],headers={'User-Agent':'Mozilla/5.0'}) # 객체 생성
         html = urlopen(req) # 요청후 응답 반환
         soup_tmp = BeautifulSoup(html,'html.parser') #bs 객체 생성
         temp_string = soup_tmp.find('p','addy').get_text() # 주소와 가격이 포함된 정보 추출
         price.append(temp_string.split()[0][:-1]) # 추출한 정보에서 가격을 분리해서 list에 저장
         address.append(' '.join(temp_string.split()[1:-2])) # 추출한 정보에서 주소를 분리해서 list에 저장
     
     ```

7.  수집된 각 cafe의 pirce와 address를 df에 추가

   - ``` python
     df['price'] = price
     df['adress'] = address
     ```

   - Rank 컬럼을 index로 설정

     ````python
     df.set_index("Rank", inplace = True)
     ````

   - df를 csv로 저장

     ```python
     df.to_csv('./crawl_data/시카고샌드위치_주소.csv',sep=',',encoding='utf-8')
     ```



## 수집된 주소를 이용해서 각 상점의 위경도 찾아오고 FOLIUM해서 cafe 마커

1. 필요 패키지 import 및 데이터 읽어오기

   - ```python
     import googlemaps 
     import folium
     import pandas as pd
     ## 데이터 읽어오기
     df = pd.read_csv('./crawl_data/시카고샌드위치_주소.csv',index_col=0)
     df.head()
     
     ```

2. 구글 클라이언트 등록키를 이용해서 client 객체 생성

   - ```python
     gmapsKey = 'AIzaSyDaavIigsdXYCOaBIG_Gt-S0mScya5TWbE'
     gmaps = googlemaps.Client(key = gmapsKey)
     ```

3. 상점의 위경도 찾고 DF에 저장

   - 미국 주 이름앞에는 ,가 와야함(두번있어도 상관 없음 단, 없으면 안됨)

     ```python
     # 원래 주소 2109 W. Chicago Ave., 를 2109 W. Chicago Ave.,,Chicago 형태로 해주어야 함.
     target_name = df['address'][1] + "," + "Chicago" 
     
     ```

   - gmaps.geocode 를 이용해 위경도 찾기 

     ```python
     g_info = gmaps.geocode(target_name)
     g_lo = g_info[0].get("geometry")['location']
     g_lo['lat']
     g_lo['lng']
     ```

   - 50개의 위경도 찾아오기

     ```python
     # 50개 위경도 찾아오기
     lat=[]
     lng=[]
     
     from tqdm import tqdm_notebook
     for n in tqdm_notebook(df.index) :
         target_name = df['address'][n] +','+ 'Chicago'
         g_info = gmaps.geocode(target_name)
         g_lo =g_info[0].get("geometry")['location']
         lat.append(g_lo['lat'])
         lng.append(g_lo['lng'])
     
     ```

     

   - 찾으 위경도 DF에 저장하고 csv파일로 저장

     ```python
     df['lat'] =lat
     df['lng'] = lng
     df.to_csv('./crawl_data/시카고샌드위치위경도포함.csv')
     ```

     

4. 전체 cafe의 위치에 Marker 표시하기

   - 마커를 위한 기본 맵 변수 생성

     ```python
     lat_c = df['lat'].mean()
     lng_c = df['lng'].mean()
     map_fin = folium.Map(location=[lat_c,lng_c], zoom_start=11)
     
     ```

   - for문을 통해 모든 카페 위치에 Marker 표시

     ```python
     for n in df.index :
         folium.Marker([df['lat'][n],df['lng'][n]],
                       popup=df['Cafe'][n]).add_to(map_fin)
     
     map_fin
     ```

   - 지도 저장

     ```python
     map_fin.save('./crawl_data/시카고카페.html')
     ```

     





---

----

# 공공데이터 API 활용

```
공공데이터 포털 : 한국 관광공사 지역기반 행사 정보 조회
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057787
```





1.  활용할 api의 endpint와 serviceKey 저장

   - ```python
     import requests
     from bs4 import BeautifulSoup
     
     # url 및 서비스 키
     endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchFestival?'
     serviceKey = '%2BLLqZA1QqtSEtr1Tkwof8BSkf14yznYnRQqU5bo0FydlhEz0L9dqbrjE75%2Ff%2FIPoKqOSJb4hQhtQj%2BTKx3aVjw%3D%3D'
     
     
     ```

   - 요청 변수 파라미터 저장

     ```python
     numOfRows = "50"
     pageNo = "1"
     MobileOS = "ETC"
     MobileApp = "AppTest"
     arrange = "A"
     listYN = "Y"
     areaCode ="1"
     sigunguCode ="4"
     eventStartDate = "20200101"
     ```

2.  요청할 URL은 endpint + paramset 이며 paramset은 요청 변수 파라미터 들을 연결한 주소들.

   - ```python
     paramset = "serviceKey=" + serviceKey +"&" \
                 + "numOfRows=" + numOfRows +"&" \
                 + "pageNo=" + pageNo +"&"  \
                 + "MobileOS=" + MobileOS +"&"  \
                 + "MobileApp=" + MobileApp + "&" \
                 + "arrange="+ arrange + "&" \
                 + "areaCode=" + areaCode + "&"\
                 + "listYN=" + listYN + "&"  \
                 + "eventStartDate=" + eventStartDate
                 
     url = endpoint + paramset
     ```

3.  url을 BeautifulSoup 객체로 저장하기

   - ``` python
     result = requests.get(url) # api 서비스 호출
     bs_obj = BeautifulSoup(result.content, "html.parser")
     
     ```



4. 원하는 정보(title, addr1, tel)가 bs_obj의 item 태그 밑에 있음.

   - ```python
     items = bs_obj.findAll('item')
     
     for item in items :
         try :
             print(item.find('title').text, end=',')
             print(item.find('addr1').text, end=',')
             print(item.find('tel').text)
         except :
             print(' No data ')
     ```

   - 



---

---

# 네이버 검색 API

```
네이버 블로그에 강남역 검색 API
```



1. json() 형태로 검색결과 불러오기

   - 필요한 패키지 import

     ```python
     import os
     import sys
     import urllib.request
     ```

   - 네이버 개발자 센터에서 본인의 API ID와 secret을 변수에 저장

     ```python
     ## id와 key 변수에 저장
     client_id = "my_id"
     client_secret = "my_secret"
     ```

   - 원하는 검색어 utf-8로 인코딩해 변수에 저장

     ```python
     enc_text = urllib.parse.qoute("강남역")
     ```

   - url 작업 및 헤더 작업 후 서버에 요청

     ```python
     # json 형태의 기본 url_base
     url_base = 'https://openapi.naver.com/v1/search/blog?query='
     
     # 검색 결과 100개로 늘리기
     
     search_ = "&display=100"
     
     # url_base에 원하는 검색어 변수를 연결해 url 생성
     url = url_base + enc_text + search_ 
     
     
     
     #get()안에 url과 headers를 포함 할 수 있음
     result = requests.get(url,
           headers={"X-Naver-Client-Id":client_id,
                    "X-Naver-Client-Secret":client_secret})
     ```

   - 검색된 결과를 json 형태로 읽어오기

     ```python
     json_obj = result.json()
     
     ```

     

2. 불러온 json() 형태에서 특정 속성값 추출

   - 제목 추출

     ```python
     # 찾고자 하는 제목 데이터는 json의 items 밑에 title에 있음
     # 제목에 불필요한 단어를 제거(<b></b> 같은거)
     for item in json_obj["items"] :
         print(item["title"].replace("<b>","").replace("</b>",""))
         
     ```

     

