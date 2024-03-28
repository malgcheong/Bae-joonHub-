#9655
# n이 1일때, sk
# n이 2일때, cy
# n이 3일때, sk
# n이 4일때, cy
# n이 5일때, sk
# n이 6일때, cy

# 수학과 박진용님 조언 덕분에 제대로 안 사실
# 홀수 두개를 더하면 짝수이다.
# 홀수 1,3을 뽑는 문제이니 결국 사라지는 숫자는 (1,1),(1,3) 즉 짝수 갯수만큼만 준다.
# n이 4이면 두번째로 집어드는 사람이 이기고 1,1,1,1 또는 1,3
# n이 5이면 처음 집어드는 사람이 이긴다. 1,1,1,1,1 또는 1,3,1

import sys

n = int(sys.stdin.readline())

if n % 2 == 0:
    print("CY")
elif n % 2 != 0:
    print("SK")

