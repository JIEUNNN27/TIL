def solution(n, m):
    answer = []
    n_list = []
    m_list = []
    yak_list = []
    bea_list = []
    # 약수 찾기
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)

    for i in range(1, m+1):
        if m % i == 0:
            m_list.append(i)

    # 최대공약수
    for i in n_list:
        for j in m_list:
            if i == j:
                yak_list.append(i)
    answer.append(yak_list[-1])

    # 최소공배수
    for i in n_list:
        for j in m_list:
            bea = i*j
            if bea % n == 0 and bea % m == 0:
                bea_list.append(bea)
    answer.append(bea_list[0])

    return answer
