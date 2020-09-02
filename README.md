# Cosc326-Etude-Syllable-Slam
Josh Mullin     
Thomas Hunt     
Thomas Passmore 
Thomas Roff     

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
