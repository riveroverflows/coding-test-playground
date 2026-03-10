"""
TC: O(n+m)
for char in s: O(n)
for char in t: O(m)
최종: O(n+m)

SC: O(n)
counter: 최악일 때 O(n)
char: O(1)
최종: O(n)

풀이:
입력값 s를 문자 별로 몇개씩 있는지 확인
입력값 t를 순회하면서 입력값 s의 문자열과 반복 횟수가 동일한지 확인
"""

from typing import *
import sys

input = sys.stdin.readline



def isAnagram(s: str, t: str) -> bool:
    counter = dict()
    for char in s:
        if char == '\n':
            continue
        if char not in counter:
            counter[char] = 0
        counter[char] += 1

    for char in t:
        if char == '\n':
            continue

        if char not in counter:
            return False

        if counter[char] == 1:
            counter.pop(char)
            continue

        counter[char] -= 1

    return True if not counter else False



s = input()
t = input()
print(isAnagram(s, t))