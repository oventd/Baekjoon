#!/bin/bash

# -----------------------------
# 1. n 값 설정
# -----------------------------
if [ -n "$1" ]; then
    n="$1"
elif [ -z "$n" ]; then
    read -rp "Enter question number: " n
fi
export num="$n"

# 숫자 확인
while ! [[ "$n" =~ ^[0-9]+$ ]]; do
    read -rp "Invalid number. Enter a valid question number: " n
done

# -----------------------------
# 2. n 확인 후 셋업 여부
# -----------------------------
while true; do
    read -rp "Set up and open editor for Question No.$n? (y/n) > " confirm
    case "$confirm" in
        y|Y)
            break
            ;;
        n|N)
            read -rp "Enter new question number: " n
            while ! [[ "$n" =~ ^[0-9]+$ ]]; do
                read -rp "Invalid number. Enter a valid question number: " n
            done
            export num="$n"
            ;;
        *)
            echo "Please enter y or n."
            ;;
    esac
done

# -----------------------------
# 3. 폴더 및 파일 생성
# -----------------------------
echo "Setting up folder and files for Question No.$n..."
file_path="./$n"
if [ -d "$file_path" ]; then
    echo "Folder already exists."
else
    mkdir -p "$n"
    pushd "$n" >/dev/null || exit
    touch "main.py"
    echo "https://www.acmicpc.net/problem/$n" > README.md
    popd >/dev/null
    cd "$n"
fi

# -----------------------------
# 4. 에디터 선택
# -----------------------------
read -rp "Select editor (v: VS Code, p: PyCharm, c: Cursor) > " editor_choice
case "$editor_choice" in
    v|V)
        if command -v code >/dev/null 2>&1; then
            code . &
        else
            echo "VS Code executable (code) not found in PATH."
        fi
        ;;
    p|P)
        if command -v pycharm64.exe >/dev/null 2>&1; then
            pycharm64.exe . &>/dev/null &
        else
            echo "PyCharm executable not found in PATH (pycharm64.exe)."
        fi
        ;;
    c|C)
        if command -v cursor >/dev/null 2>&1; then
            cursor . &
        else
            echo "Cursor executable (cursor) not found in PATH."
        fi
        ;;
    *)
        echo "Unknown input. Please enter one of v/p/c."
        ;;
esac
