# import time library to record computation time
import time
# import pandas library for creation of nicely displayed table (using pandas dataframe)
import pandas as pd
# import module to obtain current date and time
from datetime import datetime


# function to create a vertical coloured slit at the beginning of each line
def line_colour_label(colour):
    # red for error messages
    if colour == "red":
        x = 1
    # currently unused
    elif colour == "green":
        x = 2
    # yellow for information/notes
    elif colour == "yellow":
        x = 3
    # blue for prompts
    elif colour == "blue":
        x = 4
    # currently unused
    elif colour == "pink":
        x = 5
    # cyan for summary messages at the end of processes
    elif colour == "cyan":
        x = 6
    # currently unused
    elif colour == "silver":
        x = 7
    # black for invalid colour name
    else:
        x = 0
    # print coloured label
    return "\033[0;37;4{}m \033[0m ".format(x)


# apply bold escape sequence code to text
def bolden():
    return "\033[1m"


# apply italic escape sequence code to text
def italicise():
    return "\033[3m"


# apply underline escape sequence code to text
def underline():
    return "\033[4m"


# reset escape sequence formatting in text
def reset_text_formatting():
    return "\033[0m"


# Generic yes/no checking function
def yes_no_checker(question, error_message):
    # start with invalid input
    var_valid = False
    # repeat until input is valid
    while not var_valid:
        # take input with given prompt
        answer = input(question)
        # apply lowercase to all characters in raw input
        answer = answer.lower()
        # if input is not blank
        try:
            # if first letter is y, read as 'yes'
            if answer[0] == "y":
                return "Yes"
            # if first letter is n, read as 'no'
            elif answer[0] == "n":
                return "No"
            # otherwise, print error message and keep input status as invalid
            else:
                print("\n" + error_message)
        # if input is bank
        except IndexError:
            # print error message and keep input status as invalid
            print("\n" + error_message)


# print banner with program name
def title_banner():
    # print program title banner
    print(line_colour_label("pink") + bolden() + "-------------------------------------------\n"
          + reset_text_formatting() +
          line_colour_label("pink") + bolden() + "-----   NY Spelling Bee word finder   -----\n"
          + reset_text_formatting() +
          line_colour_label("pink") + bolden() + "-------------------------------------------\n\n"
          + reset_text_formatting())


# program description + info
def instructions_and_information():
    # give information on usage of the program
    print(line_colour_label("yellow") + "This tool helps you find the answers to the NYT Spelling Bee puzzle.\n"
          + line_colour_label("yellow") + "Learn more about it here: https://www.nytimes.com/puzzles/spelling-bee\n\n"
          # advise user of the required prompts
          + line_colour_label(
        "blue") + "You will " + bolden() + underline() + "provide" + reset_text_formatting() + ":\n"
          + line_colour_label("blue") + "- a list of 7 unique letters\n"
          + line_colour_label("blue") + "- the must-have letter\n\n"
          # advise user of the expected outputs
          + line_colour_label(
        "cyan") + "You will " + bolden() + underline() + "receive" + reset_text_formatting() + ":\n"
          + line_colour_label("cyan") + "- 4, 5, 6 and 7-letter words as they are computed\n"
          + line_colour_label("cyan") + "- a list of all the words at the end\n"
          + line_colour_label("cyan") + "- updates (to see the progress of the computation)\n"
          + line_colour_label("cyan") + "- total computation time\n"
          + line_colour_label("cyan") + "- the option to save the list of words to a text file\n\n"
          )


# function to check for repeated letters in a string
def repeated_letter(string):
    # check for every letter in the string
    for letter in string:
        # that it only exists once in the entire string (nowhere else)
        if string.count(letter) > 1:
            # if any letter exists more than once, return True
            return True
    # if none of the letters exist more than once (no repeats), return False
    return False


