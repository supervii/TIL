# LED 스위치 켜기
# N개의 방이 일렬로 늘어져 있고 각 방에는 전원을 켤수 있는 스위치가 있다. 방의 번호는 1번부터 시작한다. 특정
# 방의 스위치를 조작하면 해당 방 번호의 배수에 해당하는 방들도 조작된다. 불을 켜야 하는 방들의 정보가 주어질 때,
# 모두 꺼져있는 상황에서 주어진 정보대로 불을 켜기 위해 스위치를 조작해야하는 최소 횟수를 구하라.
# 예를 들어 6개의 방이 1번부터 꺼짐(0), 켜짐(1), 켜짐(1), 꺼짐(0), 꺼짐(0), 켜짐(1)이라면 2번방, 3번방, 4번방,
# 6번방의 스위치 네개를 조작하면 되므로 답은 4이다.
import sys; sys.stdin = open('8444.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0]*N
    room = list(map(int, input().split()))
    cnt= 0

    for i in range(N):
        if room == arr:
            break
        else:
            if room[i] != arr[i]:
                cnt += 1
                for j in range(i,N,i+1):
                    if arr[j]:
                        arr[j] = 0
                    else:
                        arr[j] = 1
    print('#{} {}'.format(tc, cnt))






