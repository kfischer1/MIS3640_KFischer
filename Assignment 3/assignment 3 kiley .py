import nltk, string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

file = open('Treasure_Island.txt')
t= file.read()

def main():
    hist1 = process_file('Flatland.txt', skip_header = True)
    hist2 = process_file('Treasure_Island.txt',skip_header = True)
    text1 = process_word(hist1)
    text2 = process_word(hist2)


score = SentimentIntensityAnalyzer().polarity_scores('t')
print(score)

if __name__ == '__main__':
    main()