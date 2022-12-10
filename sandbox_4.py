"""import time


def filter_words_from_list(letters):
    words = []
    start_time = time.time()
    with open('word_list_full.txt') as f:
        for line in f.readlines():
            words.append(line.strip("\n"))
    count = 0
    end_time = time.time()
    extraction_time = end_time - start_time
    start_time = time.time()
    for word in range(0, len(words)):
        stripped_word = words[word - count]
        for letter in range(0, len(letters)):
            stripped_word = stripped_word.replace(letters[letter], "")
        if len(stripped_word) > 0:
            words.remove(words[word - count])
            count += 1
        elif len(words[word - count]) < 4:
            words.remove(words[word - count])
            count += 1
    end_time = time.time()
    computation_time = end_time - start_time
    return [extraction_time, computation_time, words]


list_of_letters = ['k', 'a', 'c', 'd', 'e', 'l', 't']

print("Original length: 178,693 words")
raw_result = filter_words_from_list(list_of_letters)
list_of_valid_words = raw_result[2]
time_one = raw_result[0]
time_two = raw_result[1]
print("Time taken to turn txt file into a list: {}s".format(round(time_one, 1)))
print("Time taken to find all valid words: {}s".format(round(time_two, 1)))
print("Valid words for the letters KACDELT: {} words".format(len(list_of_valid_words)))
print("The words are:\n{}".format(list_of_valid_words))"""
