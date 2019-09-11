import json

with open("anagrams.json", 'r') as f:
    some_dict = json.load(f)

word = input().lower()
word_sort = ''.join(sorted(word))

for words in some_dict[word_sort]:
    if words != word:
        print(words)
        break
