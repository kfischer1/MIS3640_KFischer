team = 'New England Patriots'
# print(team[0])

# #print(team[1.5])
# # number of letters in team
# print(len(team))
# # prints the 19th letter
# print(team[19])
# # or (-1 is the last one)
# print([len(team)-1])
# print(last)

# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index += 1
    
# #use 'for' instead of 'while'
# for letter in team:
#     print(letter)

# Exercise 1

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         suffix = 'uack'
#     else:
#         suffix = 'ack'
#     print(letter + suffix)

# prints 'New England' only on a line
# print(team[0:11])
# #prints 'Patriots'
# print(team[12:20])
# print([:11])
# print(team[12:])

#Exercise 2


word = 'New England Patriots'
str.letters(word)
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

print(count, letter)