# check that letters provided by user are valid for processing
def valid_letter_input():
    # initialise variables
    user_input = ""
    var_count = 0
    # start with invalid input
    valid_input = False
    # give user notice of input format
    print("\n" + line_colour_label("yellow") + underline() + italicise() +
          "For the following input, please enter:" + reset_text_formatting() + "\n"
          + line_colour_label("yellow") + "- seven letters only, separated by commas\n"
          + line_colour_label("yellow") + "- no duplicate letters\n"
          + line_colour_label("yellow") + "- no other characters\n"
          + line_colour_label("yellow") + "- (white spaces and capitals are forgivable)\n")
    # repeat until letter input is valid
    while not valid_input:
        # every time input is taken, add one count
        var_count += 1
        # if input is being taken for the second or more time, give an error message
        if var_count > 1:
            print("\n\n" +
                  line_colour_label("red") + "That's not a valid answer\n" +
                  line_colour_label("red") + underline() + "Please enter:" + reset_text_formatting() + "\n" +
                  line_colour_label("red") + "- seven letters only, separated by commas\n" +
                  line_colour_label("red") + "- no duplicate letters\n" +
                  line_colour_label("red") + "- no other characters\n" +
                  line_colour_label("red") + "- (white spaces and capitals are forgivable)\n")
        # get letter input from user, and remove commas, leading/trailing spaces and apply lowercase to all characters
        user_input = input(line_colour_label("blue") +
                           "Enter the seven letters, starting with the must-have letter: ").replace(" ", "") \
            .replace(",", "").lower()
        # check that processed input is alphanumeric, 7 characters (letters) long and no repeats are present
        # if all conditions met, set letter input validity as True
        valid_input = len(user_input) == 7 and user_input.isalpha() and not repeated_letter(user_input)
    # return valid letter list
    var_letters = [user_input[0], user_input[1], user_input[2], user_input[3],
                   user_input[4], user_input[5], user_input[6]]
    return var_letters


# update user on the commencement of the computation
def computation_started():
    print("\n\n" + line_colour_label("yellow") + bolden() + "***** Starting computation... *****" +
          reset_text_formatting() + "\n\n")


# obtain list of valid words (answers)
def get_words(var_letters):
    # initialise variables
    words = []
    running_removal_count = 0
    # open and read the txt file with all the possible words
    with open('word_list_full.txt') as f:
        # read the file line by line
        for line in f.readlines():
            # add each word as a separate item in a list
            words.append(line.strip("\n"))
    # start a timer to measure duration of computational period
    start_time = time.time()
    # cycle through all words in list of words
    for word in range(0, len(words)):
        # get subsequent word from list, accounting for the running total of the number of words removed from the list
        # to use correct index
        stripped_word = words[word - running_removal_count]
        # remove all the puzzle letters from the word to see what remains
        for letter in range(0, len(var_letters)):
            stripped_word = stripped_word.replace(var_letters[letter], "")
        # if any letters remain, then there must be invalid letters in the word
        if len(stripped_word) > 0:
            # remove the word from the word list
            words.remove(words[word - running_removal_count])
            # record the number of words removed to offset the index of the removed word when calling other words
            running_removal_count += 1
        # if word is shorter than 4 letters
        elif len(words[word - running_removal_count]) < 4:
            # remove the word from the word list
            words.remove(words[word - running_removal_count])
            # record the number of words removed to offset the index of the removed word when calling other words
            running_removal_count += 1
    # stop the timer
    end_time = time.time()
    # calculate the computation time
    computation_time = end_time - start_time
    # return the computation time and the list of valid words
    return [computation_time, words]


# update user on the conclusion of the computation
def computation_finished():
    print("\n" + line_colour_label("yellow") + "All iterations finished, printing results...\n")


# print all words found
def print_words(var_valid_words):
    # sort words from longest to shortest
    var_valid_words.sort(key=len)
    # repeat for the length of list of valid words
    for word_num in range(0, len(var_valid_words)):
        # if the length of the word is different (longer by one) the previous word, it is the first word of that length
        if len(var_valid_words[word_num]) != len(var_valid_words[word_num - 1]):
            # print a header with the length of following words
            print("\n" + line_colour_label("cyan") + bolden() + "{} Letter Words:"
                  .format(len(var_valid_words[word_num]))
                  + reset_text_formatting())
        # number the word according to its order in the list and print it
        print(line_colour_label("cyan") + str(word_num + 1) + ". " + var_valid_words[word_num])


