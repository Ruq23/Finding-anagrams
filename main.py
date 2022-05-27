# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
from unittest import result


print("Hello")
print("Welcome to Anagrams Checker")


def find_anagrams(word, anagram):
    if len(word) == len(anagram):
        if sorted(word) == sorted(anagram):
            print(True)
            print('%s and %s are anagrams! Good Job' %(word, anagram))
        else:
            print(False)
            print('%s and %s are not anagrams! Try another word' %(word, anagram))
    else:
        print(False)
        print("Words are not the same length. Check and try again")


find_anagrams("bored", "robed")


#-----------------------------------------------
# to accept user's input
# word = input( "What is your first word?")
# anagram = input( "What is your second word?")
# find_anagram(word, anagram)
