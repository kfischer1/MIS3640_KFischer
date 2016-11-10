import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# text = open('Treasure_Island.txt','r')

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

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def main():
    print('Sentiment Analysis of "Treasure Island"')
    text = process_file('Treasure_Island.txt', skip_header = True)
    lowercase = True
    stop_words = 'english'
    text1 = process_word(text)
    score = SentimentIntensityAnalyzer().polarity_scores(text1)
    print(score)


if __name__ == '__main__':
    main()