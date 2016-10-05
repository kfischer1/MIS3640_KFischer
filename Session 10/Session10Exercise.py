L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print(L[0][0])  #index of apple
print(L[2][2])  #index of Lisa
print(L[1][2][1])   #index of On Rail


for team in AFC_East:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):       #length if 5 numbers -- range of 5 
    numbers[i] = numbers[i] * 2     #multiplies the number in list by 2
    
print(numbers)

# my_list = ['spam', 1, ['New England Patriots', \
#                        'Buffalo Bills', 'Miami Dolphins', \
#                        'New York Giants'], \
#            [1, 2, 3]]
# print(len(my_list))

