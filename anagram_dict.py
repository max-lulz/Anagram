import json


def read_dict(filename):
    with open(filename, 'r') as f:
        english_dict = json.load(f)

    return english_dict


def create_anagrams(words):
    anagram_dict = {}

    for (word, _) in words.items():
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] = anagram_dict.get(sorted_word, [])
        anagram_dict[sorted_word].append(word)

    return anagram_dict


def write_ana_dict(ana_dict, filename):
    #ana_json = json.dumps(ana_dict)
    with open(filename, 'w') as f:
        json.dump(ana_dict, f)


if __name__ == "__main__":
    eng_dict = read_dict("words_dictionary.json")
    ana_dict = create_anagrams(eng_dict)
    write_ana_dict(ana_dict, "anagrams.json")



