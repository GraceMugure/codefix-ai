CodeFix AI

A Python CLI tool that runs Python code, detects errors, and explains them in plain English.

Overview

CodeFix AI is a command-line interface (CLI) tool that helps Python developers — especially beginners — understand errors in their code. It detects common Python errors and provides friendly explanations to help you fix your code quickly.

This project is based on the original CodeFix AI, but all improvements, CLI enhancements, and error explanations were implemented by me.

Features

.Detects common Python errors:

.SyntaxError

.IndentationError

.NameError

.TypeError

.ZeroDivisionError

.ValueError
/
.Provides plain-English explanations for errors.

.Works entirely in the terminal / command line.

.Easy to run with or without arguments.

Installation

Clone the repository:

git clone https://github.com/GraceMugure/codefix-ai.git
cd codefix-ai


Make sure Python 3 is installed.

Usage
Run a Python file:
python codefix-ai.py path/to/your_script.py

Run a Python file with arguments:
python codefix-ai.py path/to/your_script.py arg1 arg2

Examples
1. SyntaxError

test.py:

print("Hello World


Output:

[CodeFix AI] ❌ Your code has an error!
SyntaxError: unterminated string literal
[CodeFix AI] 💡 Explanation:
There’s a mistake in the code structure. Check colons, brackets, or indentation.

2. ZeroDivisionError

test.py:

print(10 / 0)


Output:

[CodeFix AI] ❌ Your code has an error!
ZeroDivisionError: division by zero
[CodeFix AI] 💡 Explanation:
You divided by zero, which is not allowed.

3. NameError

test.py:

print(unknown_variable)


Output:

[CodeFix AI] ❌ Your code has an error!
NameError: name 'unknown_variable' is not defined
[CodeFix AI] 💡 Explanation:
You used a variable/function that hasn’t been defined.

⚡ Features

Explains Python errors in simple English

Suggests improvements and fixes

Helps beginners understand errors instead of just fixing them

Works locally — no external API required

📌Limitations

Currently works only with Python code

Not all errors can be fully explained yet (work in progress 🚧)

🌟Future Plans

Add support for multiple programming languages

Smarter error explanations with AI integration

Option to auto-fix code
