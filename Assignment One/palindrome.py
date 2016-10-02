#To check if a word or string was a palindrome I used the reverse function.
#This let me check if the word was a palindrome or not by checking if the word
# reversed was the same as the original word. I did it this way because it made the code
# much shorter and simpler to understand/run.

inputStr = input("Enter a string: ")
RevStr = reversed(inputStr)

def isPalindrome(s):
    if list(inputStr) == list(RevStr):
        print("That's a palindrome.")
    else:
        print("That isn't a palindrome.")

isPalindrome(inputStr)
