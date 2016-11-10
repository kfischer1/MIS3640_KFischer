import random, string, nltk
from sklearn.feature_extraction.text import TfidfVectorizer

def process_file(filename, skip_header):
    hist = {}
    fp = open(filename)
    if skip_header:
        skip_gutenberg_header(fp)
    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        for word in line.split():
            word = word.lower()
            hist[word] = hist.get(word,0) + 1 
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())     

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common_10(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    temp = []
    for word, frequency in hist.items():
        temp.append((frequency, word))              #sorts by first element, so put freq first for order

    temp.sort()                 #sorts smallest to largest
    temp.reverse()              # reverses list to read most frequent to least
    top_10 = temp [:10]
    return top_10

def different_word(book_1_top10,book_2_top10):
    '''
    book_1_top10,book_2_top10: the top 10 most frequent words in each book
    returns: list of words that appear the top 10 in each text that don't appear in other texts
    '''
    book_1_word = []
    book_2_word = []
    difference = []
    #convert dict to list, store the each book's top 10 words in a list 
    for frequency,word in book_1_top10:
        book_1_word.append(word)
    for frequency,word in book_2_top10:
        book_2_word.append(word)
    #add the different word in a new list
    for word in book_1_word:
        if word not in book_2_word:
            difference.append(word)
    return difference


def process_word(hist):
    #define a list to store words
    word_list = []
    #add all the words of a book to the list 
    for word,frequency in hist.items():
        n = 0
        while n < frequency:
            word_list.append(word)
            n += 1
    #covert the list to string, because the function Similarity_Test only takes string
    word_string = ' '.join(word_list)
    return word_string


def Similarity_Test(text1, text2):
    '''
    text1, text2: two strings that contains each book's total words
    return: similarity score of the two books
    '''
    #convert all the words of two books to a vector, except for the stop words
    vectorizer = TfidfVectorizer(stop_words= 'english')    
    tfidf = vectorizer.fit_transform([text1, text2])
    #multipe the vector by its transpose to get the Similarity score
    return ((tfidf * tfidf.T).A)[0,1]


def main():
    print('Text Analysis of "Flatland" and "Treasure Island"')
    
    hist1 = process_file('Flatland.txt', skip_header = True)
    hist2 = process_file('Treasure_Island.txt',skip_header = True)
    print('Total number of words of "Flatland":', total_words(hist1))
    print('Number of different words of "Flatland":', different_words(hist1))
    print('Total number of words of "Treasure Island":', total_words(hist2))
    print('Number of different words of "Treasure Island":', different_words(hist2))
    
    most_common1 = most_common_10(hist1)
    most_common2 = most_common_10(hist2)
    print('The top ten words in "Flatland" is :', most_common1)
    print('The top ten words in "Treasure Island" is :', most_common2)
    
    difference = different_word(most_common1,most_common2)
    print("Difference words between two books' top 10 words are:",difference)
    text1 = process_word(hist1)
    text2 = process_word(hist2)
    similarity = Similarity_Test(text1,text2)
    print('Similarity of the two books is:',similarity)

if __name__ == '__main__':
    main()

