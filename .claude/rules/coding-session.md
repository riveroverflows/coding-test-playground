# 코딩 세션 시작 규칙

"코테풀자" 요청 시 아래 순서로 진행.

## Step 1. 이번 주차 계산

- DaleStudy 7기: 시작일 **2026-03-01** (일요일)
- 주차 기준: **일요일 ~ 토요일**
- 계산: `(현재 날짜 - 2026-03-01) / 7 + 1` → Week N
- 문제 스케줄은 4기 이후 고정이므로, Projects 보드에서 **Week N** 문제를 확인

## Step 2. 이번주 문제 확인

아래 URL을 WebFetch로 조회해 **Step 1에서 계산한 Week N**의 문제 목록을 파악.
반드시 계산된 주차 번호를 명시해서 요청할 것.

```
https://github.com/orgs/DaleStudy/projects/6/views/5
```

## Step 3. 완료 여부 확인

`/Users/river/Developer/playground/leetcode-study`에서
각 문제 폴더에 `riveroverflows.py` 파일이 존재하는지 확인.

## Step 4. 결과 출력

| 문제명 | 난이도 | 완료 여부 |
|--------|--------|-----------|
| ...    | ...    | ✅ / ❌   |

남은 문제 중 어떤 것을 풀지 사용자에게 물어볼 것.
