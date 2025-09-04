#!/bin/bash
q=$1
if ! [[ "$q" =~ ^[0-9]+$ ]]; then
	echo "Error: q must be a number."
	exit 1
fi
echo "set up and open vscode for Question No.$q" 
file_path="./$q"
if [ -d "$file_path" ]; then
	echo "folder exists"
else
	mkdir "$q"
	cd "$q"
	touch "main.py"
	touch "README.md"
	echo "https://www.acmicpc.net/problem/$q" > README.md
fi

read -rp "Select editor (v: VS Code, p: PyCharm, c: Cursor) > " editor_choice
case "$editor_choice" in
	v|V)
		if command -v code >/dev/null 2>&1; then
			code .
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
			cursor .
		else
			echo "Cursor executable (cursor) not found in PATH."
		fi
		;;
	*)
		echo "Unknown input. Please enter one of v/p/c."
		;;
esac
