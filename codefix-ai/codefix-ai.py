import traceback
import argparse
import subprocess
import os

def explain_error(error_msg):
    """Custom error explanations for common Python errors."""
    explanations = {
        "SyntaxError": "There’s a mistake in the code structure. Check colons, brackets, or indentation.",
        "IndentationError": "Your indentation is off. Make sure tabs/spaces are consistent.",
        "NameError": "You used a variable/function that hasn’t been defined.",
        "TypeError": "You’re using the wrong type. Example: adding a string and a number.",
        "ZeroDivisionError": "You divided by zero, which is not allowed.",
        "ValueError": "You used the right type but an invalid value. Example: int('abc')."
    }

    for key in explanations:
        if key in error_msg:
            return explanations[key]
    return "Unknown error. Try checking syntax and variable names."

def run_file(file_path, args_list):
    """Run a Python file and explain errors in plain English."""
    try:
        cmd_args = ["python", file_path] + args_list
        try:
            subprocess.check_output(cmd_args, stderr=subprocess.STDOUT)
            print("[CodeFix AI] ✅ Your code ran successfully!")
        except subprocess.CalledProcessError as e:
            exception_log = e.output.decode()
            print("-" * 50)
            print("[CodeFix AI] ❌ Your code has an error!")
            print(exception_log)
            print("[CodeFix AI] 💡 Explanation:")
            print(explain_error(exception_log))
            print("-" * 50)
    except Exception as e:
        exception_log = traceback.format_exc()
        print("-" * 50)
        print("[CodeFix AI] ❌ Failed to run file")
        print(exception_log)
        print("[CodeFix AI] 💡 Suggestion:")
        print(explain_error(exception_log))
        print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description="CodeFix AI: Run a Python file and explain errors")
    parser.add_argument("file", type=str, help="Path to the Python file to run")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments to pass to the Python script")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("[CodeFix AI] File not found: {}".format(args.file))
        exit(1)

    run_file(args.file, args.args)

if __name__ == "__main__":
    main()
