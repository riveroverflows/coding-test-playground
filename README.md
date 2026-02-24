# Coding Test Playground

알고리즘 코딩 테스트 풀이 저장소. Python, Java, Kotlin, C++을 지원합니다.

## 플랫폼

| 디렉토리                      | 플랫폼                |
|---------------------------|--------------------|
| `boj/`                    | 백준 온라인 저지          |
| `programmers/`            | 프로그래머스             |
| `leetcode/`               | LeetCode           |
| `code-up/`                | 코드업                |
| `book-codingtest-python/` | 이것이 취업을 위한 코딩 테스트다 |

## 언어 및 도구

| 언어     | IDE           | 버전                            |
|--------|---------------|-------------------------------|
| Python | PyCharm       | 3.8.5                         |
| Java   | IntelliJ IDEA | OpenJDK 14.0.2                |
| Kotlin | IntelliJ IDEA | 1.9.25 (language-version 1.6) |
| C++    | CLion         | C++17 (clang++)               |

Sublime Text 빌드 설정은 `.sublime-build/` 디렉토리에 있습니다.

## 입력 처리

각 솔루션은 stdin으로 입력을 받습니다. 프로젝트 루트의 `input.txt`에 테스트 입력을 작성하고:

- **IDE**: Run Configuration에서 Redirect input from → `input.txt`
    - **Sublime Text**: `Cmd+Shift+B` → Run (자동으로 `< input.txt` 적용)