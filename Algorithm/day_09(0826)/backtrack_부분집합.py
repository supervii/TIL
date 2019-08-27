# 부분집합 백트랙킹

def backtrack(a,k, input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES
    if k == input:
        process_solution(a,k)
    else:
        k += 1
        ncanidates = construct_candidates(a,k,input,c)
        for i in range(ncanidates):
            a[k] =c[i]
            backtrack(a, k, input)

def construct_candidates(a,k, input, c):
    c[0] =True
    c[1] = False
    return 2

def process_solution(a,k):
    # Sum = []
    print('(', end='')
    for i in range(k+1):
        if a[i]:
            # Sum.append(i)
            print(i, end='')
    print(')')
    # if sum(Sum) == 10:
        # print(Sum)



MAXCANDIDATES = 100
NMAX = 100
a= [0]*NMAX
backtrack(a,0,10)


