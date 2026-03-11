"""
TC: O(n+m)
if len(s) != len(t): O(1)
ss = set(s): O(n)
for c in ss: O(1)
  s.count(c): O(n)
  t.count(c): O(m)
최종: O(n+m)

SC: O(n)
ss = set(s): 최악일 때 O(n)
for c in ss: O(1)
최종: O(n)

풀이:
s와 t 길이가 다르면 anagram 아니므로 False로 early return
set으로 s의 중복 문자열 제거
set을 순회하면서 각 문자열이 s와 t에 몇개씩 있는지 확인 후 다르면 False로 early return
early return 없이 순회가 끝났다면 anagram
"""

from typing import *
import sys

input = sys.stdin.readline


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    ss = set(s)
    for c in ss:
        if s.count(c) != t.count(c):
            return False

    return True



s = input()
t = input()
print(isAnagram(s, t))