# sort words into lists of respective lengths and add vertical separators
def prepare_for_print(var_valid_words):
    # initialise list variables
    # add a space at the beginning of each list of words for printing (to file) purposes
    var_four_letter_words = [" "]
    var_five_letter_words = [" "]
    var_six_letter_words = [" "]
    var_seven_letter_words = [" "]
    var_long_letter_words = [" "]
    # create separate word lists
    var_clean_four_letter_words = []
    var_clean_five_letter_words = []
    var_clean_six_letter_words = []
    var_clean_seven_letter_words = []
    var_clean_long_letter_words = []
    # repeat for the length of list of valid words
    for word_num in range(0, len(var_valid_words)):
        # add four letter words to the list of four letter words
        if len(var_valid_words[word_num]) == 4:
            var_four_letter_words.append(var_valid_words[word_num] + " |")
            var_clean_four_letter_words.append(var_valid_words[word_num])
        # add five letter words to the list of five letter words
        elif len(var_valid_words[word_num]) == 5:
            var_five_letter_words.append(var_valid_words[word_num] + " |")
            var_clean_five_letter_words.append(var_valid_words[word_num])
        # add six letter words to the list of six letter words
        elif len(var_valid_words[word_num]) == 6:
            var_six_letter_words.append(var_valid_words[word_num] + " |")
            var_clean_six_letter_words.append(var_valid_words[word_num])
        # add seven letter words to the list of seven letter words
        elif len(var_valid_words[word_num]) == 7:
            var_seven_letter_words.append(var_valid_words[word_num] + " |")
            var_clean_seven_letter_words.append(var_valid_words[word_num])
        # add words of other lengths (eight+) to a combined list
        else:
            var_long_letter_words.append(var_valid_words[word_num] + " |")
            var_clean_long_letter_words.append(var_valid_words[word_num])
    # collate all word lists in one list
    var_all_lists = [var_four_letter_words, var_five_letter_words, var_six_letter_words,
                     var_seven_letter_words, var_long_letter_words]
    # collate all clean word lists in one clean list
    var_clean_all_lists = [var_clean_four_letter_words, var_clean_five_letter_words, var_clean_six_letter_words,
                           var_clean_seven_letter_words, var_clean_long_letter_words]
    # return length of longest list within main list
    var_max_length = max([len(temp_var) for temp_var in var_all_lists])
    # add separators to empty word slots
    for i in range(0, 5):
        while len(var_all_lists[i]) < var_max_length:
            var_all_lists[i].append(" |")
            # if vertical separator (made up of | character) is to only reach the final word of each column, then use:
            """var_all_lists[i].append(" ")"""
        # add separators to empty word slots
    for i in range(0, 5):
        while len(var_clean_all_lists[i]) < var_max_length:
            var_clean_all_lists[i].append(" ")
    # add a space at the beginning of each list of words for printing (to file) purposes
    var_four_letter_words.pop(-1)
    var_five_letter_words.pop(-1)
    var_six_letter_words.pop(-1)
    var_seven_letter_words.pop(-1)
    var_long_letter_words.pop(-1)
    # create separate word lists
    var_clean_four_letter_words.pop(-1)
    var_clean_five_letter_words.pop(-1)
    var_clean_six_letter_words.pop(-1)
    var_clean_seven_letter_words.pop(-1)
    var_clean_long_letter_words.pop(-1)
    # return all word lists in order and ready to be printed nicely
    return [var_all_lists, var_clean_all_lists]


# give total number of words and total computation time
def give_computation_stats():
    print("\n\n" + line_colour_label("cyan") + bolden() + "Total computation time: {}s"
          .format(round(total_comp_time, 1)) + reset_text_formatting())
    print(line_colour_label("cyan") + bolden() + "Total of {} words".format(len(all_words)) + reset_text_formatting())


