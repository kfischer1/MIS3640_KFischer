# Exercise 1

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    print(letter + suffix)

# #Exercise 2
def count(word, a):
    count = 0
    for letter in word:
        if letter == a:
            count += 1
    print(count)

count('New England Patriots','n')

#Exercise 3
team = 'New England Patriots'
print(team.split(' ',1))
print(team.split(' ',2))
print(team.split())
print(team)
print(team.strip())
print(team.strip('Patriots'))
print(team.replace('riots','s'))
print(team.replace('New England','Boston',2))

#Exercise 4 
def price(n):
    letter = 0
    p = 0 
    while letter < len(n):
        p += ord(n[letter]) - 96
        letter += 1
    print(n,'$'+str(p))
price('bananas')
price('rice')
price('paprika')
price('potato chips')
print("------------------------")
print('Total','$237')

 
def price(n):
    letter = 0
    p = 0 
    while letter < len(n):
        p += ord(n[letter]) - 96
        letter += 1
    print('{:16}{:3}'.format(n,'$'+str(p)))
    
price('bananas')
price('rice')
price('paprika')
price('potato chips')
print("------------")
print('{:16}{:3}'.format('Total','$237'))

'''
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
'''

#Exercise 6
def rotate_letter(letter, a):
    b = ord(letter) - 97
    c = (a + b) % 26 + 97
    return chr(c)
def rotate_word(word,a):
    new_word = ''
    for letter in word:
        new_word += rotate_letter(letter,a)
    print(new_word)

rotate_word('cheer',7)
rotate_word('melon', -10)

