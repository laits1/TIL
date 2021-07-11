# anaconda 설치
1. 아나 콘다 다운로드 [Anaconda Download](https://www.anaconda.com/products/individual)  
2.  ![](C:\Users\SDG\Documents\TIL\TIL\pandas\md_pic\anaconda down1.png)체크 후 설치 진행후 설치 완료





## Jupyter notebook 홈디렉터리 변경



1.  Jupyter Notebook 실행 바로가기의 속성
2.  대상에서 맨 끝에 있는 "%USERPROFILE%/" 삭제
3.  Anaconda Prompt 관리자 권한으로 실행
4.  jupyter notebook --generate-config 입력
5. C:\Users\본인 컴퓨터이름\\.jupyter 폴더에 있는 jupyter_notebook_config.py 수정
6. c.NotebookApp.notebook_dir = '변경하고 싶은 홈 디렉터리' 로 설정 후 저장

 
