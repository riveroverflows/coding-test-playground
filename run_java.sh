#!/bin/bash
JAVA_HOME="/Users/river/.local/share/mise/installs/java/openjdk-14.0.2"
FILE="$1"
FILE_PATH="$2"
FILE_BASE="$3"

# 소스에서 package 추출
pkg=$(grep -m1 '^package ' "$FILE" | sed 's/package //;s/;//;s/[[:space:]]//g')

# 컴파일
"$JAVA_HOME/bin/javac" -encoding UTF-8 "$FILE" || exit 1

# 실행
if [ -n "$pkg" ]; then
    # package 경로를 file_path에서 제거하여 classpath 계산
    # 예: file_path=/a/b/leetcode/p46_permutations, pkg=p46_permutations
    #     pkgpath=p46_permutations, cp=/a/b/leetcode
    pkgpath=$(echo "$pkg" | tr '.' '/')
    cp="${FILE_PATH%"/$pkgpath"}"
    "$JAVA_HOME/bin/java" -Dfile.encoding=UTF-8 -cp "$cp" "$pkg.$FILE_BASE"
else
    "$JAVA_HOME/bin/java" -Dfile.encoding=UTF-8 -cp "$FILE_PATH" "$FILE_BASE"
fi