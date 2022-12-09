import enchant
import time
import matplotlib.pyplot as plt
import math
# from collections import Counter
import numpy as np


def nine_letter_words_two_known(first_two_letters, letters_list):
    print("\n*********************************")
    print("*** Finding 9 letter words... ***")
    print("*********************************\n")
    nine_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    for e in range(0, 7):
                        for f in range(0, 7):
                            for g in range(0, 7):
                                string = first_two_letters + letters_list[a] + letters_list[b] + letters_list[c] + \
                                         letters_list[d] + letters_list[e] + letters_list[f] + letters_list[g]
                                word = enchant.Dict("en_US")
                                is_word = word.check(string)
                                key_letter = letters_list[0]
                                if is_word and key_letter in string:
                                    list_of_words.append(string)
                                    print("\n--------------------------------")
                                    print("New word found!\n\033[1m{}\033[0m\nNumber of 9-letter words so far: {}"
                                          .format(string, len(list_of_words)))
                                    print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        nine_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, nine_total_time]


def nine_letter_words_one_known(first_letter, letters_list):
    print("\n*********************************")
    print("*** Finding 9 letter words... ***")
    print("*********************************\n")
    nine_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    for e in range(0, 7):
                        for f in range(0, 7):
                            for g in range(0, 7):
                                for h in range(0, 7):
                                    string = first_letter + letters_list[a] + letters_list[b] + letters_list[c] + \
                                             letters_list[d] + letters_list[e] + letters_list[f] + letters_list[g] + \
                                             letters_list[h]
                                    word = enchant.Dict("en_US")
                                    is_word = word.check(string)
                                    key_letter = letters_list[0]
                                    if is_word and key_letter in string:
                                        list_of_words.append(string)
                                        print("\n--------------------------------")
                                        print("New word found!\n\033[1m{}\033[0m\nNumber of 9-letter words so far: {}"
                                              .format(string, len(list_of_words)))
                                        print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        nine_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, nine_total_time]


def eight_letter_words_two_known(first_two_letters, letters_list):
    print("\n*********************************")
    print("*** Finding 8 letter words... ***")
    print("*********************************\n")
    eight_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    for e in range(0, 7):
                        for f in range(0, 7):
                            string = first_two_letters + letters_list[a] + letters_list[b] + letters_list[c] + \
                                     letters_list[d] + letters_list[e] + letters_list[f]
                            word = enchant.Dict("en_US")
                            is_word = word.check(string)
                            key_letter = letters_list[0]
                            if is_word and key_letter in string:
                                list_of_words.append(string)
                                print("\n--------------------------------")
                                print("New word found!\n\033[1m{}\033[0m\nNumber of 8-letter words so far: {}"
                                      .format(string, len(list_of_words)))
                                print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        eight_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, eight_total_time]


def eight_letter_words_one_known(first_letter, letters_list):
    print("\n*********************************")
    print("*** Finding 8 letter words... ***")
    print("*********************************\n")
    eight_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    for e in range(0, 7):
                        for f in range(0, 7):
                            for g in range(0, 7):
                                string = first_letter + letters_list[a] + letters_list[b] + letters_list[c] + \
                                         letters_list[d] + letters_list[e] + letters_list[f] + letters_list[g]
                                word = enchant.Dict("en_US")
                                is_word = word.check(string)
                                key_letter = letters_list[0]
                                if is_word and key_letter in string:
                                    list_of_words.append(string)
                                    print("\n--------------------------------")
                                    print("New word found!\n\033[1m{}\033[0m\nNumber of 8-letter words so far: {}"
                                          .format(string, len(list_of_words)))
                                    print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        eight_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, eight_total_time]


def seven_letter_words(letters_list):
    print("\n*********************************")
    print("*** Finding 7 letter words... ***")
    print("*********************************\n")
    seven_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    for e in range(0, 7):
                        for f in range(0, 7):
                            for g in range(0, 7):

                                string = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d] + \
                                         letters_list[e] + letters_list[f] + letters_list[g]
                                word = enchant.Dict("en_US")
                                is_word = word.check(string)
                                key_letter = letters_list[0]
                                if is_word and key_letter in string:
                                    list_of_words.append(string)
                                    print("\n--------------------------------")
                                    print("New word found!\n\033[1m{}\033[0m\nNumber of 7-letter words so far: {}"
                                          .format(string, len(list_of_words)))
                                    print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        seven_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, seven_total_time]


def six_letter_words(letters_list):
    print("\n*********************************")
    print("*** Finding 6 letter words... ***")
    print("*********************************\n")
    six_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    for e in range(0, 7):
                        for f in range(0, 7):
                            string = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d] + \
                                     letters_list[e] + letters_list[f]
                            word = enchant.Dict("en_US")
                            is_word = word.check(string)
                            key_letter = letters_list[0]
                            if is_word and key_letter in string:
                                list_of_words.append(string)
                                print("\n--------------------------------")
                                print("New word found!\n\033[1m{}\033[0m\nNumber of 6-letter words so far: {}"
                                      .format(string, len(list_of_words)))
                                print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        six_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, six_total_time]