# check if user wants to save file, return yes or no
def check_want_file():
    return yes_no_checker("\n" + line_colour_label("blue") + "Do you want to save the list of words? Yes/No: ",
                          line_colour_label("red") + "That's not a valid answer\n")


# Function obtains valid file name for csv/txt files
def get_file_name():
    # initialise variables
    input_count = 0
    change_count = 0
    # start with invalid file name
    valid_file_name = False
    # give user notice on file name format
    print("\n" + line_colour_label("yellow") + "The file name can only have alphanumeric characters "
                                               "(spaces will be replaced with underscores)")
    # repeat until file name is valid
    while not valid_file_name:
        # every time input is taken, add one count
        input_count += 1
        # if input is being taken for the second or more time, give error message
        if input_count - change_count > 1:
            # same as prior user notice but in red
            print("\n" + line_colour_label("red") + "The file name can only have alphanumeric characters "
                                                    "(spaces will be replaced with underscores)")
        # manipulate file name to remove leading/trailing spaces and replace other spaces with underscores
        var_file_name = input("\n" + line_colour_label("blue") + "Please enter a file name: ") \
            .strip(" ").replace(" ", "_")
        # if file name is alphanumeric, check if user wants to change it
        # otherwise, file name validity stays as False, and loop cycles
        if var_file_name.replace("_", "").isalnum():
            # check if user wants to change the file name, yes or no response received
            want_to_change = yes_no_checker("\n" + line_colour_label("yellow") + "Your file name will be {}.txt\n\n"
                                            .format(var_file_name) + line_colour_label("blue") +
                                            "Do you want to change it? Yes/No: ", line_colour_label("red") +
                                            "That's not a valid answer")
            # if user happy with file name
            if want_to_change == "No":
                # return it
                return var_file_name
            # otherwise (taken as no)
            else:
                # record the number of times the user has changed the file name, to not print error messages prematurely
                change_count = input_count


# get current date and time
def date_and_time():
    # datetime object containing current date and time
    now = datetime.now()
    # store the 24-hour version of the hour in a variable
    hour = int(now.strftime("%H"))
    # if it's 12 or over (12-23), then it must be pm
    if hour >= 12:
        time_of_day = "pm"
    # if it's under 12 (0-11) then it must be am
    else:
        time_of_day = "am"
    # if the hour is 12am
    if hour == 0:
        # write 12 as the hour instead of zero as a string value
        adjusted_hour = "12"
    # otherwise, the hour is 1am - 11pm
    else:
        # create string version of the hour value
        adjusted_hour = str(int(now.strftime("%I")))
    # create string version of current time
    var_time = str(now.strftime("{}:%M{}".format(adjusted_hour, time_of_day)))
    # create string version of today's date
    var_date = str(now.strftime("%d/%m/%Y"))
    return [var_time, var_date]


"""# see if user wants a csv file or not
def check_want_csv_file():
    return yes_no_checker("\n" + line_colour_label("blue") +
                          "Do you also want to save a csv version of the words? Yes/No: ", line_colour_label("red") +
                          "That's not a valid answer\n")"""


