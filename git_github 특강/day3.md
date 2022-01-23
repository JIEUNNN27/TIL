[TOC]

# 20220107 Git-Github 특강 3일차

# 1. Branch

```
실습 과정 요약
	branch 폴더 만들기, txt 파일 만들기
	branch 폴더 안에서 git init, git add, git commit		[master]
	
	새로운 branch 만들기 git branch <branch name> or git switch <branch name>		[new branch]
	새로운 branch로 이동(git switch <new branch>)해서 파일 수정. 변경하기
	git add, git commit
	
	master branch로 이동해서 파일 수정, 변경하기		[master]
	git add, git commit
	git merge <new branch>
	여기서 conflict가 일어나면 해결하기 (예: code a.txt)
	git add, git commit(commit 할 때 메시지 안 남겨도 자동으로 merge된것 확인할 수 있다.) 
```

### (1) branch

- branch?
  - 독립적으로 어떤 작업을 진행하기 위한 개념.
  - 여러 개발자들이 동시에 다양한 작업을 할 수 있게 만들어 주는 기능
  - 분리된 작업 영역에서 변경된 내용은 나중에 원래 버전과 비교해 하나의 new 버전으로 만들 수 있다.
  - ![branch](../../%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B5%AD%EB%B9%84%20%EA%B5%90%EC%9C%A1/20220107%205%EC%9D%BC%EC%B0%A8%20%EC%A0%95%EB%A6%AC/aaaaaaaaa-16415349636962.png)



- branch 만들기

  - `git branch <branch 이름>`

  

- branch 확인

  - 'git branch'

  

- branch 이동

  - `git switch <branch 이름>`
  - `git checkout <branch 이름>`
  - 만들면서 이동
    - `git switch -c <branch 이름>`



- branch 지우기

  - `git branch -d <branch 이름>`
  - `git branch -D <branch 이름>`

  
### (3) Branch merge  


  - 기준이 될 branch에서
    - git merge <합칠 브랜치 이름>
    
      
    
   1. 두 브랜치 모두에서 수정사항이 있지만, 겹치지 않은 상황
             - 3-way merg
   2. 두 브랜치 모두에서 수정사항이 있고, 겹친 상황
             - Conflict 해결 후 commit






# 2. Restore, Commit 수정, diff

### (1) Restore

- git restore 

  - 가장 최근 기록(Staging area or Commit)으로 돌아온다.
  - 뒤로 가기의 의미. 파일을 예전 기록으로 돌아가게 한다.
  - `git restore <파일명>`

- git restore --staged
  - Staging area에서 내려준다

  - `git restore --staged <파일명>`

:smiley: git rm --cached 

  - untracked 상태로 바꿔줌.
  - `git rm --cached <파일명>`
  - `git rm -r --cached .`  : 모든 파일을 untracked 상태로 바꿔줌.



### (2) Commit 수정

- commit --amend
  - 파일 수정이 없으면 코밋 메시지만 재작성 해준다.
  - 파일 수정이 있으면 그것을 반영해 코밋을 덮어씌운다.
  - `git commit --amend`



### (3) diff

- diff
  - 워킹디렉토리와 가장 최근 기록(Staging area or Commit)의 차이를 보여준다.
  - `git diff`
- diff --staged
  - Staging area 와 Commit의 차이를 보여준다.
  - `git diff --staged`

​		

:smiley:중간중간에 `git status`, `git log --oneline`(commit 확인) 확인하면서 하기!





# 3. Reset, Revert

`<Commit ID>`

​	`commit id`는 사진의 노란색과 같이 `git log --oneline` 했을 때 나오는 commit ID를 이용한다.(*네 자리 까지만 입력해도 됨*)

![image-20220107155923660](../../%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B5%AD%EB%B9%84%20%EA%B5%90%EC%9C%A1/20220107%205%EC%9D%BC%EC%B0%A8%20%EC%A0%95%EB%A6%AC/image-20220107155923660.png) 



### (1) Reset

- Reset
  - 과거에 했던 commit으로 되돌리기


- --soft
  - commit만 하면 원 상태로 돌아올 수 있다
  - `git reset --soft <Commit ID>`

- --mixed
  - add, commit까지 하면 원 상태로 돌아올 수 있음
  - `git reset --mixed <Commit ID>`
- --hard
  - 전부 리셋
  - `git reset --hard <Commit ID>`



​	:smiley: `git reflog` : commit 리셋 기록을 확인



### (2) Revert

- reset 이랑 다른점
  - revert는  commit을 남긴다.
- `git revert <Commit ID>`	
  - 해당 코밋을 취소
- `git revert <Commit ID 1>..<Commit ID 2>` 
  - <Comit ID 1>는 불포함한 채로 여기부터 <Comit ID 2> 까지 revert 하기.





# 4. 협업의 방식

### (1) Git Flow

- branch 이용하기

### (2) Fork and Pull Model

- open source 이용하기

### (3) Shared Repository Model

- Repository 공유
- Repository settings -> manage access





# 5. Profile page 만들기

- HTML 양식.

- 새 폴더에 [양식 다운로드](https://startbootstrap.com/), HTML을 VScode를 이용해서 수정하기
- 이 폴더에서 git hub 에서 Repository 만들고 연결해서 push까지 하기
- 해당 Repository Settings - Pages - master - /(root) - save 