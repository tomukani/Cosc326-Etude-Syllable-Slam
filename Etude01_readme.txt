Josh Mullin     2067221
Thomas Hunt     4646221
Thomas Passmore 6656924
Thomas Roff     7783190

10/01/2020

This program was made for etude 1 of COSC326

To run the program navigate to directory containing Syllable.py then type in
terminal: `python3 Syllable.py`

To test a list of files, you should use unix style piping,
```bash
$ cat words.txt | python3 Syllable.py
```
otherwise, running `python3 Syllable.py` will open a prompt to read user input,
you should type each word seperated by a new line. Note that if you don't press
enter after the last word, the program won't know you finished the last word!

To run our doctests which are within the Syllable.py file type in terminal: 
python3 Syllable.py -t -v

Our test cases were chosen by using randomly generated words of different
syllable lengths.

We used a mob programming approach with all of us around one pc collaborating
on how to write the code, with Thomas Hunt doing the majority of the typing.
Josh came up with our main case of defining a syllable of a vowel following a
consonant and Thomas Roff also helped to brainstorm other cases such as counting
a syllable when a word has 'i' followed by another vowels. We all created our
doctests together, and Thomas Passmore did most of the debugging when our tests
were failing.
