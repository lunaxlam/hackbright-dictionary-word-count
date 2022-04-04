"""Count words in file."""

def count_words(filename):
    """
    Print a dictionary summary with counted words.
    
    :param filename: text file
    :return: None
    """

    # Initialize an empty dictionary
    word_count = {}

    # Open text file and store as a file object
    text_file = open(filename)


    ### METHOD 1:
    for line in text_file:
        words = line.strip().split(" ")

        for word in words:
            for char in words:
                no_punctuation = ""
                if char.isalpha():
                    no_punctuation += char
                word_count[no_punctuation] = word_count.get(word,0) + 1

    ### METHOD 2:
    # # Initialize an empty list to store list of words from file
    # list_of_words = []

    # # Iterate through each line in file
    # for line in text_file:
    #     # Tokenize each line to individual words, use " " as delimiter
    #     words = line.strip().split(" ")
    #     # Add words to list_of_words by tokenizing each element in words
    #     list_of_words.extend(words)
 
    # # Iterate over list of words to update membership and count in dictionary
    # for word in list_of_words:
    #     # If word exists as a key in dictionary, increment by 1
    #     if word in word_count:
    #         word_count[word] += 1
    #     # Else initialize a new key and set value to 1
    #     else:
    #         word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word}: {count}")


print(count_words("test.txt"))