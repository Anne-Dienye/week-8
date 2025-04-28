#coding
import sys

# wc command implementation
def wc_command(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            num_lines = contents.count('\n') + (1 if contents else 0)
            num_words = len(contents.split())
            num_chars = len(contents)
            print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
    else:
        wc_command(sys.argv[1])