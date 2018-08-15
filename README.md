# work-with-wordlists
some python scripts to merge and create wordlists
wordlists are always in the format that each word is separated by a new line.
Hint: the word charset might be irritating, it can not only contain chars, but whole strings

usage:

powersetwl.py: 
creates a wordlist containing the powerset of a given charset with a fixed length. You probably have to manually edit the length("pwlen":default = 3) and the charset(default = all upper and lowercase letters + numbers 0-9), also create the file wordlist.txt in the same folder as powersetwl.py since the output will be written to this file.
e.G.: charset = ['a', 'b', 'c', 'd']; pwlen=3 -> abc abd acd bcd 

powersetwlupuntil.py:
creates a wordlist containing powersets of a given charset up until a fixed length. For further usage see powersetwl.py
e.G.: charset = ['a', 'b', 'c' ]; pwlen = 3 -> a b c ab ac bc abc


wltocharset.py:
takes a wordlist(needs to be named wordlist.txt) and gives out a ready to use charset list to the console which you can use in the other provided scripts that work with charsets
