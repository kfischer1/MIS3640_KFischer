list_1=[10,20]

AFC_East = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

#Nested: a list within another list
a_nested_list = ['spam', 2.0, 5, [10, 20]]


print(AFC_East)

# Will replace NY Jets (3) with NY Giants
AFC_East[3] = 'New York Giants'
print(AFC_East)

# will print just NE Patriots and Buffalo Bills
print(AFC_East[0:2])
print(AFC_East[2:4])

#list exercise 1
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print(L[0][0])  #index of apple(list 0, place holder 0)
print(L[2][2])  #index of Lisa
print(L[1][2][1])   #index of On Rail
for team in AFC_East:
    print(team)
numbers = [2, 0, 1, 6, 9]
for i in range(len(numbers)):       #length if 5 numbers -- range of 5 
    numbers[i] = numbers[i] * 2     #multiplies the number in list by 2
    
print(numbers)

# length of this list = 4 (4 elements within the list)
my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

#list operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)    #is not a sum: combines the two lists into a single list [1,2,3,4,5,6]

print([0] * 4)  #print the element 0 four times
print(['Tom Brady', 'Bill Belichick']*3) #prints the two names 3 times

#LIST SLICES:
t = ['a', 'b', 'c', 'd', 'e', 'f']
#get just [b,c]
print(t[1:3])
#print [a,b,c,d]
print(t[:4])
#Print [d,e,f]
print(t[3:])

# t[1:3] = ['x', 'y'] # will replace [b,c] with [x,y] within the list
print(t)

#EXERCISE 2
#append adds letter to end of list
t.append('g')
print(t)
# counts number of times a appears in the list
t.count('a')
print(t.count('a'))




