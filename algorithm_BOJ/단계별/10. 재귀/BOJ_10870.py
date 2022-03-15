#피보나치 수 5

n = int(input())
fn2 = 0
fn1 = 1
fn = 0

if n == 1:
    print(1)
else:
    for i in range(n-1):
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn

    print(fn)
