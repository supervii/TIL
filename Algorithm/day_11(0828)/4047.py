import sys
sys.stdin = open("4047.txt", "r")
T = int(input())
for tc in range(1, T+1):
    # print(tc)
    deck = ['S', 'D', 'H', 'C']
    arr = [13]*4
    card = input()
    check = [[] for _ in range(4)]

    for i in range(0, len(card), 3):
        # print(card)
        card_num = int(card[i+1] + card[i+2])
        card_idx = deck.index(card[i])
        if card_num not in check[card_idx]:
            check[card_idx].append(card_num)
            arr[card_idx] -= 1
        else:
            print('#{} ERROR'.format(tc))
            break
    else:
        print('#{} {}'.format(tc, ' '.join(map(str,arr))), )
