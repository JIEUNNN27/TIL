[TOC]



# 20220105 Git 특강 1일차 TIL



# 1. Intro

## Git

- 분산 버전 관리 시스템 

  * 코드의 버전을 관리하는 도구
  * 개발 과정 파악 가능
  * 이전 버전과의 변경 사항 비교 및 분석
  * ***백업, 복구 협업***이 용이하다**
  
- **Git 설치** 

  - [git 설치](https://git-scm.com/)

  

## Git hub

- 깃 기반의 저장소 서비스
- 포트폴리오를 만들 수 있다.
- 실제 많은 개발자들이 사용하고 있다.





# 2. CLI 기초

## CLI(Command Line Interface)

- 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- **CLI**를 사용하는 이유

  - GUI보다 단계가 간단하다.
  - GUI보다 많은 기능을 사용할 수 있다.

- **Git Bash**를 사욯하는 이유

  - 명령어의 통일을 위해서(*Git bash는 일종의 번역기*)
  - UNIX 계열 운영체제의 명령어를 더 많이 쓰기 때문

- #### **터미널 명령어**

  - ```
    $ mkdir folder				#폴더 만들기
    $ touch text.txt			#파일 생성하기, 확장자 입력해야 한다
    $ ls						#폴더/파일 목록
    $ mv text.txt folder		#text.txt를 folder 폴더 안에 넣을 때
    $ mv text1.txt text2.txt 	#이름 바꾸기
    $ cd folder					#folder 폴더로 이동
    $ cd ..						#상위 폴더로 이동
    $ rm						#삭제
    $ vi a.txt					#기존파일 수정 or 파일 생성하면서 수정
    	i	글쓰기
    	esc + : + wq	저장
    ```
    
  - 유용한 단축기
  
    - tab : 자동 완성
    - ctrl + a : 커서가 맨 앞으로 이동
    - ctrl + e : 커서가 맨 뒤로 이동
    - ctrl + l : 터미널 화면 청소
    - ctrl + insert : 복사
    - shift + insert : 붙여넣기





# 3. Visual Studio Code

- **Visual Studio Code 설치**
  - [Vscode 설치](https://code.visualstudio.com/docs/?dv=win)
- **폰트 설치**
  - [Fira code](https://github.com/tonsky/FiraCode)





# 4. Markdown

- Typora 설치

  - [Typora 설치](https://typora.io/windows/dev_release.html)

- Markdown이란?

  - 일반 텍스트 기반의 경량 Markup 언어
  - .md 확장자를 가지며, 개발과 관련된 많은 문서는 Markdowm 형식
  - HTML, Google Colab 등에서 쓰인다.

- Markdown 문법

  - ```markdown
    * 제목 (크기가 6종류 있다, ctrl + 1~6 해도 가능)
    	# 제목
    	## 제목
    	### 제목
    	#### 제목
    	##### 제목
    	###### 제목
    ```

  - ```markdown
    * 목록(List)
    	1. 순서 없는 목록
    		- * +
    	2. 순서 있는 목록
    		1. 2. 3.
    	3. tab키를 이용히 들여쓰기도 사용 가능
    ```

  - ```markdown
    * 강조
    	1. 기울임
    		*글자* 혹은 _글자_
    	2. 굵게
    		**글자** 혹은 __글자__
    	3. 취소선
    		~~글자~~
    ```
    
  - ```markdown
    * 코드
    	1. 인라인 코드
    		`inline code`
    	2. 블록 코드
    ```
  
  - ```markdown
    * 링크 (Links)
    	[표시할 글자](이동할 주소)
    
    * 이미지 (Images)
    	![대체 텍스트](이미지 주소)
    ```
  
  - ```markdown
    * 인용 (Blockquote)
    	> 인용문
    	>> 중첩된 인용문
    	>>>
    	>>>>
    	>>>>>
    	.
    	.
    	.
    ```
  
  - ```markdown
    * 표 (Table)
    	- 파이프(|)와 space키( )를 이용해서 행과 열을 구분
    	- Ctrl + T를 통해서 쉽게 표 생성 가능
    	- 행을 늘릴 때는 Ctrl + enter
    ```
  
  - ```markdown
    * 수평선 (Horizontal Rule)
    	- 구분선을 생성
    	- - or * or _ 을 3번 이상 연속으로 작성한다
    ```
  
  - ```
    [TOC] : 목차, 링크를 제공해 준다
    ```
  
    



# 5. Git 초기 설정

- 최초 한 번만 설정, 컴퓨터 변경 시 다시 설정 해야 한다

- ```
  $ git config --global user.name <username>		#username 등록
  $ git config --global user.name					#username 확인
  $ git config --global user.email <email>			#email 등록
  $ git config --global user.email		#email 확인
  ```





# 6. Git - Github 연결 (Repository)

##### :slightly_smiling_face:Repository 연결할때는 한번만 하는 작업

Github에서 Repository 생성

```
$ git init										#git 시작
$ git remote add origin <git repository url>	#repository 연결
```



##### :slightly_smiling_face:파일 수정, 생성 할때마다 해야하는 작업

```
$ git add .								#모든 파일 staging area에 올리기
$ git add <file_name>					#파일 staging area에 올리기
$ git commit -m '<commit message>'		#커밋 message 작성
$ git push origin master				#github로 밀어내기
$ git push -u origin master				#이후에는 git push라고만 작성해도 push가 됨
```

* 상태 확인 : `git status`, `git log`
