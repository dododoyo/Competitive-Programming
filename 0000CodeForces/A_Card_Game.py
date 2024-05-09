rank_map = {'6': 0, '7': 1, '8': 2, '9': 3,
            'T': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8}
suit_map = {'S': 0, 'H': 1, 'D': 2, 'C': 3}

tramp_suit = input()
card1,card2 = input().split()

if card1[1] == tramp_suit and card2[1] == tramp_suit or card2[1] == card1[1]:
    print('YES' if rank_map[card2[0]] < rank_map[card1[0]] else 'NO')
elif card1[1] == tramp_suit:
    print("YES")
else:
    print("NO")
    