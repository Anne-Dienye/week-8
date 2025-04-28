#coding
import sys

# Load the dictionary from a file
def load_dictionary(dict_file="dictionary.txt"):
    try:
        with open(dict_file, 'r') as file:
            # Read all words from the dictionary file, convert to lowercase, and store in a set
            return set(word.strip().lower() for word in file)
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dict_file}' not found.")
        return set()

# Spell-checking function
def spell_check(file_name, dictionary):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Extract words from the line (remove punctuation and split by whitespace)
                words = line.strip().split()
                for word in words:
                    # Remove punctuation and convert to lowercase
                    clean_word = ''.join(char.lower() for char in word if char.isalpha())
                    if clean_word and clean_word not in dictionary:
                        print(clean_word)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python spell.py <filename>")
    else:
        # Load the dictionary
        dictionary = load_dictionary()
        if dictionary:
            # Perform spell-checking on the input file
            spell_check(sys.argv[1], dictionary)