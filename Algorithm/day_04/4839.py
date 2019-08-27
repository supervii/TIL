import sys

sys.stdin = open("4839.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    # print(P, Pa, Pb)

    lo = 1
    hi = P
    a_count = 0
    b_count = 0


    while lo <= hi:

        mid_a = (lo + hi) // 2
        # print(lo, hi, mid_a, Pa)
        a_count += 1
        if mid_a == Pa:
            # print(mid_a)
            break
        # print(mid_a, Pa)

        elif mid_a > Pa:
            hi = mid_a
            # print(mid_a)

        else:
            lo = mid_a
            # print(mid_a)

    # print(a_count)

    lo = 1
    hi = P
    while lo <= hi:

        mid_b = (lo + hi) // 2
        # print(lo, hi, mid_b, Pb)
        b_count += 1
        if mid_b == Pb:
            # print(mid_b)
            break
        elif mid_b > Pb:
            hi = mid_b
        else:
            lo = mid_b



    if a_count > b_count:
        print('#{} B'.format(test_case))
    elif a_count < b_count:
        print('#{} A'.format(test_case))
    else:
        print('#{} 0'.format(test_case))
