#숫자의 개수
numl = [int(input()) for _ in range(3)]
num = numl[0] * numl[1] * numl[2]

nums = list(str(num))

print(nums.count('0'))
print(nums.count('1'))
print(nums.count('2'))
print(nums.count('3'))
print(nums.count('4'))
print(nums.count('5'))
print(nums.count('6'))
print(nums.count('7'))
print(nums.count('8'))
print(nums.count('9'))
