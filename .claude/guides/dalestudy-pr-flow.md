# DaleStudy leetcode-study PR Flow 가이드

## 기본 정보

- **fork repo 경로**: `~/Developer/playground/leetcode-study`
- **upstream repo**: `DaleStudy/leetcode-study`
- **GitHub 계정**: `riveroverflows`
- **스터디 프로젝트**: `리트코드 스터디 7기` (project #26)
- **주차 문제 스케줄**: `문제 풀이 스케줄` (project #6)
- **브랜치**: fork의 `main` → upstream `main`으로 PR

---

## Step 1. 파일 생성 및 커밋

```bash
# 파일 생성 위치: {문제폴더명}/riveroverflows.py
# 예: valid-anagram/riveroverflows.py
```

파일 형식:
```python
from typing import *


class Solution:
    """
    TC: O(...)
    ...

    풀이:
    ...
    """
    def methodName(self, ...):
        ...
```

주의사항 (CI 검사 있음):
- 파일명 반드시 `riveroverflows`로 시작해야 함
- 파일 끝에 줄바꿈(`\n`) 필수 (없으면 CI 실패)

```bash
# 커밋 메시지 형식: "{문제명} solution" (소문자)
cd /Users/river/Developer/playground/leetcode-study
git add {문제폴더}/riveroverflows.py
git commit -m "{문제명} solution"
git push origin main
```

---

## Step 2. PR 생성 (주차 첫 문제일 때만)

> 같은 주차에 이미 PR이 열려있으면 커밋만 push하고 Step 5(체크박스 업데이트)로 이동.

```bash
cd /Users/river/Developer/playground/leetcode-study

gh pr create \
  --repo DaleStudy/leetcode-study \
  --title "[riveroverflows] WEEK 0N Solutions" \
  --label "py" \
  --assignee "riveroverflows" \
  --body "$(cat <<'EOF'
## 답안 제출 문제

- [x] #이슈번호1
- [ ] #이슈번호2
- [ ] #이슈번호3
- [ ] #이슈번호4
- [ ] #이슈번호5

## 작성자 체크 리스트

- [ ] **Projects**의 오른쪽 버튼(▼)을 눌러 확장한 뒤, **Week**를 현재 주차로 설정해주세요.
- [ ] 문제를 모두 푸시면 프로젝트에서 **Status**를 `In Review`로 설정해주세요.
- [ ] 코드 검토자 1분 이상으로부터 승인을 받으셨다면 PR을 병합해주세요.

## 검토자 체크 리스트

> [!IMPORTANT]
> 본인 답안 제출 뿐만 아니라 다른 분 PR 하나 이상을 반드시 검토를 해주셔야 합니다!

- [ ] 바로 이전에 올라온 PR에 본인을 코드 리뷰어로 추가해주세요.
- [ ] 본인이 검토해야하는 PR의 답안 코드에 피드백을 주세요.
- [ ] 토요일 전까지 PR을 병합할 수 있도록 승인해주세요.
EOF
)"
```

> PR 생성 시 `--project` 옵션으로 Week 자동 설정 불가능. 생성 후 GraphQL API로 별도 설정 필요.

---

## Step 3. Week 설정 (GraphQL API)

```bash
# 3-1. PR의 project item ID 조회
gh api graphql -f query='
{
  repository(owner: "DaleStudy", name: "leetcode-study") {
    pullRequest(number: {MY_PR_NUMBER}) {
      projectItems(first: 5) {
        nodes {
          id
          project { title }
        }
      }
    }
  }
}'
# → "리트코드 스터디 7기" 프로젝트의 item ID를 사용

# 3-2. Week 설정
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PVT_kwDOBijJi84A9whE"
    itemId: "{ITEM_ID}"
    fieldId: "PVTIF_lADOBijJi84A9whEzg-GxfM"
    value: { iterationId: "{WEEK_ITERATION_ID}" }
  }) {
    projectV2Item { id }
  }
}'
```

### Week iteration ID (7기 기준)

| Week    | startDate  | iterationId |
|---------|------------|-------------|
| Week 2  | 2026-03-08 | `1323841f`  |
| Week 3  | 2026-03-15 | `0f651524`  |
| Week 4  | 2026-03-22 | `59694a9d`  |
| Week 5  | 2026-03-29 | `d90b420b`  |
| Week 6  | 2026-04-05 | `66d56623`  |
| Week 7  | 2026-04-12 | `3d61fb64`  |
| Week 8  | 2026-04-19 | `13878a9e`  |
| Week 9  | 2026-04-26 | `95ba5f37`  |
| Week 10 | 2026-05-03 | `c37cc0d1`  |
| Week 11 | 2026-05-10 | `cfac1476`  |
| Week 12 | 2026-05-17 | `1d1d9d50`  |
| Week 13 | 2026-05-24 | `58b2e15c`  |
| Week 14 | 2026-05-31 | `585df32a`  |
| Week 15 | 2026-06-07 | `1f7e47dc`  |

---

## Step 4. 직전 PR에 리뷰어 등록

```bash
# 직전 PR 번호 찾기 (내 PR보다 번호 작은 가장 최근 open PR)
gh pr list --repo DaleStudy/leetcode-study --state open --limit 20 --json number,createdAt \
  | python3 -c "
import json, sys
prs = sorted(json.load(sys.stdin), key=lambda x: x['number'])
my_pr = {MY_PR_NUMBER}
prev = [p for p in prs if p['number'] < my_pr]
print(prev[-1]['number'] if prev else 'none')
"

# 직전 PR에 리뷰어 등록
gh pr edit {PREV_PR_NUMBER} --repo DaleStudy/leetcode-study --add-reviewer riveroverflows
```

---

## Step 5. PR 체크리스트 업데이트

```bash
gh pr view {MY_PR_NUMBER} --repo DaleStudy/leetcode-study --json body -q '.body' > /tmp/pr_body.txt

# Week 설정 완료 시
sed -i '' 's/- \[ \] \*\*Projects\*\*/- [x] **Projects**/' /tmp/pr_body.txt

# 리뷰어 등록 완료 시
sed -i '' 's/- \[ \] 바로 이전에 올라온 PR에 본인을 코드 리뷰어로 추가해주세요./- [x] 바로 이전에 올라온 PR에 본인을 코드 리뷰어로 추가해주세요./' /tmp/pr_body.txt

# 문제 이슈 체크 시
sed -i '' 's/- \[ \] #{이슈번호}/- [x] #{이슈번호}/' /tmp/pr_body.txt

gh pr edit {MY_PR_NUMBER} --repo DaleStudy/leetcode-study --body-file /tmp/pr_body.txt
```

---

## Step 6. 모든 문제 완료 시 Status → In Review

```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PVT_kwDOBijJi84A9whE"
    itemId: "{ITEM_ID}"
    fieldId: "PVTSSF_lADOBijJi84A9whEzgxXXPk"
    value: { singleSelectOptionId: "47fc9ee4" }
  }) {
    projectV2Item { id }
  }
}'

# PR 체크리스트도 업데이트
gh pr view {MY_PR_NUMBER} --repo DaleStudy/leetcode-study --json body -q '.body' > /tmp/pr_body.txt
sed -i '' 's/- \[ \] 문제를 모두 푸시면/- [x] 문제를 모두 푸시면/' /tmp/pr_body.txt
gh pr edit {MY_PR_NUMBER} --repo DaleStudy/leetcode-study --body-file /tmp/pr_body.txt
```

---

## 핵심 ID 참고

| 항목                | 값                                |
|-------------------|----------------------------------|
| 프로젝트 ID (7기)      | `PVT_kwDOBijJi84A9whE`           |
| Week field ID     | `PVTIF_lADOBijJi84A9whEzg-GxfM`  |
| Status field ID   | `PVTSSF_lADOBijJi84A9whEzgxXXPk` |
| Status: In Review | `47fc9ee4`                       |
| Status: Completed | `98236657`                       |