def five_letter_words(letters_list):
    print("\n*********************************")
    print("*** Finding 5 letter words... ***")
    print("*********************************\n")
    five_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    for e in range(0, 7):
                        string = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d] + \
                                 letters_list[e]
                        word = enchant.Dict("en_US")
                        is_word = word.check(string)
                        key_letter = letters_list[0]
                        if is_word and key_letter in string:
                            list_of_words.append(string)
                            print("\n--------------------------------")
                            print("New word found!\n\033[1m{}\033[0m\nNumber of 5-letter words so far: {}"
                                  .format(string, len(list_of_words)))
                            print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        five_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, five_total_time]


def four_letter_words(letters_list):
    print("\n*********************************")
    print("*** Finding 4 letter words... ***")
    print("*********************************\n")
    four_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    string = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d]
                    word = enchant.Dict("en_US")
                    is_word = word.check(string)
                    key_letter = letters_list[0]
                    if is_word and key_letter in string:
                        list_of_words.append(string)
                        print("\n--------------------------------")
                        print("New word found!\n\033[1m{}\033[0m\nNumber of 4-letter words so far: {}"
                              .format(string, len(list_of_words)))
                        print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        four_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, four_total_time]


def three_letter_words(letters_list):
    print("\n*********************************")
    print("*** Finding 3 letter words... ***")
    print("*********************************\n")
    three_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                string = letters_list[a] + letters_list[b] + letters_list[c]
                word = enchant.Dict("en_US")
                is_word = word.check(string)
                key_letter = letters_list[0]
                if is_word and key_letter in string:
                    list_of_words.append(string)
                    print("\n--------------------------------")
                    print("New word found!\n\033[1m{}\033[0m\nNumber of 3-letter words so far: {}"
                          .format(string, len(list_of_words)))
                    print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        three_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, three_total_time]


