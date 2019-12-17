"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""
words = [w.strip() for w in open('words.txt')]

def make_anagram_dict(words):
    """Return dict mapping sorted letters -> [words w/ those letters]


        >>> make_anagram_dict(["act", "cat", "dog", "god"])
        {'dgo': ['dog', 'god'], 'act': ['act', 'cat']}
    """
    

    #add first word to a dictionary with a value of a list
    #initialize an empty dictionary {key: empty_list}

    #for word in words: 
    #if sorted word in dict => append word to key_list
    #else add sorted word as key in dict with emtpy list value. 

    anagram_dict = {}

    for word in words:

        sorted_word = ''.join(sorted(word))
        # print(word, sorted_word)

        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)

        else: 
            anagram_dict[sorted_word] = [word]

    # for key in anagram_dict:
    #     print(anagram_dict[key])

    return anagram_dict



def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""
    
    anagram_dict = make_anagram_dict(wordlist)
    most_anagrams = None
    longest_list = 0

    for key in anagram_dict:
        if len(anagram_dict[key]) > longest_list:
            most_anagrams = anagram_dict[key][0]
            longest_list = len(anagram_dict[key])



    return most_anagrams

    #loop through dictionary
        #the first key is the word to return

    #Set largest dict[key] to variable
    #use len(dict.get()) 



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
