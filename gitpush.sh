#!/bin/bash

# -----------------------------
# 1. commit 번호 결정
# -----------------------------
if [ -z "$num" ]; then
    # num이 없으면 새로 입력
    while true; do
        read -rp "Enter commit number: " n
        if [[ "$n" =~ ^[0-9]+$ ]]; then
            num="$n"
            break
        else
            echo "Invalid number. Please enter a numeric value."
        fi
    done
else
    # num이 이미 있을 때
    while true; do
        read -rp "num=$num exists. Use it as commit number? (y: yes, n: enter new, number: append _1 etc.) > " choice
        case "$choice" in
            y|Y)
                n="$num"
                break
                ;;
            n|N)
                while true; do
                    read -rp "Enter new commit number: " n
                    if [[ "$n" =~ ^[0-9]+$ ]]; then
                        num="$n"
                        break
                    else
                        echo "Invalid number. Please enter a numeric value."
                    fi
                done
                break
                ;;
            *)
                # 숫자 입력이면 기존 num 뒤에 _숫자 붙이기
                if [[ "$choice" =~ ^[0-9]+$ ]]; then
                    suffix="$choice"
                    n="${num}_$suffix"
                    echo "Commit number set to $n"
                    break
                else
                    echo "Invalid input. Please enter y/n/number."
                fi
                ;;
        esac
    done
fi

# -----------------------------
# 2. 푸시 여부 확인
# -----------------------------
while true; do
    read -rp "Do you want to push No.$n? (y/n): " confirm
    case "$confirm" in
        y|Y)
            git add .
            git commit -m "No.$n"
            git push
            echo "Pushed commit No.$n ✅"
            break
            ;;
        n|N)
            echo "Commit canceled ❌"
            break
            ;;
        *)
            echo "Please enter y or n."
            ;;
    esac
done
