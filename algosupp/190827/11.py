import sys; sys.stdin =open('1.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    pan = [[0]*