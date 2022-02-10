#평균은 넘겠지
case = int(input())


po = [[int(i) for i in input().split()] for _ in range(case)]
  
for i in po:
    mean1 = sum(i[1:])/i[0]
    mean_over = [ii for ii in i[1:] if ii>mean1]
  
    print('%0.3f'%((len(mean_over)/i[0])*100)+'%')
    

    


