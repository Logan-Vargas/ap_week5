# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.

magic = 'abracadabra'

# a. Retrieve the 5th character
fifth_char = magic[4]       # Indexing starts at 0
# 'c'

# b. Retrieve the second to last character
second_last = magic[-2]
# 'r'

# c. Find the first occurrence of the letter 'c'
first_c_index = magic.index('c')
# 4


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# a. Extract the letters 'hij'
hij = alphabet[7:10]
# 'hij'

# b. Extract every second letter starting from 'a' to 'm'
every_second_to_m = alphabet[0:13:2]
# 'acegikm'

# c. Reverse the entire string
reversed_alphabet = alphabet[::-1]


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
name = quote.split('-')[-1].strip()
# 'John F. Kennedy'


# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

info = "Python is fun. Fun is good. Good is subjective."

# a. Extract the word 'subjective'
word_subjective = info.split()[-1].strip('.')
# 'subjective'

# b. Extract every third word
every_third_word = info.split()[::3]
# ['Python', 'Fun', 'Good']

# c. Reverse the positions of the words
reversed_words = ' '.join(info.split()[::-1])
# 'subjective. Good is good. Fun is fun. is Python'


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

text = "MAY THE FORCE BE WITH YOU."
lower_text = text.lower()
# 'may the force be with you.'


# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

motto = ["Make", "haste", "slowly."]

# a. Convert list to a single string
joined_motto = ' '.join(motto)
# 'Make haste slowly.'

# b. Split at every occurrence of 'a'
split_motto = joined_motto.split('a')
# ['M', 'ke h', 'ste slowly.']


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

sentence = "Life is what happens when you are busy making other plans."

# a. Replace "busy" with "distracted"
sentence1 = sentence.replace("busy", "distracted")

# b. Replace "plans" with "mistakes"
sentence2 = sentence1.replace("plans", "mistakes")


# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

word = "Iteration"
repeated = word * 7
# 'IterationIterationIterationIterationIterationIterationIteration'


# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
contains_moonlight = "moonlight" in quote
# False


# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.

word = "Supercalifragilisticexpialidocious"

# a. Number of characters
length = len(word)
# 34

# b. Count occurrences of 'i'
count_i = word.count('i')
# 7
