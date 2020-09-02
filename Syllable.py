# 13/01/2020

# Josh Mullin       2067221
# Thomas Hunt       4646221
# Thomas Passmore   6656924
# Thomas Roff       7783190





import doctest

#DEBUG = False
#def debug(string):
#    if DEBUG:
#        print(string)


"""Function that takes a word and returns the number of syllable it conatains
   Paramter: word. The word to count the syllables in
   Returns: count. The number of syllables in the word
"""
def num_syllable(word):
    """
    >>> num_syllable("skrillex")
    2
    >>> num_syllable("doctest")
    2
    >>> num_syllable("Thomas")
    2
    >>> num_syllable("Joshua")
    3
    >>> num_syllable("date")
    1
    >>> num_syllable("are")
    1
    >>> num_syllable("potato")
    3
    >>> num_syllable("lamest")
    2
    >>> num_syllable("macer")
    2
    >>> num_syllable("police")
    2
    >>> num_syllable("home")
    1
    >>> num_syllable("digital")
    3
    >>> num_syllable("analog")
    3
    >>> num_syllable("computer")
    3
    >>> num_syllable("onomatopoeia")
    6
    >>> num_syllable("words")
    1
    >>> num_syllable("computer")
    3
    >>> num_syllable("safe")
    1
    >>> num_syllable("safer")
    2
    >>> num_syllable("straw")
    1
    >>> num_syllable("exam")
    2
    >>> num_syllable("examination")
    5
    >>> num_syllable("system")
    2
    >>> num_syllable("master")
    2
    >>> num_syllable("mastermind")
    3
    >>> num_syllable("comment")
    2
    >>> num_syllable("mention")
    2
    >>> num_syllable("mystery")
    3
    >>> num_syllable("tenant")
    2
    >>> num_syllable("fog")
    1
    >>> num_syllable("complex")
    2
    >>> num_syllable("blank")
    1
    >>> num_syllable("greeting")
    2
    >>> num_syllable("constitution")
    4
    >>> num_syllable("crescent")
    2
    >>> num_syllable("renumerate")
    4
    >>> num_syllable("mathematics")
    4
    >>> num_syllable("hostility")
    4
    >>> num_syllable("unfortunate")
    4
    >>> num_syllable("23")
    'Error: 23 is not a valid word'
    >>> num_syllable("!@#$")
    'Error: !@#$ is not a valid word'
   """
    count = 0
    # list containing vowels characters
    vowels = ['a', 'e', 'i', 'o', 'u']
    # list of all of the vowel characters with y added
    vowelsY = ['a', 'e', 'i', 'o', 'u', 'y']
    
    # checks if the entered word has at least one character and that it is part of alphabet
    # not a number or special character
    if len(word) < 1 or not word.isalpha():
        return "Error: " + word + " is not a valid word"
    
    # adds one to the count if the first letter of the word is a vowel
    if word[0].lower() in vowels:
        count += 1
        
        
    for i in range(len(word)):
        
        # stops index out of bounds error    
        if i == len(word) - 1:
            break
        
        # checks if letter is a constanant and if so whether a vowel(including Y) follows it, if true increment syllable count
        if(word[i] not in vowelsY and word[i+1] in vowelsY):
            count += 1
            
            
    # if word ends with 'e' then we subtract from the syllable count to prevent errors from words such as 'race' and 'place'
    if word[len(word) - 1] == 'e' and not word[len(word) -2] == "l":
        count -= 1
        
    # words with the suffix 'ed' are often not pronounced with a corresponding vowel sound, except for the case when this
    # is prepended with 't' or 'd'
    if word[-2:] == 'ed' and len(word) > 3 and (word[-3] != 't' and word[-3] != 'd'):
        count -= 1
        
        
    # increments count for cases where a vowel after an 'i' creates a syllable such as in 'curious'
    if "ia" in word or "io" in word or "iu" in word or "ie" in word:
        count += 1
        
    
    #decrements count for cases with words ending with 'ion' to counteract any false additions cause by the 'io' case in above if statememt
    if "ion" in word:
        count -= 1
        
    
    # increments count for cases where 'eal' creates a syllable such as in 'veal'
    if "eal" in word:
        count += 1
        
    
    # increments count for cases when an 'a' following a 'u' creates a syllable such as in 'evaluate'
    if "ua" in word:
        count += 1    
    
    
        
    # word must have at least one syllable        
    if count <= 0:
        count = 1
    
    return count





import fileinput
import sys

if (len(sys.argv) > 1 and sys.argv[1] == '-t'):
    doctest.testmod()
else:
    print("Enter a word and we will count the number of syllables")
    print("Note: Non-aplhabetic symbols such as numbers or special characters will not be accepted")

    for line in fileinput.input():
        
        word = line.split();
        if(len(word) > 1):
            print("Please make sure input has only one word per line")
            continue
        elif(len(word) == 0):
            continue
        
        print(num_syllable(word[0]))
          

    
        
