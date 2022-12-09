def pangram_finder(letters):
    words = []
    with open('word_list_full.txt') as f:
        for line in f.readlines():
            words.append(line.strip("\n"))
    for each_unique_letter in range(0, 7):
        count = 0
        print("start")
        for word in range(0, len(words)):
            try:
                print("word(var) = {} and count(var) = {}".format(word, count))
                print(words[word - count])
                words[word - count].index(letters[each_unique_letter])
            except ValueError:
                words.remove(words[word - count])
                count += 1
        print("finish")
    return words


list_of_letters = ['k', 'a', 'c', 'd', 'e', 'l', 't']

print("Original length: 178,693 words")
list_of_pangrams = pangram_finder(list_of_letters)
print("Pangrams for the letters KACDELT: {} words".format(len(list_of_pangrams)))
print("The words are:\n{}".format(list_of_pangrams))
