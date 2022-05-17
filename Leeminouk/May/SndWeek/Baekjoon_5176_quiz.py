# 문제
# 이번 ACM-ICPC 대회의 자리는 참가자들이 직접 정한다. 참가자들은 예비 소집일에 자신이 원하는 자리를 미리 정해놓았고, 대회 당일에 어제 적어놓은 자리에 앉으면 된다. 여러명이 같은 자리를 적어논 경우에는, 먼저 도착한 사람이 그 자리에 앉게되고, 앉지 못한 사람은 대회에 참가할 수 없다.

# 각 사람이 선호하는 자리가 주어졌을 때, 대회에 참가하지 못하는 사람의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어 있다.

# 첫째 줄에 참가자의 수 P와 자리의 수 M이 주어진다. (1 ≤ P, M ≤ 500) 다음 P개 줄에는 각 참가자가 원하는 자리가 주어진다. 자리는 1번부터 M번까지 있다. 입력으로 주어지는 참가자가 도착하는 순서이다.

# 출력
# 각 테스트 케이스에 대해서, 대회에 참가하지 못하는 사람의 수를 출력한다.

import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    cannot_test = 0

    player, seat = list(map(int, sys.stdin.readline().split()))
    seats = {a:0 for a in range(1, seat + 1)}

    for _ in range(player):
        pos = int(sys.stdin.readline())

        if seats[pos] == 0:
            seats[pos] = 1

        else:
            cannot_test += 1

    print(cannot_test)
