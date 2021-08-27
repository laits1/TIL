# GCP

[GCP 시작하기](https://cloud.google.com/gcp/getting-started?authuser=2)

## 1. Linux VM 만들기

```
VM 인스턴스를 만들고, 연결하고, 삭제합니다.
제품: Google Compute Engine
```



### 1. **시작 하기 전에**

1) [프로젝트 생성](https://console.cloud.google.com/projectselector2/home/dashboard?authuser=2&_ga=2.24592441.2064428097.1630058388-307852693.1629880764&_gac=1.150603204.1629884416.CjwKCAjw1JeJBhB9EiwAV612y31Ubb2W14YX8c9eQNH80kOlKwjhPBNI_QtVpBe3jRqqxYuNBCSoERoCEy0QAvD_BwE)에서 새 프로젝트 만들기

<img src="pic/make_new_pj.png" style="zoom:60%;" />

2. [Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview?authuser=2&_ga=2.201845778.2064428097.1630058388-307852693.1629880764&_gac=1.86566250.1629884416.CjwKCAjw1JeJBhB9EiwAV612y31Ubb2W14YX8c9eQNH80kOlKwjhPBNI_QtVpBe3jRqqxYuNBCSoERoCEy0QAvD_BwE) 사용 설정

<img src="pic/engine_API.png" style="zoom:60%;" />



### 2. **Linux VM 인스턴스 만들기 **

1. Cloud Console에서 [VM 인스턴스](https://console.cloud.google.com/compute/instances?authuser=2&_ga=2.128976655.2064428097.1630058388-307852693.1629880764&_gac=1.57426520.1629884416.CjwKCAjw1JeJBhB9EiwAV612y31Ubb2W14YX8c9eQNH80kOlKwjhPBNI_QtVpBe3jRqqxYuNBCSoERoCEy0QAvD_BwE&project=my-first-vm-324009&folder=&organizationId=) 페이지로 이동

2. **인스턴스 만들기** 클릭

3. **부딩 디스크** 섹션에서 **변경**을 클릭하여 부팅 디스크 구성을 시작

4. **Public images**탭에서 **Ubuntu 20.04 LTS** 선택

   <img src="pic/booting_disk.PNG" style="zoom:60%;" />

5. **선택** 클릭

6. **방화벽** 섹션에서 **HTTP 트래픽 허용** 선택

   <img src="pic/http_traffic.png" style="zoom:60%;" />

7. **만들기** 클릭하여 인스턴스 만들기





### 3. VM 인스턴스에 연결



1. Cloud Console에서 **[VM 인스턴스](https://console.cloud.google.com/compute/instances?authuser=2&_ga=2.256190216.2064428097.1630058388-307852693.1629880764&_gac=1.57732824.1629884416.CjwKCAjw1JeJBhB9EiwAV612y31Ubb2W14YX8c9eQNH80kOlKwjhPBNI_QtVpBe3jRqqxYuNBCSoERoCEy0QAvD_BwE&project=my-first-vm-324009&folder=&organizationId=)** 페이지로 이동

2. 가상 머신 인스턴스 목록에서연결할 인스턴스 행의 **SSH**를 클릭

   <img src="pic/start_VM.png" style="zoom:60%;" />





---

## 2. 파일 저장 및 공유

```
버킷을 생성하고, 파일을 업로드 및 공유하고, 폴더로 정리합니다.
제품: Google Cloud Storage
```



### 1. 버킷 만들기

- 버킷은 Cloud Storage에서 데이터를 보관하는 기본 컨테이너

1. Google Cloud Console에서 Cloud Storage **[브라우저](https://console.cloud.google.com/storage/browser?authuser=2&_ga=2.28648255.2064428097.1630058388-307852693.1629880764&_gac=1.151078603.1629884416.CjwKCAjw1JeJBhB9EiwAV612y31Ubb2W14YX8c9eQNH80kOlKwjhPBNI_QtVpBe3jRqqxYuNBCSoERoCEy0QAvD_BwE)** 페이지로 이동

2. **버킷 생성**을 클릭하여 다음과 같이 버킷 생성 

   - 버킷의 고유한 **이름** 입력
   - 위치유형 **Multi-Region**, 위치 **Asia**

   - 기본 스토리지 클래스 **Standard** 
   - 객체 제어 엑세스 방식 : **균일한 엑세스 제어**



### 2. 버킷에 객체 업로드

1.  Cloud Storage **[브라우저](https://console.cloud.google.com/storage/browser?authuser=2&_ga=2.28648255.2064428097.1630058388-307852693.1629880764&_gac=1.151078603.1629884416.CjwKCAjw1JeJBhB9EiwAV612y31Ubb2W14YX8c9eQNH80kOlKwjhPBNI_QtVpBe3jRqqxYuNBCSoERoCEy0QAvD_BwE)** 페이지에서 앞서 만든 버킷의 이름 클릭
2. **객체** 탭에서 **파일 업로드** 클릭
3. 파일 업로드



### 3. 객체 다운로드

1. 버킷에서 객체를 클릭하고 **다운로드** 클릭



### 4. 객체 공유

- 버킷에 대한 공개 액세스를 허용하고 이미지에 대해 **공개적으로 액세스 가능한 URL**을 만들기

1. 파일 목록 위에 있는 **권한** 탭을 클릭
2. 뷰가 **구성원**으로 설정되어 있는지 확인. **추가**를 클릭하면 구성원 추가 창이 나타난다.
3. **새 구성원** 상자에 ``allUsers``를 입력
4. **역할 선택** 드롭다운에서 **Cloud Storage > 저장소 객체 뷰어**를 선택

5. **저장** 클릭
6. **이 리소스를 공개로 설정하시겠습니까?** 창에서 **공개 액세스 허용**을 클릭



### 5. 버킷에서 공개 액세스 삭제 및 공개 공유 중지

1. 객체 목록 위에 있는 **권한** 탭을 클릭
2. **구성원** 열에서 **allUsers**가 나열된 항목을 찾고, 해당 항목의 체크박스를 선택
3. **삭제**를 클릭
4. **allUsers 삭제** 창에서 **확인**을 클릭
5. **객체** 탭에서 이지미에 더 이상 **URL 복사** 버튼이 없다는 것을 확인