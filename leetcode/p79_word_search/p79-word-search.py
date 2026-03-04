import json
from typing import List



def exist(board: List[List[str]], word: str) -> bool:
    

board = json.loads(input())
word = input()
print(exist(board, word))