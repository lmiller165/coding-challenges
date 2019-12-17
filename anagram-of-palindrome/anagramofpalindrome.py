"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""




def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""



    #loop through the dictionary
    #check for a fast fail - if key is not divisible by 2, return false. 
    #else return true 

    #loop through the word and: 
    #make dictionary using the letters whose value is the list of how many times
    #the leters appear. 

    #new approach just add value

    #------------
    #ex: racecar
    #------------
    #{r : [r, r], 
    # a: [a, a], 
    # c: [c, c],
    # e: [e]} 

    #create empty dict
    #loop through the string provided
    #check if letter is in dict
    #if not add it to the dict with value of 1
    #else add 1 to the value of that key. 
    #empty_dict: 
    #
    letter_dict = {}

    for letter in word: 
        if letter in letter_dict:
            letter_dict[letter] = letter_dict[letter] + 1
        else: 
            letter_dict[letter] = 1

    #for key in dict:
    #if length of list is even
    count = 0

    for value in letter_dict.values():
        if value % 2 !=0:
            count = count + 1

    if count > 1: 
        return False

    return True

        

    # value = letter_dict.values()





    #if len of dict is equal to on and len of key value is odd,
        #return true. 

    #else
    #return false.







if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