def two_letter_words(letters_list):
    print("\n*********************************")
    print("*** Finding 2 letter words... ***")
    print("*********************************\n")
    two_total_time = 0
    start_time = time.time()
    list_of_words = []
    for a in range(0, 7):
        for b in range(0, 7):
            string = letters_list[a] + letters_list[b]
            word = enchant.Dict("en_US")
            is_word = word.check(string)
            key_letter = letters_list[0]
            if is_word and key_letter in string:
                list_of_words.append(string)
                print("\n--------------------------------")
                print("New word found!\n\033[1m{}\033[0m\nNumber of 2-letter words so far: {}"
                      .format(string, len(list_of_words)))
                print("--------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        two_total_time += time_lapsed
        print("\x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(a + 1, round(
            time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, two_total_time]


# first letter is the critical letter (must be in all words)
# letters = ['k', 'a', 'c', 'd', 'e', 'l', 't']

nine_time = 0
eight_time = 0
nine_letter = []
eight_letter = []
letter_num_one = 0
letter_num_two = 0
starting_letters_one = ""
starting_letters_two = ""
nine_letter_words_list = []
eight_letter_words_list = []

# print title
print("\033[1m---------------------------------------------------")
print("--- NY Spelling Bee word finder (DVLPR VERSION) ---")
print("---------------------------------------------------\033[0m")

# get letters from user
letters = ['k', 'a', 'c', 'd', 'e', 'l', 't']

# check if user wants to check for longer words
long_words_one = "N"
long_words_two = "N"

# Get first two letters in 9-letter word (if user says yes)
if long_words_one == "Y":
    starting_letters_one = ""

# Get first two letters in 8-letter word (if user says yes)
if long_words_two == "Y":
    starting_letters_two = ""

for iteration in range(1, 11):
    if long_words_one == "Y":
        if letter_num_one == 2:
            nine_letter = nine_letter_words_two_known(starting_letters_one, letters)
        elif letter_num_one == 1:
            nine_letter = nine_letter_words_one_known(starting_letters_one, letters)
        nine_letter_words_list = nine_letter[0]
        nine_time = nine_letter[1]

    if long_words_two == "Y":
        if letter_num_two == 2:
            eight_letter = eight_letter_words_two_known(starting_letters_two, letters)
        if letter_num_two == 1:
            eight_letter = eight_letter_words_one_known(starting_letters_two, letters)
        eight_letter_words_list = eight_letter[0]
        eight_time = eight_letter[1]

    # commented out code to find seven letter words
    seven_letter = seven_letter_words(letters)
    seven_letter_words_list = seven_letter[0]
    seven_time = seven_letter[1]

    six_letter = six_letter_words(letters)
    six_letter_words_list = six_letter[0]
    six_time = six_letter[1]

    five_letter = five_letter_words(letters)
    five_letter_words_list = five_letter[0]
    five_time = five_letter[1]

    four_letter = four_letter_words(letters)
    four_letter_words_list = four_letter[0]
    four_time = four_letter[1]

    three_letter = three_letter_words(letters)
    three_letter_words_list = three_letter[0]
    three_time = three_letter[1]

    two_letter = two_letter_words(letters)
    two_letter_words_list = two_letter[0]
    two_time = two_letter[1]

    print("\nAll iterations finished, printing results...\n")

    if long_words_one == "Y":
        print("\033[1m9 Letter Words:\033[0m")
        print("\x1B[3mComputation time: {}s\x1B[0m".format(round(nine_time, 1)))
        for i in range(0, len(nine_letter_words_list)):
            print(str(i + 1) + ". " + nine_letter_words_list[i])

    if long_words_two == "Y":
        print("\033[1m8 Letter Words:\033[0m")
        print("\x1B[3mComputation time: {}s\x1B[0m".format(round(eight_time, 1)))
        for i in range(0, len(eight_letter_words_list)):
            print(str(i + 1 + len(nine_letter_words_list)) + ". " + eight_letter_words_list[i])

    print("\n\033[1m7 Letter Words:\033[0m")
    print("\x1B[3mComputation time: {}s\x1B[0m".format(round(seven_time, 1)))
    for i in range(0, len(seven_letter_words_list)):
        print(
            str(i + 1 + len(nine_letter_words_list) + len(eight_letter_words_list)) +
            ". " + seven_letter_words_list[i])

    print("\n\033[1m6 Letter Words:\033[0m")
    print("\x1B[3mComputation time: {}s\x1B[0m".format(round(six_time, 1)))
    for i in range(0, len(six_letter_words_list)):
        print(
            str(i + 1 + len(nine_letter_words_list) + len(eight_letter_words_list) + len(seven_letter_words_list)) +
            ". " + six_letter_words_list[i])

    print("\n\033[1m5 Letter Words:\033[0m")
    print("\x1B[3mComputation time: {}s\x1B[0m".format(round(five_time, 1)))
    for i in range(0, len(five_letter_words_list)):
        print(str(i + 1 + len(nine_letter_words_list) + len(eight_letter_words_list) + len(seven_letter_words_list) +
                  len(six_letter_words_list)) + ". " + five_letter_words_list[i])

    print("\n\033[1m4 Letter Words:\033[0m")
    print("\x1B[3mComputation time: {}s\x1B[0m".format(round(four_time, 1)))
    for i in range(0, len(four_letter_words_list)):
        print(str(i + 1 + len(nine_letter_words_list) + len(eight_letter_words_list) + len(seven_letter_words_list) +
                  len(six_letter_words_list) + len(five_letter_words_list)) + ". " + four_letter_words_list[i])

    print("\n\033[1m3 Letter Words:\033[0m")
    print("\x1B[3mComputation time: {}s\x1B[0m".format(round(three_time, 1)))
    for i in range(0, len(three_letter_words_list)):
        print(str(i + 1 + len(nine_letter_words_list) + len(eight_letter_words_list) + len(seven_letter_words_list) +
                  len(six_letter_words_list) + len(five_letter_words_list) + len(four_letter_words_list)) + ". " +
              three_letter_words_list[i])

    print("\n\033[1m2 Letter Words:\033[0m")
    print("\x1B[3mComputation time: {}s\x1B[0m".format(round(two_time, 1)))
    for i in range(0, len(two_letter_words_list)):
        print(str(i + 1 + len(nine_letter_words_list) + len(eight_letter_words_list) + len(seven_letter_words_list) +
                  len(six_letter_words_list) + len(five_letter_words_list) + len(four_letter_words_list) +
                  len(three_letter_words_list)) + ". " + two_letter_words_list[i])

    total_time = round(nine_time + eight_time + seven_time + six_time + five_time + four_time + three_time + two_time,
                       2)
    print("\n\nTotal computation time: {}".format(total_time))
    total_num_words = len(nine_letter_words_list) + len(eight_letter_words_list) + len(seven_letter_words_list) + \
                      len(six_letter_words_list) + len(five_letter_words_list) + len(four_letter_words_list) + \
                      len(three_letter_words_list) + len(two_letter_words_list)

    print("Total number of words found: {}".format(total_num_words))

    # daily data
    # US date for spelling bees
    # 22/09/2022: 'handout' took 268.1s for 42 words
    # 23/09/2022: 'barzgon' took 251.46s for 44 words
    # 24/09/2022: 'onfruit' took <>s for <> words
    # 25/09/2022: 'klacted' took <>s for <> words
    # 26/09/2022: '' took <>s for <> words

    # line 1 points
    x1 = [2, 3, 4, 5, 6, 7]

    # CHANGE THIS ****
    # CHANGE THIS ****
    # CHANGE THIS ****
    y1 = [math.log(two_time),
          math.log(three_time),
          math.log(four_time),
          math.log(five_time), math.log(six_time), math.log(seven_time)]
    # CHANGE THIS ****
    # CHANGE THIS ****
    # CHANGE THIS ****

    # plotting points
    plt.plot(x1, y1)

    # line 2 points
    # x2 = [1, 2, 3]
    # y2 = [4, 1, 3]
    # plotting the line 2 points
    # plt.plot(x2, y2, label="line 2")

    # naming the x axis
    plt.xlabel('Length of words (# of letters)')
    # naming the y axis
    plt.ylabel('Natural log of time')
    # giving a title to my graph
    plt.title('Natural Log of computation time vs length of words')

    # save graph to local folder
    plt.savefig('day-one_try-9_iteration-num-{}.png'.format(iteration))
