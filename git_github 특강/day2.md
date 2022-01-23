[TOC]



# 20220106 Git 특강 2일차 TIL

:smiley: 어제 내용 복습

:smiley: git hub 프로필 만들기



# 7. .gitignore

:star:gitignore : 특정 파일 혹은 폴더에 대해 git이 버전 관리를 하지 못하도록 지정하는 것

#### (1) .gitignore에 작성하는 목록

* 민감한 개인 정보가 담긴 파일
* 운영체제에서 활용되는 파일
* IDE 혹은 vscode 등에서 활용되는 파일
* 개발언어 혹은 프레임워크에서 사용되는 파일
* [.ignore](https://www.toptal.com/developers/gitignore) 여기서 개발 언어별로 찾을 수 있다.



#### (2) .gitignore 작성 시 주의사항

- 이름을 `.gitignore`로 작성하기.
- `.gitignore` 파일은 `.git` 폴더와 동일한 선상에 설치
- 반드시 `git add` 하기 전에 `.gitignore` 작성하기



# 8. clone, pull

``` 
대략적인 과정 요약
* 가정
	- 이미 레포지토리에 커밋이 올라가 있다.
	- pull, push하는 권한이 있다
* clone
	- 빈 폴더(상위 폴더에 git이 없어야 함)에 clone
	- git clone <url> -> 새로운 폴더를 만들면서 clone
	- giot clone <url> . -> 현재 폴더에 그대로
* Do something and push commit
	- 원격 저장소가 원본 저장소보다 상위 버전이 된다.
*pull
	- 원본 로컬 저장소에서 원격 저장소의 코밋을 pull함
	- git pull <저장소 이름> <브랜치 이름>
		git pull origin master
```



#### (1) git clone

* 원격 저장소의 커밋 내용을 모두 가져와 로컬 저장소를 생성하는 명령어
* `git clone <원격 저장소의 주소>`  또는 `git clone <원격 저장소의 주소> .`
* git clone을 통해 생성된 로컬 저장소는 `git init` 과 `git remote add`가 이미 실행된 상태.



#### (2) git pull

- 원격 저장소의 변경 사항을 가져와 로컬 저장소를 업데이트하는 명령어
- 로컬 저장소와 원격 저장소의 내용이 완전 일치하면 git pull을 해도 변화가 일어나지 않음
- `git pull <저장소 이름> <브랜치 이름>`

​	

#### (3) CONFLICT 해결하기

```
* 실습
	1. 원본 디렉토리에서 a.txt 변경 -> commit -> push
	2. clone 디렉토리에서 a.txt 변경 -> commit -> pull
	3. vscode 등을 이용하여 conflict 해결하기
	4. 원격 저장소에 push 하기
	5. 원본 디렉토리에서 원격 저장소로부터 pull 해오기
```





---

#### 대략적인 과정 정리

1. git init

2. .gitignore 만들기

3. git add

4. git commit

5. 레포 만들기

6. remote add <name> <url>

7. push

   ​	이 다음 부터는 add, commit, push 하기
