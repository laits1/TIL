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

       

