#빠른 A+B
#sys 이용하기
import sys

t =  int(sys.stdin.readline())


for i in range(t):
    a, b =  map(int, (sys.stdin.readline().split()))
    print(a+b)