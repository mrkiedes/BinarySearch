# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("engmix.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

def binarySearch(term):
    print(term)


wordList = get_dictionary()
found = binarySearch("test")