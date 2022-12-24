"""
def strip_invalid(lst):
    # initialise variables
    count = 1
    some_list = []
    # create a list of how often each letter occurs consecutively, very similar to run length encoding but with seven
    # possible characters instead of 0's and 1's. The actual characters are dismissible, the consecutive
    if len(lst) > 1:
        for i in range(1, len(lst)):
            if lst[i - 1] == lst[i]:
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


total_words = 0
for a in range(0, 7):
    for b in range(0, 7):
        for c in range(0, 7):
            for d in range(0, 7):
                for e in range(0, 7):
                    for f in range(0, 7):
                        for g in range(0, 7):
                            temp_list = [a, b, c, d, e, f, g]
                            if not strip_invalid(temp_list):
                                total_words += 1
                                print(temp_list)
                            else:
                                break

print("Total permutation possible now: {}".format(total_words))
print("7^7 = {}".format(7 * 7 * 7 * 7 * 7 * 7 * 7))
print("Percentage of original number of permutations: {}%"
      .format(round(100*total_words/(7 * 7 * 7 * 7 * 7 * 7 * 7), 2)))
"""
import pandas as pd
# create dataframe to store words separately according to their lengths
words_dataframe = {
    "Four letters |": ["abcd", "edgh"],
    "Five letters |": ["abacd", "edgah"],
    "Six letters |": ["abaacd", "eaadgh"],
    "Seven letters |": ["abaaacd", "edaaagh"],
    "Eight+ letters |": ["abcaaaad", "edaaaagh"],
}
# create pandas dataframe
words_frame = pd.DataFrame(words_dataframe)
# make sure all rows are shown and none are hidden
pd.set_option('display.max_rows', None)
# Sort columns in dataframe by four letters column (first column)
words_frame = words_frame.set_index("Four letters |")

words_frame.to_csv('Test.txt', header=False, index=None, sep=' ', mode='a')
