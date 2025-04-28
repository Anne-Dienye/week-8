#coding
import sys

# diff command implementation
def diff_command(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            if f1.read() == f2.read():
                print("The files are identical.")
            else:
                print("The files are different.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
    else:
        diff_command(sys.argv[1], sys.argv[2])