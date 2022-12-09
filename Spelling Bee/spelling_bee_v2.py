import enchant
import time


def repeated_letter(string):
    for letter in string:
        if string.count(letter) > 1:
            return True
    return False


def letter_input_check():
    user_input = ""
    valid_input = False
    count = 0
    while not valid_input:
        count += 1
        if count > 1:
            print("Please make sure that you enter\n"
                  "- seven letters only\n"
                  "- no duplicate letters\n"
                  "- no other characters\n"
                  "- (white spaces and capitals are forgivable)")
        user_input = input("Enter the seven letters of today's Spelling Bee, starting with the middle (need "
                           "to include) letter: ").replace(" ", "").lower()
        valid_input = len(user_input) == 7 and user_input.isalpha() and not repeated_letter(user_input)
    return user_input


def get_words(first_nine_word_letters, first_eight_word_letters, letters_list):
    total_time = 0
    list_of_words = []
    num_eight = len(first_eight_word_letters)
    num_nine = len(first_nine_word_letters)
    key_letter = letters_list[0]
    start_time = time.time()
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    four_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d]
                    word = enchant.Dict("en_US")
                    is_word = word.check(four_letter_word)
                    if is_word and key_letter in four_letter_word:
                        list_of_words.append(four_letter_word)
                        print("\n--------------------------------")
                        print("New 4-letter word found!\n\033[1m{}\033[0m".format(four_letter_word))
                        print("--------------------------------\n")
                    for e in range(0, 7):
                        five_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d] + \
                                           letters_list[e]
                        word = enchant.Dict("en_US")
                        is_word = word.check(five_letter_word)
                        if is_word and key_letter in five_letter_word:
                            list_of_words.append(five_letter_word)
                            print("\n--------------------------------")
                            print("New 5-letter word found!\n\033[1m{}\033[0m".format(five_letter_word))
                            print("--------------------------------\n")

                        for f in range(0, 7):
                            six_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d] + \
                                              letters_list[e] + letters_list[f]
                            word = enchant.Dict("en_US")
                            is_word = word.check(six_letter_word)
                            if is_word and key_letter in six_letter_word:
                                list_of_words.append(six_letter_word)
                                print("\n--------------------------------")
                                print("New 6-letter word found!\n\033[1m{}\033[0m".format(six_letter_word))
                                print("--------------------------------\n")

                            if num_eight == 2:
                                eight_letter_word = first_eight_word_letters + six_letter_word
                                is_word = word.check(eight_letter_word)
                                if is_word and key_letter in eight_letter_word:
                                    list_of_words.append(eight_letter_word)
                                    print("\n--------------------------------")
                                    print("New 8-letter word found!\n\033[1m{}\033[0m".format(eight_letter_word))
                                    print("--------------------------------\n")

                            for g in range(0, 7):
                                seven_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + \
                                                    letters_list[d] + letters_list[e] + letters_list[f] + \
                                                    letters_list[g]
                                word = enchant.Dict("en_US")
                                is_word = word.check(seven_letter_word)
                                if is_word and key_letter in seven_letter_word:
                                    list_of_words.append(seven_letter_word)
                                    print("\n--------------------------------")
                                    print("New 7-letter word found!\n\033[1m{}\033[0m".format(seven_letter_word))
                                    print("--------------------------------\n")

                                if num_eight == 1:
                                    eight_letter_word = first_eight_word_letters + seven_letter_word
                                    word = enchant.Dict("en_US")
                                    is_word = word.check(eight_letter_word)
                                    if is_word and key_letter in eight_letter_word:
                                        list_of_words.append(eight_letter_word)
                                        print("\n--------------------------------")
                                        print("New 8-letter word found!\n\033[1m{}\033[0m".format(eight_letter_word))
                                        print("--------------------------------\n")

                                if num_nine == 2:
                                    nine_letter_word = first_nine_word_letters + seven_letter_word
                                    word = enchant.Dict("en_US")
                                    is_word = word.check(nine_letter_word)
                                    if is_word and key_letter in nine_letter_word:
                                        list_of_words.append(nine_letter_word)
                                        print("\n--------------------------------")
                                        print("New 9-letter word found!\n\033[1m{}\033[0m".format(nine_letter_word))
                                        print("--------------------------------\n")

                                for h in range(0, 7):
                                    # commented code below checks for 8  letter words without knowing any of the letters
                                    # takes additional ~220s x 7 for all permutations
                                    """eight_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + \
                                                        letters_list[d] + letters_list[e] + letters_list[f] + \
                                                        letters_list[g] + letters_list[h]
                                    word = enchant.Dict("en_US")
                                    is_word = word.check(eight_letter_word)
                                    if is_word and key_letter in eight_letter_word:
                                        list_of_words.append(eight_letter_word)
                                        print("\n--------------------------------")
                                        print("New {}-letter word found!\n\033[1m{}\033[0m".format(
                                            len(eight_letter_word), eight_letter_word))
                                        print("--------------------------------\n")
                                    """
                                    if num_nine == 1:
                                        nine_letter_word = first_nine_word_letters + letters_list[a] + letters_list[b] \
                                                           + letters_list[c] + letters_list[d] + letters_list[e] + \
                                                           letters_list[f] + letters_list[g] + letters_list[h]
                                        word = enchant.Dict("en_US")
                                        is_word = word.check(nine_letter_word)
                                        if is_word and key_letter in nine_letter_word:
                                            list_of_words.append(nine_letter_word)
                                            print("\n--------------------------------")
                                            print("New 9-letter word found!\n\033[1m{}\033[0m".format(nine_letter_word))
                                            print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, total_time]


