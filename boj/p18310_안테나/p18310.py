"""
집의 수: N(1 <= N <= 200,000)
공백으로 구분된 N채의 집의 위치 (1 <= 100,000)

4
5 1 7 9

0 4 2 4  10
4 0 6 8  18
2 6 0 2  10
4 8 2 0  14

result
가장 작은 합을 저장할 변수 min
N 만큼 반복
    i에 안테나가 설치된다고 가정, 여기서 다른 집과의 거리 구해서 i sum에 더하기.(여기서 n-1번씩 반복)
        i sum을 min 연산해서 min에 저장
        저장될 때 기존 min이랑 같으면 i를 min 연산해서 result에 저장
시간초과..

중앙값을 찾아서 풀어야함.
총 개수 // 2 이렇게 찾을 수 있는데 값이 여러 개일 경우 가장 작은 값을 리턴해야함

총 개수가 홀수면 중앙값도 하나라서 문제 없음
총 개수가 짝수면 중앙값이 두개인데 그 중 작은 값을 리턴해야함
계산해보면 n // 2도 중앙값, (n-1) // 2도 중앙값
더 작은 값을 리턴해야하므로 (n-1)//2 활용해서 풀이 함
"""

import sys

input = sys.stdin.readline

n = int(input())
house_indexes = list(map(int, input().split()))
house_indexes.sort()

print(house_indexes[(n - 1) // 2])
