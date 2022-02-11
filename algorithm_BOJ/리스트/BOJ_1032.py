#명령 프롬프트
n = int(input())


for i in range(n):
    if i == 0:
        first_file = list(input())
    else:
        file_name = list(input())
        for f in range(len(first_file)):
            if first_file[f] != file_name[f]:
                first_file[f] = "?"

print(*first_file, sep='')



