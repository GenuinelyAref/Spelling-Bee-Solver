import enchant
import time
import pandas as pd


# Generic yes/no checking function
def yes_no_checker(question, error_message):
    valid_two = False
    while not valid_two:
        answer = input(question)
        answer = answer.lower()
        try:
            if answer[0] == "y":
                return "Yes"
            elif answer[0] == "n":
                return "No"
            else:
                print("\n" + error_message)
        except IndexError:
            print("\n" + error_message)


# Function checks for blank input
def get_file_name():
    var_file_name = ""
    valid_file_name = False
    count = 0
    print("\n\033[0;37;43m \033[0m The file name can only have alphanumeric characters "
          "(spaces will be replaced with underscores)")
    while not valid_file_name:
        count += 1
        if count > 1:
            print("\n\033[0;37;41m \033[0m The file name can only have alphanumeric characters "
                  "(spaces will be replaced with underscores)")
        var_file_name = input("\n\033[0;37;44m \033[0m Please enter a file name: ").strip(" ").replace(" ", "_")
        if var_file_name.replace("_", "").isalnum():
            valid_file_name = True
    return var_file_name


def repeated_letter(string):
    for letter in string:
        if string.count(letter) > 1:
            return True
    return False


# return length of longest list within main list
def find_max_list(lst):
    list_len = [len(temp_var) for temp_var in lst]
    return max(list_len)


def letter_input_check():
    user_input = ""
    valid_input = False
    count = 0
    print("\n\033[0;37;43m \033[0m \033[4m\033[3mFor the following input, please enter:\033[0m\n"
          "\033[0;37;43m \033[0m \033[3m- seven letters only, separated by commas\n"
          "\033[0;37;43m \033[0m \033[3m- no duplicate letters\n"
          "\033[0;37;43m \033[0m \033[3m- no other characters\n"
          "\033[0;37;43m \033[0m \033[3m- (white spaces and capitals are forgivable)\n")
    while not valid_input:
        count += 1
        if count > 1:
            print("\n\n"
                  "\033[0;37;41m \033[0m That's not a valid answer\n"
                  "\033[0;37;41m \033[0m \033[4mPlease enter:\033[0m\n"
                  "\033[0;37;41m \033[0m - seven letters only, separated by commas\n"
                  "\033[0;37;41m \033[0m - no duplicate letters\n"
                  "\033[0;37;41m \033[0m - no other characters\n"
                  "\033[0;37;41m \033[0m - (white spaces and capitals are forgivable)\n")
        user_input = input("\033[0;37;44m \033[0m "
                           "Enter the seven letters, starting with the must-have letter: ").replace(" ", "").replace(
            ",", "").lower()
        valid_input = len(user_input) == 7 and user_input.isalpha() and not repeated_letter(user_input)
    return user_input


def strip_invalid(lst):
    # initialise variables
    count = 1
    some_list = []
    # create a list of how often each letter occurs consecutively, very similar to run length encoding but with seven
    # possible characters instead of 0's and 1's. The actual characters are dismissible, the consecutive
    if len(lst) > 1:
        for x in range(1, len(lst)):
            if lst[x - 1] == lst[x]:
                count += 1
            else:
                some_list.append(count)
                count = 1
        some_list.append(count)
    # remove occurrences of 1/2 consecutive letters, if anything remains then there are instances of 3+ consecutive
    # letters, which would return True
    some_list = list(filter(lambda var_one: var_one != 1, some_list))
    some_list = list(filter(lambda var_two: var_two != 2, some_list))
    if len(some_list) > 0:
        return True
    # after checking for this condition, check for secondary condition to further eliminate more invalid options
    else:
        # if must-have letter is present at least once, then the string can be a valid word
        if lst.count(0) != 0:
            return False
        # otherwise, it can't be a valid word
        else:
            return True


