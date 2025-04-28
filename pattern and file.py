#coding
import sys

# grep command implementation
def grep_command(pattern, file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if pattern.lower() in line.lower():  # Case-insensitive search
                    print(f"{line_number}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
    else:
        grep_command(sys.argv[1], sys.argv[2])