# save results to text (and csv) file(s)
def save_to_file(var_all_lists, var_file_name, var_letters, var_time, var_date, var_clean_list):
    # create dataframe to store words separately according to their lengths
    words_dataframe = {
        "Four letters |": var_all_lists[0],
        "Five letters |": var_all_lists[1],
        "Six letters |": var_all_lists[2],
        "Seven letters |": var_all_lists[3],
        "Eight+ letters |": var_all_lists[4],
    }
    # create pandas dataframe
    words_frame = pd.DataFrame(words_dataframe)
    # make sure all rows are shown and none are hidden
    pd.set_option('display.max_rows', None)
    # Sort columns in dataframe by four letters column (first column)
    words_frame = words_frame.set_index("Four letters |")
    # convert dataframe to csv file
    words_frame.to_csv("{}.csv".format(var_file_name))

    # read csv file and store in a local variable
    df = pd.read_csv('{}.csv'.format(var_file_name))
    # create a text file and name it with the file name provided by user - open & close file allows creation of txt file
    open('{}.txt'.format(var_file_name), 'a').close()

    # write the contents of the local variable (from the csv file) to the text file
    print(str(df), file=open('{}.txt'.format(var_file_name), 'w'))

    # open text file in read view
    temp_file = open('{}.txt'.format(var_file_name))
    # store the text file as a list, where each line of the file is a separate list item
    string_list = temp_file.readlines()
    # close text file
    temp_file.close()

    # write the date and time to the text file
    string_list.insert(0, "This file was created at {} on {}.\n\n".format(var_time, var_date))
    string_list.insert(0, "The letters chosen are: '{}' (key letter), '{}', '{}', '{}', '{}', '{}' and '{}'"
                          ".\n\n".format(var_letters[0], var_letters[1], var_letters[2], var_letters[3],
                                         var_letters[4], var_letters[5], var_letters[6]))
    string_list.insert(2, "   ----------------------------------------------------------------------------\n")
    string_list.insert(4, "   ----------------------------------------------------------------------------\n")
    # remove second list item (with index 0 and no content)
    string_list[5] = ""
    # reopen text file but in write view
    my_file = open('{}.txt'.format(file_name), "w")
    # store new list (after changes) to a local variable
    new_file_contents = "".join(string_list)

    # write the local variable contents to the text file, replacing the 2nd line with a horizontal separator
    my_file.write(new_file_contents)
    # close the text file
    my_file.close()

    # create dataframe to store words separately according to their lengths
    clean_words_dataframe = {
        "Four letters": var_clean_list[0],
        "Five letters": var_clean_list[1],
        "Six letters": var_clean_list[2],
        "Seven letters": var_clean_list[3],
        "Eight+ letters": var_clean_list[4],
    }
    # create pandas dataframe
    clean_words_frame = pd.DataFrame(clean_words_dataframe)
    # make sure all rows are shown and none are hidden
    pd.set_option('display.max_rows', None)
    # Sort columns in dataframe by four letters column (first column)
    clean_words_frame = clean_words_frame.set_index("Four letters")
    # convert dataframe to csv file
    clean_words_frame.to_csv("{}.csv".format(var_file_name))

    # print saving success message
    print("\n" + line_colour_label("cyan") + italicise() + "The words have been successfully saved to file."
          + reset_text_formatting())


def farewell_user():
    print(line_colour_label("cyan") + "Thank you for using this program!")


# MAIN ROUTINE

# initialise text variables
file_name = ""

# show program title
title_banner()

# show instructions and program info
instructions_and_information()

# get valid list of letters from user
letters = valid_letter_input()

# update user on the commencement of the computation
computation_started()

# call for computation and collect raw output
word_results_raw = get_words(letters)
# retrieve list of valid words
all_words = word_results_raw[1]
# retrieve overall computation time
total_comp_time = word_results_raw[0]

# update user on the conclusion of the computation
computation_finished()

# print all words found
print_words(all_words)

# give total number of words and total computation time
give_computation_stats()

# check if user wants to save file
want_file = check_want_file()

# user wants to save the words
if want_file == "Yes":
    # sort all words into lists according to their lengths
    all_lists = prepare_for_print(all_words)
    printable_list = all_lists[0]
    clean_list = all_lists[1]

    # get file name from user
    file_name = get_file_name()

    # get current time and date
    time_and_date_raw = date_and_time()
    current_time = time_and_date_raw[0]
    current_date = time_and_date_raw[1]

    """
    # see if user wants a csv copy too
    want_csv_file = check_want_csv_file()
    """

    # save words to file
    save_to_file(printable_list, file_name, letters, current_time, current_date, clean_list)
# user does not want to save the words
else:
    # add spacing to separate differently-coloured line labels
    print()

# farewell user
farewell_user()