def get_words(letters_list):
    total_time = 0
    list_of_words = []
    start_time = time.time()
    for a in range(0, 7):
        for b in range(0, 7):
            for c in range(0, 7):
                for d in range(0, 7):
                    temp_list = [a, b, c, d]
                    if strip_invalid(temp_list):
                        break
                    else:
                        four_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d]
                        word = enchant.Dict("en_US")
                        is_word = word.check(four_letter_word)
                        if is_word:
                            list_of_words.append(four_letter_word)
                            print("\n\033[0;37;45m \033[0m --------------------------------")
                            print("\033[0;37;45m \033[0m  New 4-letter word found!\n"
                                  "\033[0;37;45m \033[0m  \033[1m{}\033[0m".format(four_letter_word))
                            print("\033[0;37;45m \033[0m --------------------------------\n")
                    for e in range(0, 7):
                        temp_list = [a, b, c, d, e]
                        if strip_invalid(temp_list):
                            break
                        else:
                            five_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + letters_list[d] + \
                                               letters_list[e]
                            word = enchant.Dict("en_US")
                            is_word = word.check(five_letter_word)
                            if is_word:
                                list_of_words.append(five_letter_word)
                                print("\n\033[0;37;45m \033[0m --------------------------------")
                                print("\033[0;37;45m \033[0m  New 5-letter word found!\n"
                                      "\033[0;37;45m \033[0m  \033[1m{}\033[0m".format(five_letter_word))
                                print("\033[0;37;45m \033[0m --------------------------------\n")
                        for f in range(0, 7):
                            temp_list = [a, b, c, d, e, f]
                            if strip_invalid(temp_list):
                                break
                            else:
                                six_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + \
                                                  letters_list[d] + letters_list[e] + letters_list[f]
                                word = enchant.Dict("en_US")
                                is_word = word.check(six_letter_word)
                                if is_word:
                                    list_of_words.append(six_letter_word)
                                    print("\n\033[0;37;45m \033[0m --------------------------------")
                                    print("\033[0;37;45m \033[0m  New 6-letter word found!\n"
                                          "\033[0;37;45m \033[0m  \033[1m{}\033[0m".format(six_letter_word))
                                    print("\033[0;37;45m \033[0m --------------------------------\n")

                            for g in range(0, 7):
                                temp_list = [a, b, c, d, e, f, g]
                                if strip_invalid(temp_list):
                                    break
                                else:
                                    seven_letter_word = letters_list[a] + letters_list[b] + letters_list[c] + \
                                                        letters_list[d] + letters_list[e] + letters_list[f] + \
                                                        letters_list[g]
                                    word = enchant.Dict("en_US")
                                    is_word = word.check(seven_letter_word)
                                    if is_word:
                                        list_of_words.append(seven_letter_word)
                                        print("\n\033[0;37;45m \033[0m --------------------------------")
                                        print("\033[0;37;45m \033[0m  New 7-letter word found!\n"
                                              "\033[0;37;45m \033[0m  \033[1m{}\033[0m".format(seven_letter_word))
                                        print("\033[0;37;45m \033[0m --------------------------------\n")
        end_time = time.time()
        time_lapsed = end_time - start_time
        total_time += time_lapsed
        print(
            "\033[0;37;46m \033[0m \x1B[3mProgress report: {}/7 of possible permutations completed ({}s)\x1B[0m".format(
                a + 1, round(
                    time_lapsed, 1)))
        start_time = time.time()
    return [list_of_words, total_time]


nine_word_letters = ""
eight_word_letters = ""
file_name = ""
four_letter_words = []
five_letter_words = []
six_letter_words = []
seven_letter_words = []
words_dataframe = {
    "Four letters |": four_letter_words,
    "Five letters |": five_letter_words,
    "Six letters |": six_letter_words,
    "Seven letters |": seven_letter_words,
}

