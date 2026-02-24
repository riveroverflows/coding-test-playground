#!/bin/bash
export JAVA_HOME="/Users/river/.local/share/mise/installs/java/openjdk-14.0.2"
FILE="$1"
FILE_PATH="$2"
FILE_BASE="$3"

# 컴파일: 프로그래머스 환경 (Kotlin 1.6.10, jvm-target 1.8)
/Users/river/.local/share/mise/installs/kotlin/1.9.25/kotlinc/bin/kotlinc \
    -language-version 1.6 -api-version 1.6 \
    -jvm-target 1.8 -include-runtime \
    -d "$FILE_PATH/$FILE_BASE.jar" "$FILE" || exit 1

# 실행
"$JAVA_HOME/bin/java" -Dfile.encoding=UTF-8 -jar "$FILE_PATH/$FILE_BASE.jar"
