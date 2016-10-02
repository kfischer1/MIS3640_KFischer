# #Exercise 2
# #Using Recursion
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    elif word[0] > word[1]:
        return False
    return(is_abecedarian(word[1:]))

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

#Using while loop
def is_abecedarian(word):
    n = 0
    previous = word[n]
    s = len(word)
    while n < s-1:
        if word[n + 1] < word[n]:
            return False
        n+=1
    return True

print(is_abecedarian('abs'))
print(is_abecedarian('college'))

#Exercise 3
# 3 pairs of letters consecutively
def cattalk():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        n = 0
        while n <= (len(word)-6):
            if word[n] == word[n+1]:
                if word[n+2] == word[n+3]:
                    if word [n+4] == word[n+5]:
                        print(word)
            n+=1

cattalk()