# print title and instructions of program
print("\033[1m-----------------------------------")
print("--- NY Spelling Bee word finder ---")
print("-----------------------------------\033[0m")
print("\n\033[0;37;43m \033[0m This tool helps you find the answers to the NYT Spelling Bee puzzle.\n"
      "\033[0;37;43m \033[0m Learn more about it here: https://www.nytimes.com/puzzles/spelling-bee\n\n"
      "\033[0;37;44m \033[0m You will \033[1m\033[4mprovide\033[0m:\n"
      "\033[0;37;44m \033[0m - a list of 7 unique letters\n"
      "\033[0;37;44m \033[0m - the must-have letter\n\n"
      "\033[0;37;46m \033[0m You will \033[1m\033[4mreceive\033[0m:\n"
      "\033[0;37;46m \033[0m - 4, 5, 6 and 7-letter words as they are computed\n"
      "\033[0;37;46m \033[0m - a list of all the words at the end\n"
      "\033[0;37;46m \033[0m - updates (to see the progress of the computation)\n"
      "\033[0;37;46m \033[0m - total computation time\n"
      "\033[0;37;46m \033[0m - the option to save the list of words to a text file "
      )

print("\n")

# get letters from user
processed_user_input = letter_input_check()
letters = [processed_user_input[0], processed_user_input[1], processed_user_input[2], processed_user_input[3],
           processed_user_input[4], processed_user_input[5], processed_user_input[6]]

print("\n\n\n\033[0;37;43m \033[0m \033[1m***** Starting computation... *****\033[0m\n")

word_results_raw = get_words(letters)
all_words = word_results_raw[0]
total_comp_time = word_results_raw[1]

print("\n\033[0;37;43m \033[0m All iterations finished, printing results...\n")

# sort words from longest to shortest
all_words.sort(key=len)
for word_num in range(0, len(all_words)):
    if len(all_words[word_num]) != len(all_words[word_num - 1]):
        print("\n\033[0;37;46m \033[0m \033[1m{} Letter Words:\033[0m".format(len(all_words[word_num])))
    print("\033[0;37;46m \033[0m " + str(word_num + 1) + ". " + all_words[word_num])
    if len(all_words[word_num]) == 4:
        four_letter_words.append(all_words[word_num] + " |")
    elif len(all_words[word_num]) == 5:
        five_letter_words.append(all_words[word_num] + " |")
    elif len(all_words[word_num]) == 6:
        six_letter_words.append(all_words[word_num] + " |")
    elif len(all_words[word_num]) == 7:
        seven_letter_words.append(all_words[word_num] + " |")

four_letter_words.insert(0, " ")
five_letter_words.insert(0, " ")
six_letter_words.insert(0, " ")
seven_letter_words.insert(0, " ")
all_lists = [four_letter_words, five_letter_words, six_letter_words, seven_letter_words]
max_length = find_max_list(all_lists)
for i in range(0, 4):
    while len(all_lists[i]) < max_length:
        all_lists[i].append(" ")


print("\n\n\033[0;37;46m \033[0m \033[1mTotal computation time: {}s\033[0m".format(round(total_comp_time, 1)))
print("\033[0;37;46m \033[0m \033[1mTotal of {} words\033[0m".format(len(all_words)))


want_file = yes_no_checker("\n\033[0;37;44m \033[0m Do you want to save the list of words? Yes/No: ",
                           "\033[0;37;41m \033[0m That's not a valid answer\n")
if want_file == "Yes":
    confirmed = False
    while not confirmed:
        file_name = get_file_name()
        want_to_change = yes_no_checker("\n\033[0;37;43m \033[0m Your file name will be \"{}.txt\""
                                        "\n\n\033[0;37;44m \033[0m Do you want to change it? Yes/No: ".format(file_name),
                                        "\033[0;37;41m \033[0m That's not a valid answer")
        if want_to_change == "No":
            confirmed = True
    words_frame = pd.DataFrame(words_dataframe)
    # Sort columns in dataframe by four letters column (first column)
    words_frame = words_frame.set_index("Four letters |")
    words_frame.to_csv("{}.csv".format(file_name))

    df = pd.read_csv('{}.csv'.format(file_name))
    open('{}.txt'.format(file_name), 'a').close()

    print(str(df), file=open('{}.txt'.format(file_name), 'w'))

    print("\n\033[0;37;46m \033[0m \033[3mThe words have been successfully saved to file.\033[0m")
else:
    print()
print("\033[0;37;46m \033[0m Thank you for using this program!")
