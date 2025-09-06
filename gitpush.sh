#!/bin/bash

# num이 이미 정의되어 있는지 확인
if [ -z "$n" ]; then
    read -rp "Enter commit number: " n
    export num=n
fi

# 푸시 여부 확인
read -rp "Do you want to push No.$n? (y/n): " confirm

if [[ $confirm == "y" || $confirm == "Y" ]]; then
    git add .
    git commit -m "No.$n"
    git push
    echo "Pushed commit No.$n ✅"
else
    echo "Commit canceled ❌"
fi