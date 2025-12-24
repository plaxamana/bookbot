from collections import Counter
def get_num_words(file_contents):
  words = file_contents.split()
  return len(words)

def get_num_of_chars(file_contents):
  text = file_contents.lower()
  counter = Counter()
  for char in text:
    counter[char] += 1

  return counter

def get_sorted_dicts(counter):
  return dict(counter.most_common())