import time
import pandas as pd


def line_colour_label(colour):
    if colour == "red":
        x = 1
    elif colour == "green":
        x = 2
    elif colour == "yellow":
        x = 3
    elif colour == "blue":
        x = 4
    elif colour == "pink":
        x = 5
    elif colour == "cyan":
        x = 6
    elif colour == "silver":
        x = 7
    else:
        x = 0
    return "\033[0;37;4{}m \033[0m ".format(x)


def bolden():
    return "\033[1m"


def italicise():
    return "\033[3m"


def underline():
    return "\033[4m"


def reset_text_formatting():
    return "\033[0m"


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


def get_words(var_letters):
    words = []
    with open('word_list_full.txt') as f:
        for line in f.readlines():
            words.append(line.strip("\n"))
    count = 0
    start_time = time.time()
    num_of_words = len(words)
    for word in range(0, num_of_words):
        stripped_word = words[word - count]
        for letter in range(0, len(var_letters)):
            stripped_word = stripped_word.replace(var_letters[letter], "")
        if len(stripped_word) > 0:
            words.remove(words[word - count])
            count += 1
        elif len(words[word - count]) < 4:
            words.remove(words[word - count])
            count += 1
    end_time = time.time()
    computation_time = end_time - start_time
    return [computation_time, words]


file_name = ""
four_letter_words = []
five_letter_words = []
six_letter_words = []
seven_letter_words = []
long_letter_words = []
words_dataframe = {
    "Four letters |": four_letter_words,
    "Five letters |": five_letter_words,
    "Six letters |": six_letter_words,
    "Seven letters |": seven_letter_words,
    "Eight+ letters |": long_letter_words,
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
all_words = word_results_raw[1]
total_comp_time = word_results_raw[0]

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
    else:
        long_letter_words.append(all_words[word_num] + " |")

four_letter_words.insert(0, " ")
five_letter_words.insert(0, " ")
six_letter_words.insert(0, " ")
seven_letter_words.insert(0, " ")
long_letter_words.insert(0, " ")
all_lists = [four_letter_words, five_letter_words, six_letter_words, seven_letter_words, long_letter_words]
max_length = find_max_list(all_lists)
for i in range(0, 5):
    while len(all_lists[i]) < max_length:
        all_lists[i].append(" |")
        # if vertical separator (made up of | character) is to only reach the final word of each column, then use:
        """all_lists[i].append(" ")"""


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
    pd.set_option('display.max_rows', None)
    # Sort columns in dataframe by four letters column (first column)
    words_frame = words_frame.set_index("Four letters |")
    words_frame.to_csv("{}.csv".format(file_name))

    df = pd.read_csv('{}.csv'.format(file_name))
    open('{}.txt'.format(file_name), 'a').close()

    print(str(df), file=open('{}.txt'.format(file_name), 'w'))

    temp_file = open('{}.txt'.format(file_name))
    string_list = temp_file.readlines()
    temp_file.close()

    string_list[1] = " ______________________________________________________________________________\n"
    my_file = open('{}.txt'.format(file_name), "w")
    new_file_contents = "".join(string_list)

    my_file.write(new_file_contents)
    my_file.close()

    print("\n\033[0;37;46m \033[0m \033[3mThe words have been successfully saved to file.\033[0m")
else:
    print()
print("\033[0;37;46m \033[0m Thank you for using this program!")
