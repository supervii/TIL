def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0]* MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncanidates = construct_candidates(a, k, input, c)
        for i in range(ncanidates):
            a[k] = c[i]
            backtrack(a, k, input)
