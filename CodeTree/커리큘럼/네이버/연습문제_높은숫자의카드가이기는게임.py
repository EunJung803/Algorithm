N = int(input())
B_cards = list(int(input()) for _ in range(N))

all_cards = list(i for i in range(1, 2*N+1))

B_cards.sort()

A_cards = []

# in을 안쓰고 A의 카드 리스트를 채우려고 시도했으나... 실패
b_set = set(B_cards)        # in 연산의 시간초과 해결을 위하여 set로 변경

for i in range(len(all_cards)):
    if(all_cards[i] not in b_set):
        A_cards.append(all_cards[i])

A_cards.sort()      # 정렬해서 오름차순으로 비교해야 최댓값을 구할 수 있음

ans = 0
j = 0

for i in range(N):
    if (A_cards[i] > B_cards[j] and j < N):     # 현재 A의 카드가 B를 이긴다면 -> 정답 추가, 다음 B의 카드 비교
        ans += 1
        j += 1

print(ans)