import sys
from stats import get_num_words, get_num_of_chars, get_sorted_dicts

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def main():
  if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  file_path = sys.argv[1]
  content = get_book_text(file_path)
  num_words = get_num_words(content)
  num_chars = get_num_of_chars(content)
  sorted_chars = get_sorted_dicts(num_chars)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for key, val in sorted_chars.items():
    if key.isalpha():
      print(f"{key}: {val}")
  print("============= END ===============")
main()