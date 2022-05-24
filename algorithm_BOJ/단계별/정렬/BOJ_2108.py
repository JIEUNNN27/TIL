#통계학
#collections 모듈의 counter클래스 사용하기
#최빈값이 가장 어려움...

from collections import Counter
N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

#산술평균
print(int(sum(nums)/N))

#중앙값
s_nums = sorted(nums)
i = int((N-1)/2)
print(s_nums[i])

#최빈값 -?????????????????????????????
cnt = Counter(nums).most_common()




#범위
print(max(nums)-min(nums))