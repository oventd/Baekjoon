#!/bin/bash
q=$1
echo "set up and open vscode for Question No.$q" 
file_path="./$q"
if [ -f "$file_path" ]; then
	echo "folder exists"
else
	mkdir "$q"
	cd "$q"
	touch "main.py"
	touch "README.md"
	echo "https://www.acmicpc.net/problem/$q" > README.md
	code .
fi
