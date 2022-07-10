def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        i_list=[]
        for j in range(len(arr1[0])):
            i_list.append(arr1[i][j]+arr2[i][j])
        answer.append(i_list)    
    
    #이거 안됨
    #import numpy as np
    #array_sum_np = np.array(arr1)+np.array(arr2)
    
    # for i in range(len(arr1[0])):
    #     for j in range(len(arr1)):
    #          answer.append([arr1[j][i] + arr2[j][i]])
    

    
    #이거 안됨
    # for i in range(len(arr1)):
    #     for j in range(len(arr1[0])):
    #         answer.append([arr1[i][j] + arr2[i][j]])

    return answer