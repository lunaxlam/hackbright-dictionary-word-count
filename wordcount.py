"""Count words in file."""

def count_words(filename):
    #input: text, output: dictionary {'word': number}
    """Returns a dictionary with counted words."""

    #initialize empty dictionary 
    word_count = {}

    #open file
    text_file = open(filename)

    ### METHOD 1:
    # #create a list to store all words
    # list_of_words = []

    #use for loop to iterate over text file
    for line in text_file:
        words = line.strip().split(" ")
        ### METHOD 1 (cont.)
        # list_of_words.extend(words)

        ### METHOD 2
        for word in words:
            word_count[word] = word_count.get(word,0) + 1

    ### METHOD 1 (cont.)
    # #iterate over list of words to count words
    # for word in list_of_words:
    #     #if word exists as a key in dictionary
    #     if word in word_count:
    #         #add 1 to value
    #         word_count[word] += 1
    #     #else create a key and set value to 1
    #     else:
    #         word_count[word] = 1

    #return dictionary
    return word_count

print(count_words("test.txt"))