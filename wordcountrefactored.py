"""Count words in file."""

def tokenize(filename):
    """
    Print a dictionary summary with counted words.
    
    :param filename: text file
    :return: list of words as a list
    """

    # Open text file and store as a file object
    text_file = open(filename)

    # Initialize an empty list of words to store all words from text file
    list_of_words = []

    for line in text_file:
        words = line.strip().split(" ")
        # Tokenize the list of words and add to list_of_words list
        list_of_words.extend(words)

    return list_of_words

def count_words(list_of_words):
    """
    Convert a list of strings and the number of occurrences into a dictionary. 

    :param list of words: list of words as strings
    :return: list of strings and the number of occurrence of each string as a dictionary
    """
        
    # Initialize an empty dictionary
    word_count = {}

    for word in list_of_words:
        # Convert all words to lowercase for uniformity
        word = word.lower()
        no_punctuation = ""
        for char in word:
            # Check to see if each character in the word .isalpha()
            if char.isalpha():
                no_punctuation += char
        # Update the dictionary
        word_count[no_punctuation] = word_count.get(word,0) + 1
    
    return word_count

def print_word_counts(word_count):
    """
    Print a string and the number of occurrences as a key: value pair.

    :param word_count: list of strings and the number of occurrences as a dictionary
    :return: None
    """
    
    # Iterate through the dictionary and print the key, value 
    for word, count in word_count.items():
        print(f"{word}: {count}")


print_word_counts(count_words(tokenize("test.txt")))