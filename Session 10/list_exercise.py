#HOMEWORK: Question 1 in exercise 4 and finish exercise 3 (this page)

#list exercise session 10
# mutable: can change elements in a list, but can't in a string
def nested_sum(t):   
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for i in t:
        total += sum(i)
    return(total)

def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    result = []
    total = 0
    for i in t:
        total += i
        result.append(total)
    return result

def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    list = t
    newList = []   
    for i in range(len(list[:-1])):
        newList = list[1:3]
    return newList

def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    del t[0]
    del t[-1]
    return 'None'


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    if list.sort(t):
        return True
    else:
        return False

def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    word1: string or list
    word2: string or list
    returns: boolean
    """
    string1 = word1
    string2 = word2
    word1 = []
    word2 = []
    #validate if the same letters are used in string1 and string2
    if(len(word1) == len(word2)):
        for letter in word1:
            if letter in word2:
                word2.remove(letter)
    if len(word2) == 0:
        return True
    else:
        return False

def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """
    for i in s:
        if s.count(i) > 1:
            return True
    return False

# def has_adjacent_duplicates(s):


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()
