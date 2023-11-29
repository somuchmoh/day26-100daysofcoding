student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

is_word = True
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while is_word:
    word_input = input("Enter word: ")
    try:
        letter_list = [letter.upper() for letter in word_input]
        code_list = [nato_dict[letter] for letter in letter_list]
    except KeyError:
        print("Sorry, only letters in the alphabets please!")
    else:
        print(code_list)
        is_word = False
