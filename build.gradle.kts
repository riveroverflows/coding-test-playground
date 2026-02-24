plugins {
    kotlin("jvm") version "1.9.25" // java 플러그인 자동 포함
}

repositories {
    mavenCentral()
}

// 프로그래머스 Java 컴파일 환경: OpenJDK 14.0.2
java {
    sourceCompatibility = JavaVersion.VERSION_14
    targetCompatibility = JavaVersion.VERSION_14
}

// 프로그래머스 Kotlin 환경: Kotlin 1.6.10, languageVersion 1.6
// jvmTarget은 Java와 동일하게 14 (소스 코드 제출이므로 로컬 바이트코드 타겟 무관)
tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
    kotlinOptions {
        jvmTarget = "14"
        languageVersion = "1.6"
        apiVersion = "1.6"
    }
}

// 새 플랫폼 디렉토리 추가 시 여기에 경로 추가
val srcDirs = listOf("boj", "book-codingtest-python", "code-up", "leetcode", "programmers")

sourceSets {
    main {
        java.setSrcDirs(srcDirs)
        kotlin.setSrcDirs(srcDirs)
    }
}