nine_word_letters = ""
eight_word_letters = ""

# print title and instructions of program
print("\033[1m-----------------------------------")
print("--- NY Spelling Bee word finder ---")
print("-----------------------------------\033[0m")
print("\n\x1B[3mStart by entering the letters in the puzzle\x1B[0m\n")

# get letters from user
processed_user_input = letter_input_check()
letters = [processed_user_input[0], processed_user_input[1], processed_user_input[2], processed_user_input[3],
           processed_user_input[4], processed_user_input[5], processed_user_input[6]]

# check if user wants to check for longer words
print("In order to search for 9 letter words, you must know the first two letters of the ")
want_nine_letters = input("\nDo you want to search for 9-letter words (extra time)?\nY/N: ")
want_eight_letters = input("\nDo you want to search for 8-letter words (extra time)?\nY/N: ")

# Get first letter(s) in 9-letter word (if user says yes)
if want_nine_letters == "Y":
    nine_word_letters = input("\nWhat are the first letter(s) of the 9-letter words you're looking for?\n"
                              "\x1B[3m(You can find this in the 'Hints' tab of the game)\x1B[0m\n"
                              "Enter: ")

# Get first letter(s) in 8-letter word (if user says yes)
if want_eight_letters == "Y":
    eight_word_letters = input("\nWhat are the first letter(s) of the 8-letter words you're looking for?\n"
                               "\x1B[3m(You can find this in the 'Hints' tab of the game)\x1B[0m\n"
                               "Enter: ")

print("\n***** Starting computation... *****\n")

word_results_raw = get_words(nine_word_letters, eight_word_letters, letters)
all_words = word_results_raw[0]
total_comp_time = word_results_raw[1]

print("\nAll iterations finished, printing results...\n")

# sort words from longest to shortest
all_words.sort(key=len)
for word_num in range(0, len(all_words)):
    if len(all_words[word_num]) != len(all_words[word_num - 1]):
        print("\n\033[1m{} Letter Words:\033[0m".format(len(all_words[word_num])))
    print(str(word_num + 1) + ". " + all_words[word_num])

print("\n\nTotal computation time: {}s".format(round(total_comp_time, 1)))
print("Total of {} words".format(len(all_words)))
