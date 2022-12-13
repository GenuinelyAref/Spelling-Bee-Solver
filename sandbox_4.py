# initialise list
words = []
# open and read the txt file with all the possible words
with open('word_list_full.txt') as f:
    # read the file line by line
    for line in f.readlines():
        # add each word as a separate item in a list
        words.append(line.strip("\n"))

# take into account number of words removed to offset them correctly when calling index
removal_count = 0
# for all the words in the word list
for word in range(0, len(words)):
    # if each word is less than 4 characters long
    if len(words[word - removal_count]) < 4:
        # remove it from the list
        words.remove(words[word - removal_count])
        # add one to the removal index count
        removal_count += 1

# for all the words in the word list
for word in range(0, len(words)):
    # re-add the removed a line break at the end of word
    words[word] = "{}\n".format(words[word])

# reopen text file but in write view
my_file = open('word_list_full.txt', "w")
# store new list (after changes) to a local variable
new_file_contents = "".join(words)

# write the local variable contents to the text file, replacing the 2nd line with a horizontal separator
my_file.write(new_file_contents)
# close the text file
my_file.close()
