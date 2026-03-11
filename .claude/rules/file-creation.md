# 문제 파일 생성 규칙

"폴더랑 파일 생성해줘" 요청 시 **coding-test-playground** 기준으로 생성.

## 경로 패턴

```
leetcode/p{번호}_{문제명_snake_case}/p{번호}-{문제명-kebab-case}.py
```

예시:
- `leetcode/p242_valid_anagram/p242-valid-anagram.py`
- `leetcode/p70_climbing_stairs/p70-climbing-stairs.py`

## 파일 템플릿

```python
"""
TC: O(...)

SC: O(...)

풀이:
...
"""

from typing import *


class Solution:
    def methodName(self, ...):
        pass
```

## 주의

- leetcode-study repo(`/Users/river/Developer/playground/leetcode-study`)에 생성하지 않음
- 풀이 완료 후 leetcode-study에 별도로 `riveroverflows.py` 파일 생성
