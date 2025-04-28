#coding
import sys

# nl command implementation
def nl_command(python):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number:6}  {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl.py <filename>")
    else:
        nl_command(sys.argv[1])